# extract.py
import re
import nltk
from nltk.util import ngrams

# Ensure NLTK data is downloaded
nltk.download('stopwords', quiet=True)

def clean_utterance(utterance):
    """
    Remove annotations and special characters from utterance.
    """
    # Remove annotations like [: word], [*], etc.
    utterance = re.sub(r'\[.*?\]', '', utterance)
    # Remove pauses and other symbols (e.g., '...', '(.)')
    utterance = re.sub(r'\([^\)]*\)', '', utterance)
    # Remove any remaining non-word characters except hyphens and apostrophes
    utterance = re.sub(r"[^\w\s'-]", '', utterance)
    # Convert multiple spaces to single space
    utterance = re.sub(r'\s+', ' ', utterance)
    # Remove leading and trailing whitespace
    utterance = utterance.strip()
    return utterance.lower()

def extract_compounds(utterances, verbose=False):
    """
    Extract potential compounds from utterances using refined patterns.
    """
    hyphenated_pattern = r'\b\w+(?:-\w+)+\b'  # Hyphenated compounds

    compounds = []
    for utt in utterances:
        utt_text = clean_utterance(utt)

        if verbose:
            print(f"Processing utterance: {utt_text}")

        # Extract hyphenated compounds
        matches = re.findall(hyphenated_pattern, utt_text)

        filtered_matches = [
            m.strip() for m in matches
            if is_valid_compound(m)
        ]

        compounds.extend(filtered_matches)

        # Tokenize the utterance
        tokens = utt_text.split()

        # Extract n-grams (bigrams and trigrams)
        for n in range(2, 4):
            for gram in ngrams(tokens, n):
                ngram_text = ' '.join(gram)
                if is_valid_compound(ngram_text):
                    compounds.append(ngram_text)

        if verbose and filtered_matches:
            print(f"Hyphenated compounds found: {filtered_matches}")

    # Ensure unique compounds only
    unique_compounds = list(set(compounds))
    return unique_compounds

def is_valid_compound(compound):
    """
    Validate compound to ensure it has a meaningful structure.
    """
    words = re.split(r'\s+|-', compound)
    if len(words) < 2:
        return False
    if not all(re.match(r"^[\w'-]+$", word) for word in words):
        return False
    return True
