#!/usr/bin/env python3
"""『音声学概説』精選版 別冊音源の生成。

    python3 gen_audio.py            # すべて生成
    python3 gen_audio.py shepard    # 指定したものだけ

合成で作れる音源のみを扱う。人間の発話の録音が要るものは
`v2/audio/音源台帳.md` に別途記載してある。
"""
import numpy as np, soundfile as sf, os, sys

FS = 22050
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'out')

def save(name, x, fs=FS):
    x = np.asarray(x, dtype=float)
    peak = np.max(np.abs(x)) or 1.0
    x = 0.85 * x / peak
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, name)
    sf.write(p, x, fs)
    dur = (len(x) if x.ndim == 1 else x.shape[0]) / fs
    print(f'  {name}  {dur:.1f}s')

def fade(x, ms=15, fs=FS):
    n = int(fs * ms / 1000)
    if len(x) < 2 * n:
        return x
    w = np.ones(len(x))
    w[:n] = np.linspace(0, 1, n)
    w[-n:] = np.linspace(1, 0, n)
    return x * w

# ---------------------------------------------------------------- 第6章

def shepard(duration=40.0, n_oct=7, f_base=32.7, cycle=12.0, fs=FS):
    """無限音階。1周期で1オクターブ上がり、元の状態に戻る。"""
    t = np.arange(int(duration * fs)) / fs
    phase = (t / cycle) % 1.0            # 0→1 で 1 オクターブ
    out = np.zeros_like(t)
    lo, hi = np.log2(f_base), np.log2(f_base * 2 ** n_oct)
    mid, half = (lo + hi) / 2, (hi - lo) / 2
    for k in range(n_oct):
        l2f = np.log2(f_base * 2 ** k) + phase
        amp = np.exp(-0.5 * ((l2f - mid) / (half / 1.6)) ** 2)   # 釣鐘型
        out += amp * np.sin(2 * np.pi * np.cumsum(2 ** l2f) / fs)
    return fade(out, 300)

def shepard_pair(chroma_a, chroma_b, tone=0.5, gap=0.15, n_oct=7, fs=FS):
    """三全音パラドックス用のシェパード音対。chroma は 0–11 の半音位置。"""
    def one(chroma):
        t = np.arange(int(tone * fs)) / fs
        out = np.zeros_like(t)
        lo, hi = np.log2(32.7), np.log2(32.7 * 2 ** n_oct)
        mid, half = (lo + hi) / 2, (hi - lo) / 2
        for k in range(n_oct):
            l2f = np.log2(32.7 * 2 ** k) + chroma / 12
            amp = np.exp(-0.5 * ((l2f - mid) / (half / 1.6)) ** 2)
            out += amp * np.sin(2 * np.pi * (2 ** l2f) * t)
        return fade(out, 20)
    return np.concatenate([one(chroma_a), np.zeros(int(gap * fs)), one(chroma_b)])

def tritone():
    """三全音（6半音）離れた対を4組。上がったか下がったかを答えさせる。"""
    seg, sil = [], np.zeros(int(1.2 * FS))
    for c in (0, 3, 6, 9):
        seg += [shepard_pair(c, (c + 6) % 12), sil]
    return np.concatenate(seg)

def octave_illusion(duration=8.0, f_lo=400.0, f_hi=800.0, seg=0.25, fs=FS):
    """オクターブ錯聴。左右の耳に高低を交互に、位相を反転させて提示する。"""
    n = int(seg * fs)
    t = np.arange(n) / fs
    hi, lo = fade(np.sin(2 * np.pi * f_hi * t), 10), fade(np.sin(2 * np.pi * f_lo * t), 10)
    L, R = [], []
    for i in range(int(duration / seg)):
        if i % 2 == 0:
            L.append(hi); R.append(lo)
        else:
            L.append(lo); R.append(hi)
    return np.stack([np.concatenate(L), np.concatenate(R)], axis=1)

# ------------------------------------------------- 簡易フォルマント合成

def resonator(x, F, B, fs=FS):
    """時変の2次共振器。F・B は x と同じ長さの配列でもスカラーでもよい。"""
    n = len(x)
    F = np.full(n, F, dtype=float) if np.isscalar(F) else np.asarray(F, dtype=float)
    B = np.full(n, B, dtype=float) if np.isscalar(B) else np.asarray(B, dtype=float)
    C = -np.exp(-2 * np.pi * B / fs)
    Bc = 2 * np.exp(-np.pi * B / fs) * np.cos(2 * np.pi * F / fs)
    A = 1 - Bc - C
    y = np.zeros(n); y1 = y2 = 0.0
    for i in range(n):
        y0 = A[i] * x[i] + Bc[i] * y1 + C[i] * y2
        y[i] = y0; y2, y1 = y1, y0
    return y

