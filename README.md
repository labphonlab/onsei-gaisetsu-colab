# 音声学概説 — Colab Labs と付属音源

[![Validate notebooks](https://github.com/labphonlab/onsei-gaisetsu-colab/actions/workflows/validate.yml/badge.svg)](https://github.com/labphonlab/onsei-gaisetsu-colab/actions/workflows/validate.yml)
[![Release](https://img.shields.io/github/v/release/labphonlab/onsei-gaisetsu-colab)](https://github.com/labphonlab/onsei-gaisetsu-colab/releases/latest)
[![License: MIT / CC BY 4.0](https://img.shields.io/badge/license-MIT%20%2F%20CC%20BY%204.0-blue.svg)](#ライセンス)

書籍『音声学概説 ── 声のしくみから音声AIまで』に対応する Colab 実習パッケージと、本文が「聴いてほしい」と指示する**付属音源**です。紙版・電子版のどちらの読者も、無料で利用できます。

## 付属音源

本文の各節が指示する合成音37点を、[`audio/out/`](audio/out/) に置いています。数式から生成した合成音で、授業での提示に制限はありません。**ファイル名を選び、ダウンロードしてから再生してください。**

| 節 | 内容 | ファイル |
|---|---|---|
| 2.5.2 | はじき音とふるえ音（pero / perro） | [`ch02_pero.wav`](audio/out/ch02_pero.wav)<br>[`ch02_perro.wav`](audio/out/ch02_perro.wav)<br>[`ch02_pero_perro.wav`](audio/out/ch02_pero_perro.wav) |
| 4.1.1 | 「あいうえお」（自分の声で試せないときの予備） | [`ch04_aiueo.wav`](audio/out/ch04_aiueo.wav) |
| 5.3.1 | 日本語のアクセント三型 | [`ch05_accent_atamadaka.wav`](audio/out/ch05_accent_atamadaka.wav)<br>[`ch05_accent_heiban.wav`](audio/out/ch05_accent_heiban.wav)<br>[`ch05_accent_odaka.wav`](audio/out/ch05_accent_odaka.wav) |
| 5.4.1 | 中国語の四声 | [`ch05_tone_1_high.wav`](audio/out/ch05_tone_1_high.wav)<br>[`ch05_tone_2_rising.wav`](audio/out/ch05_tone_2_rising.wav)<br>[`ch05_tone_3_dipping.wav`](audio/out/ch05_tone_3_dipping.wav)<br>[`ch05_tone_4_falling.wav`](audio/out/ch05_tone_4_falling.wav) |
| 5.4.2 | ベトナム語の声調 | [`ch05_viet_plain.wav`](audio/out/ch05_viet_plain.wav)<br>[`ch05_viet_creaky.wav`](audio/out/ch05_viet_creaky.wav) |
| 5.5.1 | モーラ拍と強勢拍のリズム | [`ch05_rhythm_mora.wav`](audio/out/ch05_rhythm_mora.wav)<br>[`ch05_rhythm_stress.wav`](audio/out/ch05_rhythm_stress.wav)<br>[`ch05_rhythm_pair.wav`](audio/out/ch05_rhythm_pair.wav) |
| 6.1.1 | 無限音階（40秒） | [`ch06_shepard_tone.wav`](audio/out/ch06_shepard_tone.wav) |
| 6.3.2 | マスキング | [`ch06_masking.wav`](audio/out/ch06_masking.wav) |
| 6.5.2 | 三全音パラドックス | [`ch06_tritone_paradox.wav`](audio/out/ch06_tritone_paradox.wav) |
| 6.5.3 | オクターブ錯聴（**ヘッドフォン必須**） | [`ch06_octave_illusion.wav`](audio/out/ch06_octave_illusion.wav) |
| 7.1.1 | rock–lock 連続体（7段階） | [`ch07_rl_1.wav`](audio/out/ch07_rl_1.wav)<br>[`ch07_rl_2.wav`](audio/out/ch07_rl_2.wav)<br>[`ch07_rl_3.wav`](audio/out/ch07_rl_3.wav)<br>[`ch07_rl_4.wav`](audio/out/ch07_rl_4.wav)<br>[`ch07_rl_5.wav`](audio/out/ch07_rl_5.wav)<br>[`ch07_rl_6.wav`](audio/out/ch07_rl_6.wav)<br>[`ch07_rl_7.wav`](audio/out/ch07_rl_7.wav) |
| 7.2.2 | VOT連続体（7段階） | [`ch07_vot_1.wav`](audio/out/ch07_vot_1.wav)<br>[`ch07_vot_2.wav`](audio/out/ch07_vot_2.wav)<br>[`ch07_vot_3.wav`](audio/out/ch07_vot_3.wav)<br>[`ch07_vot_4.wav`](audio/out/ch07_vot_4.wav)<br>[`ch07_vot_5.wav`](audio/out/ch07_vot_5.wav)<br>[`ch07_vot_6.wav`](audio/out/ch07_vot_6.wav)<br>[`ch07_vot_7.wav`](audio/out/ch07_vot_7.wav) |
| 12.3.1 | 通常声・きしみ声・息もれ声 | [`ch12_modal.wav`](audio/out/ch12_modal.wav)<br>[`ch12_creaky.wav`](audio/out/ch12_creaky.wav)<br>[`ch12_breathy.wav`](audio/out/ch12_breathy.wav) |

書籍では、各節の **〈付属音源〉** の行に、使うファイル名を示してあります。音源を作った [`audio/scripts/gen_audio.py`](audio/scripts/gen_audio.py) と、制作状況・権利処理の記録 [`audio/音源台帳.md`](audio/音源台帳.md) も公開しています。

**付属しない音声があります。** 9.1.1（年齢の異なる五人の朗読）、11.1.1（学習者の音声二本）、12.1.1（音声クイズ六本）、13.1.1（人間の声と合成音声の判定テスト八本）は、人の声の録音や第三者の権利を要するため付属しません。書籍の各節に **〈付属音源なし〉** の行を置き、代わりの進め方を示しています。

## 授業補助資料

書籍で授業をする教員向けの資料です。全14回(90分)の時間配分、実演の手順、想定される学生の反応、スライド用の要点を収めています。**[Release](https://github.com/labphonlab/onsei-gaisetsu-colab/releases/latest) から PDF を取得してください。** 原稿の Markdown は [`teaching/`](teaching/) にあり、自分の授業に合わせて改変できます。CC BY 4.0 で公開します。

## 正本と刊行時固定版

この公開リポジトリの **main** ブランチを、Notebook・付属音源・授業補助資料の最新版を管理する正本とします。刊行時点の固定版は [v1.0.0 Release](https://github.com/labphonlab/onsei-gaisetsu-colab/releases/tag/v1.0.0) からZIPで取得できます。ReleaseにはSHA-256チェックサムも添付しています。

コードはMIT License、Notebook本文・オリジナル図・授業補助資料はCC BY 4.0で公開します。書籍本文(授業補助資料は除く)、権利未処理の録音、第三者コーパス、参加者データはこのリポジトリに含めません。

## 使い方

**バッジを押すだけです。** Colab が開き、そのまま実行できます。
Googleドライブへのコピーも、ファイルの配置も要りません。

書き換えを残したいときだけ、**ファイル → ドライブにコピーを保存** を一度行ってください。

1. 下表の **Open in Colab** を選ぶ。
2. セルを上から順に実行する。
3. `PARAMETER` と示された値を一つずつ変え、音・図・数値の変化を観察する。
4. Notebook末尾の「観察 → 仮説 → 検証 → 限界」を記録する。

初めて音声分析を行う場合は[第4章「音を測る」](https://colab.research.google.com/github/labphonlab/onsei-gaisetsu-colab/blob/main/notebooks/ch04_data_acoustics.ipynb)、知覚実験を体験する場合は[第7章「音を言葉として聞く」](https://colab.research.google.com/github/labphonlab/onsei-gaisetsu-colab/blob/main/notebooks/ch07_experiment_speech_perception.ipynb)、自分の研究計画へ進む場合は[Research Builder](https://colab.research.google.com/github/labphonlab/onsei-gaisetsu-colab/blob/main/notebooks/ch99_research_builder.ipynb)から始めるのがおすすめです。

## 章別Notebook

| 章 | 内容 | Lab種別 | Colab |
|---:|---|---|---|
| 1 | 音声学への招待 | Demo | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/labphonlab/onsei-gaisetsu-colab/blob/main/notebooks/ch01_demo_introduction.ipynb) |
| 2 | 声を作る | Demo | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/labphonlab/onsei-gaisetsu-colab/blob/main/notebooks/ch02_demo_speech_production.ipynb) |
| 3 | 音を書く | Data | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/labphonlab/onsei-gaisetsu-colab/blob/main/notebooks/ch03_data_ipa.ipynb) |
| 4 | 音を測る | Data | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/labphonlab/onsei-gaisetsu-colab/blob/main/notebooks/ch04_data_acoustics.ipynb) |
| 5 | セグメントを超えて | Demo | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/labphonlab/onsei-gaisetsu-colab/blob/main/notebooks/ch05_demo_prosody.ipynb) |
| 6 | 耳のしくみ | Demo | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/labphonlab/onsei-gaisetsu-colab/blob/main/notebooks/ch06_demo_hearing.ipynb) |
| 7 | 音を言葉として聞く | Experiment | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/labphonlab/onsei-gaisetsu-colab/blob/main/notebooks/ch07_experiment_speech_perception.ipynb) |
| 8 | 話し言葉は崩れる | Data | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/labphonlab/onsei-gaisetsu-colab/blob/main/notebooks/ch08_data_reduction.ipynb) |
| 9 | 音を身につける | Model | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/labphonlab/onsei-gaisetsu-colab/blob/main/notebooks/ch09_model_development.ipynb) |
| 10 | 音そのものが意味を持つ | Experiment | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/labphonlab/onsei-gaisetsu-colab/blob/main/notebooks/ch10_experiment_sound_symbolism.ipynb) |
| 11 | 発音を教える | Data | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/labphonlab/onsei-gaisetsu-colab/blob/main/notebooks/ch11_data_l2_speech.ipynb) |
| 12 | 声は人を映す | Data | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/labphonlab/onsei-gaisetsu-colab/blob/main/notebooks/ch12_data_voice_identity.ipynb) |
| 13 | 話す機械・聞く機械 | Model | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/labphonlab/onsei-gaisetsu-colab/blob/main/notebooks/ch13_model_speech_technology.ipynb) |
| 14 | 声を売る、声を守る | Data | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/labphonlab/onsei-gaisetsu-colab/blob/main/notebooks/ch14_data_voice_ethics.ipynb) |
| 99 | Research Builder | Capstone | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/labphonlab/onsei-gaisetsu-colab/blob/main/notebooks/ch99_research_builder.ipynb) |

