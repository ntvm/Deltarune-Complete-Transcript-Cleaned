---
dataset_info:
  features:
  - name: speaker
    dtype: string
  - name: text
    dtype: string
  - name: context
    dtype: string
task_categories:
- text-generation
- conversation
language:
- en
tags:
- deltarune
- game-script
- dialogue
- deltarune-chapter-2
- deltarune-chapter-3
size_categories:
- 10K<n<100K
pretty_name: Deltarune Chapters 2, 3 & 4 (Unofficial Transcript)
size_categories:
- 10K<n<100K
license: cc0-1.0
---

# Deltarune Chapters 2 & 3 Dataset

This dataset contains cleaned and formatted transcripts from **Deltarune Chapter 2**, **Chapter 3** and alpha version of **Chapter 4**(English).
It is processed from video-to-text logs to provide high-quality dialogue and narrative text for NLP tasks.

## Content
- `chap2_cleaned.txt`: Narrative script format of Chapter 2.
- `chap3_cleaned.txt`: Narrative script format of Chapter 3.
- `chap4_cleaned.txt`: Narrative script format of Chapter 4.
- `chap2_dataset.jsonl`: JSON Lines format for instruction tuning/chatbots.
- `chap3_dataset.jsonl`: JSON Lines format for instruction tuning/chatbots.
- `chap4_dataset.jsonl`: JSON Lines format for instruction tuning/chatbots.

## Format (JSONL)
```json
{"context": "Scene: Cyber World", "speaker": "Susie", "text": "Hell yeah!!!"}
```

## Source
Processed from raw logs using `process_deltarune.py`.

## License
This dataset is released under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).
Do whatever you want with it.