def glottal(n, f0_start=120.0, f0_end=95.0, fs=FS):
    """声帯音源。単純なパルス列に軽い低域傾斜をかける。"""
    f0 = np.linspace(f0_start, f0_end, n)
    ph = np.cumsum(f0) / fs
    src = np.zeros(n); last = -1
    for i in range(n):
        cur = int(ph[i])
        if cur != last:
            src[i] = 1.0; last = cur
    return np.convolve(src, np.exp(-np.arange(60) / 12.0), mode='same')

def vocal_tract(src, tracks, bws=(60, 90, 150, 200)):
    y = src
    for F, B in zip(tracks, bws):
        y = resonator(y, F, B)
    return y

def ramp(a, b, n_move, n_hold):
    return np.concatenate([np.linspace(a, b, n_move), np.full(n_hold, b)])

def rl_token(f3_onset, fs=FS):
    """rock–lock 連続体の一段階。F3の出発点だけを変える（Miyawaki らの設計）。"""
    n_tr, n_v = int(0.06 * fs), int(0.22 * fs)
    n = n_tr + n_v
    F1 = ramp(350, 730, n_tr, n_v)
    F2 = ramp(1100, 1150, n_tr, n_v)
    F3 = ramp(f3_onset, 2550, n_tr, n_v)
    F4 = np.full(n, 3400.0)
    voiced = vocal_tract(glottal(n), (F1, F2, F3, F4))
    voiced = fade(voiced, 10)
    clos = np.zeros(int(0.07 * fs))                       # /k/ の閉鎖
    burst = np.random.randn(int(0.012 * fs)) * np.exp(-np.arange(int(0.012 * fs)) / (0.002 * fs))
    burst = resonator(burst, 1900, 300) * 0.35            # 軟口蓋の破裂
    return np.concatenate([voiced, clos, burst])

def rl_continuum():
    return [(f'ch07_rl_{i+1}.wav', rl_token(f3))
            for i, f3 in enumerate(np.linspace(1600, 3000, 7))]

def vot_token(vot_ms, fs=FS):
    """VOT連続体の一段階。破裂の開始から声帯振動開始までの時間だけを変える。

    共通の時間軸の上に破裂・気息・有声を重ねる。こうしないと、VOTが
    破裂そのものの長さより短い段階を作れない。
    """
    F = (730.0, 1100.0, 2450.0, 3400.0)
    lead = int(0.05 * fs)                       # 先行する無音
    n_burst = int(0.008 * fs)
    n_v = int(0.30 * fs)
    onset = lead + int(vot_ms / 1000 * fs)      # 声帯振動の開始位置
    total = max(lead + n_burst, onset + n_v) + int(0.02 * fs)
    y = np.zeros(total)

    burst = np.random.randn(n_burst) * np.exp(-np.arange(n_burst) / (0.0015 * fs))
    y[lead:lead + n_burst] += resonator(burst, 700, 400) * 0.5     # 両唇の破裂

    n_asp = onset - (lead + n_burst)                                # 気息の区間
    if n_asp > 0:
        noise = np.random.randn(n_asp) * np.linspace(0.6, 0.25, n_asp)
        y[lead + n_burst:onset] += vocal_tract(noise, F) * 0.5

    y[onset:onset + n_v] += fade(vocal_tract(glottal(n_v), F), 8)
    return y

def vot_continuum():
    return [(f'ch07_vot_{i+1}.wav', vot_token(v)) for i, v in enumerate(range(0, 70, 10))]

# ---------------------------------------------------------------- 実行

TASKS = {
    'shepard':  lambda: [('ch06_shepard_tone.wav', shepard())],
    'tritone':  lambda: [('ch06_tritone_paradox.wav', tritone())],
    'octave':   lambda: [('ch06_octave_illusion.wav', octave_illusion())],
    'rl':       rl_continuum,
    'vot':      vot_continuum,
}

# =================================================== 追加音源（第2〜6章）