## 構成

- `audio/`: 付属音源（`out/`）、生成スクリプト、音源台帳
- `teaching/`: 授業補助資料の原稿(全14回)
- `notebooks/`: 章別LabとResearch Builder
- `src/phonlab.py`: 可視化・音響処理・実験を支える共通基盤
- `templates/`: 新しいLabを作るための最小テンプレート
- `experiments/`: ブラウザ実験との連携例
- `demo_data/`: 教材用データと研究データの境界説明
- `licenses/`: 素材ごとの権利区分

## 利用上の注意

模擬データと合成音は、概念理解と動作確認のための教材です。研究結果や実測値として扱わないでください。Colab上の簡易実験は手続きの理解を目的とし、厳密な反応時間測定にはjsPsych等の専用環境が必要です。他者から研究目的でデータを集める場合は、所属機関の倫理手続きとデータ管理方針を事前に確認してください。

## 再現と検証

```bash
python -m pip install -r requirements.txt
MPLBACKEND=Agg python scripts/validate_notebooks.py
```

GitHub Actionsでも、14章のNotebookについて必須節、Python構文、全コードセル、付属音源の読み込みを検証します。Research Builderは構造と構文を検証します。

## 引用

教材を授業・研究・成果物で利用した場合は、[`CITATION.cff`](CITATION.cff) の情報を使って引用してください。GitHub画面右側の **Cite this repository** からBibTeX等を取得できます。書籍本文を参照した場合は、書籍も別途引用してください。

## ライセンス

- コード: MIT License
- Notebook本文とオリジナル図: CC BY 4.0
- 授業補助資料: CC BY 4.0
- 付属音源: 数式から生成した合成音。授業での提示に制限はありません。詳細は [`audio/音源台帳.md`](audio/音源台帳.md)
- 第三者資料・コーパス・参加者データ: 同梱しません

## 正誤・要望

書籍との不一致、Notebookの不具合、音源の不具合はIssuesでお知らせください。個人情報、参加者データ、権利未処理の録音、第三者コーパスをIssueやPull Requestへ添付しないでください。手順は [`CONTRIBUTING.md`](CONTRIBUTING.md) を参照してください。
