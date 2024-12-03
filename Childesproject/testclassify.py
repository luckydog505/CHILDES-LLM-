# test_classify.py
import unittest
from classify import get_head_position, classify_head_position, analyze_head_position

class TestClassifyModule(unittest.TestCase):
    def test_get_head_position(self):
        # Test input compounds with expected head positions
        test_cases = [
            ("big drum", "final"),
            ("high-speed", "final"),
            ("ice-cream", "final"),
            ("speed train", "final"),
            ("Mother-in-law", "final"),
            ("swimming pool", "final"),
            ("overcoat", "final"),
            ("output", "final"),
            ("input", "final"),
            ("child care", "final"),
            ("redhead", "final"),
            ("greenhouse", "final"),
            ("blackbird", "final"),
            ("bookstore", "final"),
            ("toothbrush", "final"),
            ("father-in-law", "final"),
            ("post office", "final"),
            ("basketball", "final"),
            ("laptop", "final"),
            ("breakfast", "final"),
            ("classroom", "final"),
            ("sunflower", "final"),
            ("railroad", "final"),
            ("teacup", "final"),
            ("airport", "final"),
            ("haircut", "final"),
            ("raincoat", "final"),
            ("password", "final"),
            ("notebook", "final"),
            ("fireman", "final"),
            ("grandmother", "final"),
            ("blueberry", "final"),
            ("sandcastle", "final"),
            ("underdog", "final"),
            ("desktop", "final"),
            ("milkshake", "final"),
            ("homework", "final"),
            ("bedroom", "final"),
            ("friendship", "final"),
            ("moonlight", "final"),
            ("birthday", "final"),
            ("football", "final"),
            ("seahorse", "final"),
            ("jellyfish", "final"),
            ("snowball", "final"),
            ("bookcase", "final"),
            ("playground", "final"),
            ("earring", "final"),
            ("eyebrow", "final"),
            ("handshake", "final"),
            ("typewriter", "final"),
            ("doorknob", "final"),
            ("waterfall", "final"),
        ]

        for compound, expected_head_position in test_cases:
            with self.subTest(compound=compound):
                head_position = get_head_position(compound)
                self.assertEqual(head_position, expected_head_position,
                                 f"Compound '{compound}' expected to be '{expected_head_position}' but got '{head_position}'.")

    def test_classify_head_position(self):
        # Test input compounds
        compounds = [
            "big drum",
            "high-speed",
            "ice-cream",
            "speed train",
            "Mother-in-law",
            "swimming pool"
        ]

        # Expected classification
        expected_classification = [
            {"compound": "big drum", "head_position": "final"},
            {"compound": "high-speed", "head_position": "final"},
            {"compound": "ice-cream", "head_position": "final"},
            {"compound": "speed train", "head_position": "final"},
            {"compound": "Mother-in-law", "head_position": "final"},
            {"compound": "swimming pool", "head_position": "final"},
        ]

        classified_results = classify_head_position(compounds)
        self.assertEqual(classified_results, expected_classification,
                         f"Expected {expected_classification} but got {classified_results}")

    def test_analyze_head_position(self):
        # Test input
        classified_compounds = [
            {"compound": "big drum", "head_position": "final"},
            {"compound": "high-speed", "head_position": "final"},
            {"compound": "ice-cream", "head_position": "final"},
            {"compound": "speed train", "head_position": "final"},
            {"compound": "Mother-in-law", "head_position": "final"},
            {"compound": "swimming pool", "head_position": "final"},
        ]

        # Expected counts
        expected_counts = {"final": 6}

        head_counts = analyze_head_position(classified_compounds)
        self.assertEqual(dict(head_counts), expected_counts,
                         f"Expected {expected_counts} but got {dict(head_counts)}")

if __name__ == '__main__':
    unittest.main()
