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
- 1K<n<10K
pretty_name: Deltarune Chapters 2 & 3 (Unofficial Transcript)
size_categories:
- 1K<n<10K
---

# Deltarune Chapters 2 & 3 Dataset

This dataset contains cleaned and formatted transcripts from **Deltarune Chapter 2** and **Chapter 3 (English)**.
It is processed from video-to-text logs to provide high-quality dialogue and narrative text for NLP tasks.

## Content
- `chap2_cleaned.txt`: Narrative script format of Chapter 2.
- `chap3_cleaned.txt`: Narrative script format of Chapter 3.
- `chap2_dataset.jsonl`: JSON Lines format for instruction tuning/chatbots.
- `chap3_dataset.jsonl`: JSON Lines format for instruction tuning/chatbots.

## Format (JSONL)
```json
{"context": "Scene: Cyber World", "speaker": "Susie", "text": "Hell yeah!!!"}
```

## Source
Processed from raw logs using `process_deltarune.py`.
