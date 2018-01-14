import unittest
from bowling import Game

class TestGame(unittest.TestCase):
    
    def test_TwoThrowsNoMark(self):
        g = Game.Game()
        g.add(5)
        g.add(4)
        self.assertEqual(9, g.score())
        self.assertEqual(2,g.getCurrentFrame())

    def test_FourThrowsNoMark(self):
        g = Game.Game()
        g.add(5)
        g.add(4)
        g.add(7)
        g.add(2)
        self.assertEqual(18, g.score())
        self.assertEqual(9, g.scoreForFrame(1))
        self.assertEqual(18, g.scoreForFrame(2))
        self.assertEqual(3,g.getCurrentFrame())
    
    def test_SimpleSpare(self):
        g = Game.Game()
        g.add(3)
        g.add(7)
        g.add(3)
        self.assertEqual(13,g.scoreForFrame(1))
        self.assertEqual(2,g.getCurrentFrame())
    
    def test_SimpleAfterSparre(self):
        g = Game.Game()
        g.add(3)
        g.add(7)
        g.add(3)
        g.add(2)
        self.assertEqual(18,g.score())
        self.assertEqual(18,g.scoreForFrame(2))
        self.assertEqual(13,g.scoreForFrame(1))
        self.assertEqual(3,g.getCurrentFrame())

    def test_test(self):
        g = Game.Game()
        g.add(10)
        g.add(3)
        g.add(6)
        self.assertEqual(19,g.scoreForFrame(1))
        self.assertEqual(28,g.score())
        self.assertEqual(3,g.getCurrentFrame())






