# 『音声学概説』Colab Labs

**Read → Experience → Manipulate → Experiment → Analyze → Replicate → Extend → Research** を支える実習パッケージです。

1. **Open in Colab** を開く。 2. `Copy to Drive` でコピーする。 3. 上から実行し、`PARAMETER` を変える。 4. 教材用データと研究データを混同しない。

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

`notebooks/` は章別Lab、`src/phonlab.py` は共通基盤、`templates/` は最小Lab、`experiments/` はブラウザ実験連携、`demo_data/` はデータ境界、`licenses/` は権利区分です。

模擬データは動作確認専用で、研究結果ではありません。厳密な反応時間測定はjsPsych等で行います。他者から研究目的でデータを集める場合は、事前に倫理手続きを確認してください。


## 公開範囲

このリポジトリは『音声学概説』の実習教材のみを公開する。書籍本文、権利未処理の録音、第三者コーパス、参加者データは含まない。`audio/out/` の37音源は数式から生成した教材用合成音であり、生成方法と限界は `audio/音源台帳.md` に記録している。

## 再現と検証

```bash
python -m pip install -r requirements.txt
MPLBACKEND=Agg python scripts/validate_notebooks.py
```

GitHub Actionsでも、14章のNotebookについて必須節、Python構文、全コードセル、付属音源の読み込みを検証する。Research Builderは構造と構文を検証する。

## ライセンス

- コード: MIT License
- Notebook本文とオリジナル図: CC BY 4.0
- 合成音源: `audio/音源台帳.md` を参照
- 第三者資料・コーパス・参加者データ: 同梱しない
