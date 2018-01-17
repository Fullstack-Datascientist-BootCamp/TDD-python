import unittest
from bowling import Frame

class TestFrame(unittest.TestCase):

    def test_ScoreNoThrows(self):
        f = Frame.Frame()
        f.itsScore = 0
        self.assertEqual(0, f.getScore())

    def test_AddOneThrow(self):
        f = Frame.Frame()
        f.add(5)
        self.assertEqual(5, f.getScore())
