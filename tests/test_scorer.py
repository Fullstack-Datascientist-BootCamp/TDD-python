import unittest
from bowling import score


class TestScore(unittest.TestCase):

    def test_first_throw(self):
        score_list = []
        pins = 3
        current_score = score(pins, score_list)
        self.assertEqual(current_score, 3)

    def test_second_throw(self):
        score_list = [3]
        pins = 6
        current_score = score(pins, score_list)
        self.assertEqual(current_score, 6)


if __name__ == "__main__":
    unittest.main()
