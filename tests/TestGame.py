import unittest
from bowling import Game

class TestGame(unittest.TestCase):

    def test_TwoThrowsNoMark(self):
        g = Game.Game()
        g.add(5)
        g.add(4)
        self.assertEqual(9, g.score())

    def test_FourThrowsNoMark(self):
        g = Game.Game()
        g.add(5)
        g.add(4)
        g.add(7)
        g.add(2)
        self.assertEqual(18, g.score())
        self.assertEqual(9, g.scoreForFrame(1))
        self.assertEqual(18, g.scoreForFrame(2))

    def test_SimpleSpare(self):
        g = Game.Game()
        g.add(3)
        g.add(7)
        g.add(3)
        self.assertEqual(13,g.scoreForFrame(1))

    def test_SimpleAfterSparre(self):
        g = Game.Game()
        g.add(3)
        g.add(7)
        g.add(3)
        g.add(2)
        self.assertEqual(18,g.score())
        self.assertEqual(18,g.scoreForFrame(2))
        self.assertEqual(13,g.scoreForFrame(1))

    def test_test(self):
        g = Game.Game()
        g.add(10)
        g.add(3)
        g.add(6)
        self.assertEqual(19,g.scoreForFrame(1))
        self.assertEqual(28,g.score())

    def test_PerfectGame(self):
        g = Game.Game()
        for i in range(12):
            g.add(10)
        self.assertEqual(300,g.score())

    def test_EndOfArray(self):
        g = Game.Game()
        for _ in range(9):
            g.add(0)
            g.add(0)
        g.add(2)
        g.add(8)
        g.add(10)
        self.assertEqual(g.score(), 20)

    def test_SampleGame(self):
        g = Game.Game()
        g.add(1)
        g.add(4)
        g.add(4)
        g.add(5)
        g.add(6)
        g.add(4)
        g.add(5)
        g.add(5)
        g.add(10)
        g.add(0)
        g.add(1)
        g.add(7)
        g.add(3)
        g.add(6)
        g.add(4)
        g.add(10)
        g.add(2)
        g.add(8)
        g.add(6)
        self.assertEqual(g.score(), 133)

    def test_HeartBreak(self):
        g = Game.Game()
        for i in range(11):
            g.add(10)
        g.add(9)
        self.assertEqual(299,g.score())

    def test_TenthFrameSpare(self):
        g = Game.Game()
        for i in range(9):
            g.add(10)
        g.add(9)
        g.add(1)
        g.add(1)
        self.assertEqual(270,g.score())
