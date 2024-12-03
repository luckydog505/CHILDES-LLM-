# classify.py
import spacy
import wordninja

# Load spaCy's English model
nlp = spacy.load('en_core_web_sm')

def split_compound(word):
    """
    Attempt to split a single-word compound into its components.
    """
    # First, try to split using wordninja
    split_words = wordninja.split(word)
    if len(split_words) > 1:
        return split_words

    # If wordninja fails, use a dictionary-based approach
    import nltk
    from nltk.corpus import words
    nltk.download('words', quiet=True)
    english_words = set(w.lower() for w in words.words())

    # Try splitting at every possible position
    for i in range(1, len(word)):
        left = word[:i]
        right = word[i:]
        if left in english_words and right in english_words:
            return [left, right]
    return [word]  # Return the original word if no split is found

def get_head_position(compound):
    """
    Determine the head position of a compound based on POS tags using spaCy and NLTK's WordNet.
    """
    # Check if the compound is a single word
    if len(compound.strip().split()) == 1:
        # Try to split the word into components
        split_words = split_compound(compound)
        if len(split_words) > 1:
            # Reconstruct the compound with spaces
            compound = ' '.join(split_words)
    
    # Proceed with POS tagging
    doc = nlp(compound)
    words = [token.text for token in doc]
    pos_tags = [(token.text, token.pos_) for token in doc]

    # Import NLTK's WordNet
    import nltk
    nltk.download('wordnet', quiet=True)
    from nltk.corpus import wordnet

    # Find the last noun
    head_index = None
    for i in reversed(range(len(pos_tags))):
        word, tag = pos_tags[i]
        if tag in {'NOUN', 'PROPN'}:
            head_index = i
            break
        else:
            # Check if the word can be a noun in WordNet
            if wordnet.synsets(word, pos=wordnet.NOUN):
                head_index = i
                break
    if head_index is None:
        # Default to the last word if no noun is found
        head_index = len(words) - 1

    if head_index == 0:
        return 'initial'
    elif head_index == len(words) - 1:
        return 'final'
    else:
        return 'unknown'  # For compounds where the head is in the middle

def classify_head_position(compounds):
    """
    Classify compounds as head-initial or head-final.
    """
    head_results = []
    for compound in compounds:
        head_position = get_head_position(compound)
        head_results.append({
            "compound": compound,
            "head_position": head_position
        })
    return head_results

def analyze_head_position(classified_compounds):
    """
    Count the occurrences of head-initial and head-final compounds.
    """
    from collections import Counter
    positions = [result["head_position"] for result in classified_compounds]
    return Counter(positions)
