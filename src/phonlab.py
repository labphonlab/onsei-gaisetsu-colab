"""Dependency-light common core for the book labs."""
import json, platform, random, sys, urllib.request, wave
from pathlib import Path
import numpy as np, pandas as pd, matplotlib.pyplot as plt
SEED=2027; AUDIO_RAW="https://raw.githubusercontent.com/labphonlab/onsei-gaisetsu-colab/main/audio/out"
def setup(seed=SEED):
 global SEED; SEED=seed; random.seed(seed); np.random.seed(seed); plt.rcParams.update({"figure.figsize":(8,3.8),"axes.grid":True,"grid.alpha":.25}); print(f"PhonLab ready (seed={seed}).")
def show_environment():
 d={"python":sys.version.split()[0],"platform":platform.platform(),"numpy":np.__version__,"pandas":pd.__version__,"seed":SEED}; print(json.dumps(d,ensure_ascii=False,indent=2)); return d
def fetch_asset(name,mode="demo"):
 if mode=="research":
  p=input("自分のwavファイルのパス: ").strip()
  if not p: raise ValueError("Research Modeではファイルを指定してください。")
  return Path(p)
 for p in (Path("../../audio/out")/name,Path("../audio/out")/name,Path(name)):
  if p.exists(): return p
 p=Path(name); urllib.request.urlretrieve(f"{AUDIO_RAW}/{name}",p); return p
def load_wav(path):
 with wave.open(str(path),"rb") as w: sr,n,width,c=w.getframerate(),w.getnframes(),w.getsampwidth(),w.getnchannels(); raw=w.readframes(n)
 if width!=2: raise ValueError("16-bit PCM wavを使用してください。")
 y=np.frombuffer(raw,dtype="<i2").astype(float)/32768
 if c>1: y=y.reshape(-1,c).mean(1)
 return sr,y
def display_audio(y,sr):
 try:
  from IPython.display import Audio,display; display(Audio(y,rate=sr))
 except Exception: print(f"audio: {len(y)/sr:.2f}s")
def plot_waveform_and_spectrum(y,sr,title="audio"):
 t=np.arange(len(y))/sr; f=np.fft.rfftfreq(len(y),1/sr); a=np.abs(np.fft.rfft(y*np.hanning(len(y)))); fig,ax=plt.subplots(1,2,figsize=(10,3.2)); ax[0].plot(t,y,lw=.7); ax[0].set(xlabel="Time (s)",ylabel="Amplitude",title=title); ax[1].plot(f,20*np.log10(a/a.max()+1e-8),lw=.8); ax[1].set(xlim=(0,min(5000,sr/2)),ylim=(-80,2),xlabel="Frequency (Hz)",ylabel="Relative level (dB)"); plt.tight_layout(); plt.show(); return fig
def demo_dataset(ch):
 x=np.linspace(0,1,80); y=1/(1+np.exp(-(x-.5)*(5+ch/2))) if ch in (7,10,13) else np.sin(2*np.pi*(1+ch%4)*x)*np.exp(-x/1.4); return x,y
def plot_demo(x,y,title="demo"): plt.plot(x,y,lw=2); plt.xlabel("Manipulated value (normalized)"); plt.ylabel("Observed value (teaching demo)"); plt.title(title); plt.tight_layout(); plt.show()
def describe_demo(ch,ns):
 y=np.asarray(ns.get("y",[])); return pd.Series({"chapter":ch,"n":len(y),"range":float(np.ptp(y)) if len(y) else np.nan,"note":"教材用観察"})
def manipulate_demo(ch,p,ns):
 y=np.asarray(ns.get("y",demo_dataset(ch)[1])); x=np.arange(len(y))/(ns.get("sr",len(y))); plt.plot(x,y*p); plt.title(f"parameter={p}"); plt.xlabel("Time / index"); plt.ylabel("Scaled value"); plt.tight_layout(); plt.show()
