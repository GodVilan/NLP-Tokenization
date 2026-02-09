"""
NLP Tokenization Assignment - Q5
Language: English

This program demonstrates:
1. Naïve space-based tokenization
2. Manually corrected tokenization
3. Tokenization using an NLP tool (NLTK)
4. Comparison and explanation of differences
5. Multiword Expressions (MWEs)
6. Reflection

Author: SRIKANTH REDDY NANDIREDDY
Student ID: 700773949
"""

# -----------------------------
# Import libraries
# -----------------------------
import nltk
from nltk.tokenize import word_tokenize

# -----------------------------
# Download required NLTK data
# (Required for Python 3.12+)
# -----------------------------
for pkg in ['punkt', 'punkt_tab']:
    try:
        nltk.data.find(f'tokenizers/{pkg}')
    except LookupError:
        nltk.download(pkg)

# -----------------------------
# Original Paragraph
# -----------------------------
text = (
    "I can’t believe it’s already February! "
    "NLP isn’t easy, but it’s incredibly useful. "
    "People don’t always realize how complex language really is."
)

print("Original Paragraph:\n")
print(text)
print("\n" + "-" * 60)

# -----------------------------
# 1. Naïve Space-Based Tokenization
# -----------------------------
naive_tokens = text.split()

print("\n1. Naïve Space-Based Tokens:\n")
print(naive_tokens)
print("\n" + "-" * 60)

# -----------------------------
# 2. Manually Corrected Tokens
# -----------------------------
manual_tokens = [
    'I', 'can', "n't", 'believe', 'it', "'s", 'already', 'February', '!',
    'NLP', 'is', "n't", 'easy', ',', 'but', 'it', "'s",
    'incredibly', 'useful', '.',
    'People', 'do', "n't", 'always', 'realize', 'how',
    'complex', 'language', 'really', 'is', '.'
]

print("\n2. Manually Corrected Tokens:\n")
print(manual_tokens)
print("\n" + "-" * 60)

# -----------------------------
# Highlight Differences
# -----------------------------
print("\nDifferences Between Naïve and Manual Tokenization:\n")
print("February!  -> February, !")
print("easy,      -> easy, ,")
print("useful.   -> useful, .")
print("can’t     -> can, n't")
print("isn’t     -> is, n't")
print("don’t     -> do, n't")
print("\n" + "-" * 60)

# -----------------------------
# Normalize smart quotes
# -----------------------------
normalized_text = (
    text.replace("’", "'")
        .replace("‘", "'")
)

# -----------------------------
# 3. Tokenization Using NLP Tool
# -----------------------------
tool_tokens = word_tokenize(normalized_text)

print("\n3. NLTK Tokenization Output:\n")
print(tool_tokens)
print("\n" + "-" * 60)

# -----------------------------
# Comparison Explanation
# -----------------------------
print("\nComparison: Manual vs NLTK Tokens\n")
print(
    "NLTK follows Penn Treebank conventions. "
    "For example, contractions like \"can't\" are tokenized as "
    "\"ca\" + \"n't\" instead of \"can\" + \"n't\". "
    "Manual tokenization focuses on linguistic intuition, "
    "while NLTK prioritizes consistency for statistical NLP tasks."
)
print("\n" + "-" * 60)

# -----------------------------
# 4. Multiword Expressions (MWEs)
# -----------------------------
print("\n4. Multiword Expressions (MWEs):\n")

mwes = [
    "incredibly useful",
    "realize how complex",
    "language really is"
]

for mwe in mwes:
    print(f"- {mwe}")

print("\nExplanation:")
print(
    "These expressions function as single semantic units. "
    "Splitting them can reduce meaning and negatively affect "
    "tasks such as sentiment analysis and syntactic parsing."
)
print("\n" + "-" * 60)

# -----------------------------
# 5. Reflection
# -----------------------------
print("\n5. Reflection:\n")
print(
    "The hardest part of tokenization in English is handling contractions, "
    "since different standards split them differently. Compared to English, "
    "languages with richer morphology can be more difficult to tokenize. "
    "Punctuation increases complexity because it sometimes conveys meaning "
    "and sometimes structure. Multiword expressions are challenging because "
    "their meaning is often non-compositional. Even in English, these factors "
    "make tokenization a non-trivial task."
)

print("\n" + "-" * 60)
print("End of Program")
