# test_extract.py
import unittest
from extract import extract_compounds

class TestExtractCompounds(unittest.TestCase):
    def test_extract_compounds(self):
        sample_utterances = [
            "I have a brother-in-law.",
            "She likes ice cream and apple pie.",
            "This is my children's playground.",
            "He is a kindergarten teacher.",
            "They went to New York City.",
            "Look at the sunset over the mountain range.",
            "Here's a mother-in-law's tale.",
            "I saw a fire-breathing dragon.",
            "He works part-time at the bookstore.",
            "The quick brown fox jumps over the lazy dog.",
            "She's a stay-at-home mom.",
            "Let's play hide-and-seek.",
            "They visited the Empire State Building.",
            "It's a one-of-a-kind experience.",
            "He gave me a high five.",
            "We need to schedule a follow-up meeting.",
            "He is an ex-marine.",
            "They live in a cul-de-sac.",
            "She received a full-time offer.",
            "They took a red-eye flight."
        ]

        expected_compounds = set([
            "brother-in-law",
            "ice cream",
            "apple pie",
            "children's playground",
            "kindergarten teacher",
            "new york",
            "new york city",
            "mountain range",
            "mother-in-law's",
            "fire-breathing",
            "part-time",
            "stay-at-home",
            "hide-and-seek",
            "empire state building",
            "one-of-a-kind",
            "high five",
            "follow-up",
            "ex-marine",
            "cul-de-sac",
            "full-time",
            "red-eye"
        ])

        extracted_compounds = set(extract_compounds(sample_utterances))

        # Check that all expected compounds are extracted
        missing_compounds = expected_compounds - extracted_compounds
        self.assertTrue(expected_compounds.issubset(extracted_compounds),
            f"Missing compounds: {missing_compounds}")

        # Optionally, check that there are no unexpected compounds
        unexpected_compounds = extracted_compounds - expected_compounds
        self.assertEqual(len(unexpected_compounds), 0,
            f"Unexpected compounds found: {unexpected_compounds}")

if __name__ == '__main__':
    unittest.main()