def glottal_pulses(n, f0_start, f0_end, fs=FS, jitter=0.0, shimmer=0.0):
    """パルス位置を明示的に置く声帯音源。

    jitter は周期の、shimmer は振幅のばらつき（比率）。きしみ声は、
    周期が長く不規則で、パルスごとの振幅も揺れる状態として作る。
    """
    src = np.zeros(n)
    t, k = 0.0, 0
    while True:
        f0 = f0_start + (f0_end - f0_start) * min(t / max(n / fs, 1e-9), 1.0)
        period = fs / f0 * (1 + np.random.randn() * jitter)
        i = int(t * fs)
        if i >= n:
            break
        src[i] = 1.0 * (1 + np.random.randn() * shimmer)
        t += max(period, 1) / fs
        k += 1
    return np.convolve(src, np.exp(-np.arange(60) / 12.0), mode='same')

def vowel(F, dur=0.55, f0=(125, 105), fs=FS, jitter=0.0, shimmer=0.0, breathy=0.0):
    """定常母音を1つ合成する。F は (F1, F2, F3, F4)。"""
    n = int(dur * fs)
    src = glottal_pulses(n, f0[0], f0[1], fs, jitter, shimmer)
    if breathy:                                  # 息もれ声：非周期成分を混ぜる
        src = src + np.random.randn(n) * breathy
    return fade(vocal_tract(src, F), 25)

JP_VOWELS = {                                    # 東京方言の五母音（代表値）
    'a': (800, 1300, 2550, 3400), 'i': (300, 2200, 3000, 3600),
    'u': (350, 1250, 2200, 3400), 'e': (500, 1900, 2600, 3500),
    'o': (500,  850, 2500, 3400),
}

def jp_five_vowels():
    """第4章1節：スペクトログラムで見る「あいうえお」。"""
    sil = np.zeros(int(0.12 * FS))
    seg = []
    for v in ('a', 'i', 'u', 'e', 'o'):
        seg += [vowel(JP_VOWELS[v], dur=0.75), sil]
    return [('ch04_aiueo.wav', np.concatenate(seg))]

def f0_vowel(f0_contour, F=(800, 1300, 2550, 3400), fs=FS):
    """指定したF0曲線で母音を合成する。声調・アクセントの提示に使う。"""
    n = len(f0_contour)
    ph = np.cumsum(f0_contour) / fs
    src = np.zeros(n); last = -1
    for i in range(n):
        c = int(ph[i])
        if c != last:
            src[i] = 1.0; last = c
    src = np.convolve(src, np.exp(-np.arange(60) / 12.0), mode='same')
    return fade(vocal_tract(src, F), 25)

def chinese_tones():
    """第5章4節：中国語の四声。同じ母音の上で高さのパターンだけを変える。"""
    d = int(0.45 * FS); t = np.linspace(0, 1, d)
    contours = {
        '1_high':    np.full(d, 200.0),                       # 第一声 高平
        '2_rising':  140 + 90 * t ** 1.4,                     # 第二声 上昇
        '3_dipping': 130 - 45 * np.sin(np.pi * t) + 60 * t ** 3,   # 第三声 低降昇
        '4_falling': 230 - 130 * t ** 0.7,                    # 第四声 下降
    }
    sil = np.zeros(int(0.25 * FS))
    out = []
    for k, c in contours.items():
        out.append((f'ch05_tone_{k}.wav', np.concatenate([f0_vowel(c), sil])))
    return out

def viet_tones():
    """第5章4節：ベトナム語の声調のうち、声門化を伴うもの（高さだけでは区別できない）。"""
    d = int(0.45 * FS); t = np.linspace(0, 1, d)
    plain = f0_vowel(np.full(d, 150.0))
    creaky_c = 150 - 25 * t
    x = f0_vowel(creaky_c)
    m = int(0.45 * d)                              # 後半をきしみ声にする
    tail = vowel((800, 1300, 2550, 3400), dur=(d - m) / FS, f0=(95, 72), jitter=0.07, shimmer=0.25)
    x = np.concatenate([x[:m], tail[:d - m]])
    sil = np.zeros(int(0.25 * FS))
    return [('ch05_viet_plain.wav', np.concatenate([plain, sil])),
            ('ch05_viet_creaky.wav', np.concatenate([fade(x, 25), sil]))]

def jp_accent():
    """第5章3節：日本語の三つのアクセント型。「あめ」相当の2モーラで示す。"""
    d = int(0.30 * FS)
    hi, lo = 190.0, 130.0
    types = {
        'atamadaka': (np.full(d, hi), np.full(d, lo)),      # 頭高（雨）
        'heiban':    (np.full(d, lo), np.full(d, hi)),      # 平板（飴）
        'odaka':     (np.full(d, lo), np.full(d, hi)),      # 尾高（助詞で下がる）
    }
    sil = np.zeros(int(0.25 * FS))
    out = []
    for k, (c1, c2) in types.items():
        a = f0_vowel(c1, JP_VOWELS['a'])
        e = f0_vowel(c2, JP_VOWELS['e'])
        seg = [a, e]
        if k == 'odaka':                                     # 助詞「が」で下がる
            seg.append(f0_vowel(np.full(int(0.28 * FS), lo), JP_VOWELS['a']))
        out.append((f'ch05_accent_{k}.wav', np.concatenate(seg + [sil])))
    return out

