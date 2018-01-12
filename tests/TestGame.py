import unittest
from bowling import Game

class TestGame(unittest.TestCase):
    g = Game.Game()
    def test_TwoThrowsNoMark(self):
        self.g.add(5)
        self.g.add(4)
        self.assertEqual(9, self.g.score())

    def test_FourThrowsNoMark(self):
        self.g.add(5)
        self.g.add(4)
        self.g.add(7)
        self.g.add(2)
        self.assertEqual(18, self.g.score())
        self.assertEqual(9, self.g.scoreForFrame(1))
        self.assertEqual(18, self.g.scoreForFrame(2))
