import re

def extract_compounds(utterances):
    """
    Extract potential compounds from a list of utterances.
    """
    compound_patterns = [
        r'\b\w+-\w+\b',  # Hyphenated compounds
        r'\b\w+\s+\w+\b',  # Two consecutive words (simple heuristic)
    ]
    
    compounds = []
    for utt in utterances:
        # Ensure we are working with the text of the utterance
        if hasattr(utt, 'text'):
            utt_text = utt.text
        else:
            utt_text = str(utt)

        for pattern in compound_patterns:
            matches = re.findall(pattern, utt_text)
            if matches:
                compounds.extend(matches)
    return compounds
