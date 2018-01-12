class Game(object):
    itsScore = 0
    itsThrows = []
    itsCurrentThrow = 0
    def score(self):
        return self.itsScore 
    def add(self, pins):
        self.itsThrows.insert(self.itsCurrentThrow, pins) 
        self.itsCurrentThrow += 1
        self.itsScore += pins
    def scoreForFrame(self, theFrame):
        score = 0
        ball = 0
        for currentFrame in range(theFrame):
            firstThrow = self.itsThrows[ball] 
            secondThrow = self.itsThrows[ball + 1]
            score = firstThrow + secondThrow
            ball += 2
        return score
