# NLP Tokenization Assignment – Q5

## Student Information
- Name: SRIKANTH REDDY NANDIREDDY
- Student ID: 700773949
- Course: Natural Language Processing

---

## Assignment Overview
This project addresses **Q5 – Tokenization** from the NLP assignment.
The goal is to demonstrate and compare different tokenization approaches
in English, including manual and tool-based methods.

---

## Tasks Implemented

### 1. Naïve Tokenization
- Tokenization is performed using simple whitespace splitting.
- This approach does not handle punctuation or contractions correctly.

### 2. Manual Tokenization
- Tokens are manually corrected by:
  - Separating punctuation (., !, ,)
  - Handling contractions and clitics (e.g., *can't → can + n't*)
- Differences between naïve and manual tokenization are highlighted.

### 3. NLP Tool Comparison
- Tokenization is performed using **NLTK (`word_tokenize`)**.
- Smart quotes are normalized to avoid Unicode issues.
- Differences between manual and NLTK tokenization are explained using
  Penn Treebank conventions.

### 4. Multiword Expressions (MWEs)
- Identifies three multiword expressions:
  - *incredibly useful*
  - *realize how complex*
  - *language really is*
- Explains why these expressions should be treated as single semantic units.

### 5. Reflection
- Discusses challenges in English tokenization.
- Compares English with morphologically richer languages.
- Explains the impact of punctuation and MWEs on tokenization.

---

## Tools and Technologies
- Python 3
- NLTK (Natural Language Toolkit)

---

## How to Run
pip install nltk  
python tokenization_q5_final.py
