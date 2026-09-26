# 『音声学概説』Colab Labs

[![Validate notebooks](https://github.com/labphonlab/onsei-gaisetsu-colab/actions/workflows/validate.yml/badge.svg)](https://github.com/labphonlab/onsei-gaisetsu-colab/actions/workflows/validate.yml)
[![Release](https://img.shields.io/github/v/release/labphonlab/onsei-gaisetsu-colab)](https://github.com/labphonlab/onsei-gaisetsu-colab/releases/latest)
[![License: MIT / CC BY 4.0](https://img.shields.io/badge/license-MIT%20%2F%20CC%20BY%204.0-blue.svg)](#ライセンス)

**Read → Experience → Manipulate → Experiment → Analyze → Replicate → Extend → Research** を支える実習パッケージです。

## 最初の5分

1. 下表の **Open in Colab** を選ぶ。
2. Colabで「ドライブにコピー」を選び、自分のコピーを作る。
3. セルを上から順に実行する。
4. `PARAMETER` と示された値を一つずつ変え、音・図・数値の変化を観察する。
5. Notebook末尾の「観察 → 仮説 → 検証 → 限界」を記録する。

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

- `notebooks/`: 章別LabとResearch Builder
- `src/phonlab.py`: 可視化・音響処理・実験を支える共通基盤
- `templates/`: 新しいLabを作るための最小テンプレート
- `experiments/`: ブラウザ実験との連携例
- `audio/`: 教材用合成音と音源台帳
- `demo_data/`: 教材用データと研究データの境界説明
- `licenses/`: 素材ごとの権利区分

## 利用上の注意

模擬データと合成音は、概念理解と動作確認のための教材です。研究結果や実測値として扱わないでください。Colab上の簡易実験は手続きの理解を目的とし、厳密な反応時間測定にはjsPsych等の専用環境が必要です。他者から研究目的でデータを集める場合は、所属機関の倫理手続きとデータ管理方針を事前に確認してください。


## 公開範囲

このリポジトリは『音声学概説』の実習教材のみを公開する。書籍本文、権利未処理の録音、第三者コーパス、参加者データは含まない。`audio/out/` の37音源は数式から生成した教材用合成音であり、生成方法と限界は `audio/音源台帳.md` に記録している。

## 再現と検証

```bash
python -m pip install -r requirements.txt
MPLBACKEND=Agg python scripts/validate_notebooks.py
```

GitHub Actionsでも、14章のNotebookについて必須節、Python構文、全コードセル、付属音源の読み込みを検証する。Research Builderは構造と構文を検証する。

## 引用

教材を授業・研究・成果物で利用した場合は、[`CITATION.cff`](CITATION.cff) の情報を使って引用してください。GitHub画面右側の **Cite this repository** からBibTeX等を取得できます。書籍本文を参照した場合は、書籍も別途引用してください。

## 改善提案と貢献

誤りの報告、教材案、修正提案を歓迎します。個人情報、参加者データ、権利未処理の録音、第三者コーパスをIssueやPull Requestへ添付しないでください。詳しい手順は [`CONTRIBUTING.md`](CONTRIBUTING.md) を参照してください。

## ライセンス

- コード: MIT License
- Notebook本文とオリジナル図: CC BY 4.0
- 合成音源: `audio/音源台帳.md` を参照
- 第三者資料・コーパス・参加者データ: 同梱しない
