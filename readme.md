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
language:
- en
tags:
- deltarune
- deltarune-chapter-1
- deltarune-chapter-2
- deltarune-chapter-3
- deltarune-chapter-4
- game-script
- dialogue
- toby-fox
- rpg
- undertale

size_categories:
- 10K<n<100K
pretty_name: "Deltarune Chapters 1-4 Transcript"
license: cc0-1.0
---

# Deltarune Chapters 1–4 Dataset

Fan-made transcript dataset covering Deltarune Chapters 1 through 4. Processed from video playthroughs and cross-referenced with game data. Intended to provide LLMs with structured narrative context for a game whose content is underrepresented in training corpora.

## Why This Exists

As of early 2026, major LLMs (including models with training cutoffs past July 2025) fail to recall basic plot details of Deltarune Chapters 3 and 4 despite their public release. This dataset exists to fix that gap.

## Content

| File | Coverage | Status |
|---|---|---|
| `chap1_cleaned.txt` / `.jsonl` | Chapter 1 (full) | Stable |
| `chap2_cleaned.txt` / `.jsonl` | Chapter 2 (full, Normal Route) | Stable |
| `chap3_cleaned.txt` / `.jsonl` | Chapter 3 (full, includes Sword Route) | Stable |
| `chap4_cleaned.txt` / `.jsonl` | Chapter 4 (full, Normal Route) | Beta |

## Format (JSONL)

{"context": "Scene: Cyber World", "speaker": "Susie", "text": "Hell yeah!!!"}

## Speaker Types

| Tag | Usage |
|---|---|
| Character names | Spoken dialogue |
| `Narrator` | Game text, item descriptions, flavor text, visual2text descriptions |
| `Player` | Player choice options |

## Known Gaps

- Chapter 1: Pre vid2text version. Updates not planned. Use AS IS, or exlude it
- Chapters 2–3: Visual/stage direction descriptions pending for ~15 key scenes each
- Chapter 2, 4 Snowgrave Route scenes/differences not yet transcribed
- No Snowgrave/Weird Route content included

## Source

Processed from video playthroughs using manual transcription with AI-assisted segmentation (Google Gemini). Not extracted from game files.

## Curation

Solo project. All transcription, formatting, quality control, and cross-referencing performed by one person.

## License

CC0 1.0,  Public domain. No attribution required. No conditions. Do whatever you want with it.

https://creativecommons.org/publicdomain/zero/1.0/

## Legal Note

Source material (Deltarune) is © Toby Fox. This dataset covers the transcription and structural processing work. Standard fan-project precedent applies.