def make_trial_list(ch,n_repetitions=2,seed=SEED):
 rows=[]
 for rep in range(n_repetitions):
  for i,level in enumerate(np.linspace(0,1,7)): rows.append({"participant":"demo","session":1,"trial":len(rows)+1,"stimulus":f"ch{ch:02d}_{i+1}","condition":f"level_{i+1}","item":i+1,"speaker":"demo","level":level})
 return pd.DataFrame(rows).sample(frac=1,random_state=seed).reset_index(drop=True)
def simulate_responses(t,seed=SEED):
 print("注意: 動作確認用の模擬反応であり、実測データではありません。"); rng=np.random.default_rng(seed); d=t.copy(); p=1/(1+np.exp(-8*(d.level-.5))); d["response"]=(rng.random(len(d))<p).astype(int); d["correct"]=np.nan; d["rt"]=rng.lognormal(6.2,.18,len(d)); d["data_status"]="SIMULATED_DEMO_ONLY"; return d
def summarize_responses(d): return d.groupby(["condition","level"],as_index=False).agg(n=("response","size"),response_rate=("response","mean"),mean_rt=("rt","mean"))
def plot_response_summary(s): plt.plot(s.level,s.response_rate,"o-"); plt.ylim(-.05,1.05); plt.xlabel("Condition level"); plt.ylabel("Response proportion"); plt.title("SIMULATED DEMO — not a research result"); plt.tight_layout(); plt.show()
def combine_class_data(files): return pd.concat([pd.read_csv(f) for f in files],ignore_index=True)
def save_environment(path,seed=SEED,mode="demo"):
 d={"book_version":"selected-v2","notebook_version":"1.0.0","python":sys.version,"platform":platform.platform(),"seed":seed,"mode":mode,"date_executed":pd.Timestamp.now().isoformat()}; Path(path).write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding="utf-8")


# Common experiment-builder interfaces. Precise timing belongs in jsPsych.
def _task_trials(task, chapter=0, n_repetitions=2, seed=SEED):
    d=make_trial_list(chapter,n_repetitions,seed); d["task"]=task; return d
def make_identification_experiment(**kwargs): return _task_trials("identification",**kwargs)
def make_discrimination_experiment(**kwargs): return _task_trials("discrimination",**kwargs)
def make_ax_experiment(**kwargs): return _task_trials("AX",**kwargs)
def make_abx_experiment(**kwargs): return _task_trials("ABX",**kwargs)
def make_rating_experiment(**kwargs): return _task_trials("rating",**kwargs)
def make_lexical_decision_experiment(**kwargs): return _task_trials("lexical_decision",**kwargs)
def make_gating_experiment(**kwargs): return _task_trials("gating",**kwargs)
def make_training_experiment(**kwargs): return _task_trials("training",**kwargs)

def summarize_participants(data):
    cols={"trials":("trial","size")}
    if "correct" in data and data.correct.notna().any(): cols["accuracy"]=("correct","mean")
    if "rt" in data: cols["median_rt"]=("rt","median")
    return data.groupby("participant",as_index=False).agg(**cols)
def calculate_accuracy(data):
    if "correct" not in data or not data.correct.notna().any(): raise ValueError("実測または採点済みのcorrect列が必要です。")
    return float(data.correct.mean())
def calculate_dprime(hits,false_alarms,eps=1e-5):
    from statistics import NormalDist
    h=min(max(float(hits),eps),1-eps); f=min(max(float(false_alarms),eps),1-eps)
    return NormalDist().inv_cdf(h)-NormalDist().inv_cdf(f)
def plot_reaction_times(data):
    clean=data.loc[data.rt.notna(),"rt"]; plt.hist(clean,bins=20); plt.xlabel("Reaction time (ms)"); plt.ylabel("Count"); plt.tight_layout(); plt.show()
def plot_psychometric_curve(data):
    s=summarize_responses(data); plot_response_summary(s); return s
