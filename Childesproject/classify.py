def classify_head_position(compounds):
    """
    Classify compounds as head-initial or head-final.
    """
    head_results = []
    for compound in compounds:
        words = compound.split()
        if len(words) == 2:  # Simple check for two-word compounds
            head_results.append({
                "compound": compound,
                "head_position": "final" if words[-1].isalpha() else "initial"
            })
    return head_results


def analyze_head_position(classified_compounds):
    """
    Count the occurrences of head-initial and head-final compounds.
    """
    from collections import Counter
    positions = [result["head_position"] for result in classified_compounds]
    return Counter(positions)
