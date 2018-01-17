from bowling import Score

class Game(object):

    def __init__(self):
        self.itsScorer = Score.Score()
        self.itsCurrentFrame = 0
        self.firstThrowInFrame = True

    def score(self):
        return self.scoreForFrame(self.itsCurrentFrame)

    def add(self, pins):
        self.itsScorer.addThrow(pins)
        self.adjustCurrentFrame(pins)

    def adjustCurrentFrame(self,pins):
        if(self.lastBallInFrame(pins)):
            self.advanceFrame()
            self.firstThrowInFrame = True
        else:
            self.firstThrowInFrame = False

    def lastBallInFrame(self,pins):
        return self.strike(pins) or (not self.firstThrowInFrame)

    def strike(self, pins):
        return (self.firstThrowInFrame and pins == 10)

    def advanceFrame(self):
        self.itsCurrentFrame += 1
        self.itsCurrentFrame = min(10,self.itsCurrentFrame)

    def scoreForFrame(self, theFrame):
        return self.itsScorer.scoreForFrame(theFrame)