def rhythm():
    """第5章5節：モーラ拍と強勢拍の対比。中身のない模式音で時間構造だけを示す。"""
    def beat(dur, amp, f0=150.0):
        return amp * f0_vowel(np.full(int(dur * FS), f0), JP_VOWELS['a'])
    mora = np.concatenate([beat(0.14, 1.0) for _ in range(10)])          # 等しい長さの拍
    stress = np.concatenate(sum(([beat(0.26, 1.0), beat(0.10, 0.45), beat(0.10, 0.45)]
                                 for _ in range(4)), []))                # 強-弱-弱
    sil = np.zeros(int(0.5 * FS))
    return [('ch05_rhythm_mora.wav', mora), ('ch05_rhythm_stress.wav', stress),
            ('ch05_rhythm_pair.wav', np.concatenate([mora, sil, stress]))]

def voice_quality():
    """第12章3節：通常声・きしみ声・息もれ声。同じ母音で発声様式だけを変える。"""
    F = JP_VOWELS['a']
    sil = np.zeros(int(0.25 * FS))
    return [('ch12_modal.wav',   np.concatenate([vowel(F, 0.7), sil])),
            ('ch12_creaky.wav',  np.concatenate([vowel(F, 0.7, f0=(64, 54), jitter=0.07, shimmer=0.28), sil])),
            ('ch12_breathy.wav', np.concatenate([vowel(F, 0.7, breathy=0.30), sil]))]

def tap_vs_trill():
    """第2章5節：スペイン語 pero と perro。はじき音とふるえ音の対立。"""
    F_e = (500, 1900, 2600, 3500); F_o = (500, 850, 2500, 3400)
    def tap():
        n = int(0.022 * FS)
        return np.zeros(n)                                   # ごく短い閉鎖
    def trill(n_beat=3):
        seg = []
        for _ in range(n_beat):
            seg += [np.zeros(int(0.018 * FS)),
                    0.5 * vowel((400, 1400, 2400, 3400), dur=0.016, f0=(120, 120))]
        return np.concatenate(seg)
    pe = vowel(F_e, 0.16, f0=(130, 125))
    o  = vowel(F_o, 0.30, f0=(122, 100))
    sil = np.zeros(int(0.3 * FS))
    return [('ch02_pero.wav',  np.concatenate([pe, tap(), o])),
            ('ch02_perro.wav', np.concatenate([pe, trill(), o])),
            ('ch02_pero_perro.wav',
             np.concatenate([pe, tap(), o, sil, pe, trill(), o]))]

def masking_demo():
    """第6章3節：マスキング。同じ弱音が、雑音の帯域によって聞こえたり消えたりする。"""
    d = int(0.9 * FS); t = np.arange(d) / FS
    target = 0.12 * np.sin(2 * np.pi * 2000 * t)
    def band_noise(center, width):
        n = np.random.randn(d)
        S = np.fft.rfft(n); f = np.fft.rfftfreq(d, 1 / FS)
        S[(f < center - width / 2) | (f > center + width / 2)] = 0
        return np.fft.irfft(S, d)
    near = band_noise(2000, 400); near *= 0.9 / (np.max(np.abs(near)) or 1)
    far  = band_noise(500, 400);  far  *= 0.9 / (np.max(np.abs(far)) or 1)
    sil = np.zeros(int(0.4 * FS))
    return [('ch06_masking.wav', np.concatenate([
        fade(target, 30), sil,                       # 目標音だけ
        fade(target + 0.55 * far, 30), sil,          # 遠い帯域の雑音と一緒に（聞こえる）
        fade(target + 0.55 * near, 30)]))]           # 近い帯域の雑音と一緒に（消える）

TASKS.update({
    'aiueo':   jp_five_vowels,
    'tones':   chinese_tones,
    'viet':    viet_tones,
    'accent':  jp_accent,
    'rhythm':  rhythm,
    'voice':   voice_quality,
    'trill':   tap_vs_trill,
    'masking': masking_demo,
})

if __name__ == '__main__':
    want = sys.argv[1:] or list(TASKS)
    for k in want:
        print(f'[{k}]')
        for name, x in TASKS[k]():
            save(name, x)
