import unittest
from bowling import FrameFile
from bowling import Game

class TestFrame(unittest.TestCase):
    f = FrameFile.Frame()
    g = Game.Game()
    def test_ScoreNoThrows(self):
        self.f.itsScore = 0
        self.assertEqual(0, self.f.getScore())

    def test_AddOneThrow(self):
        self.f.add(5)
        self.assertEqual(5, self.f.getScore())

    def test_oneThrow(self):
        self.g.add(5)
        self.assertEqual(5, self.g.score())
