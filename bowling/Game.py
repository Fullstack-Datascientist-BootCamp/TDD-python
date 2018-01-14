
class Game(object):
    itsScore = 0
    itsThrows = []
    itsCurrentThrow = 0
    itsCurrentFrame = 1
    firstThrow = True
    def score(self):
        return self.scoreForFrame(self.getCurrentFrame() - 1)
    
    def add(self, pins):
        self.itsThrows.insert(self.itsCurrentThrow, pins) 
        self.itsCurrentThrow += 1
        self.itsScore += pins
        self.adjustCurrentFrame(pins)

    def adjustCurrentFrame(self,pins):
        if(self.firstThrow):
            if(pins == 10):
                self.itsCurrentFrame += 1
            else:
                self.firstThrow = False
        else:
            self.firstThrow = True
            self.itsCurrentFrame += 1
    
    def scoreForFrame(self, theFrame):
        score = 0
        ball = 0
        for currentFrame in range(theFrame):
            firstThrow = self.itsThrows[ball] 
            secondThrow = self.itsThrows[ball + 1]
            frameScore = firstThrow + secondThrow
            if(firstThrow == 10):
                score += 10 + self.itsThrows[ball + 1] + self.itsThrows[ball +2]
                ball += 1
            else:
                if(frameScore == 10):
                    score += frameScore + self.itsThrows[ball + 2]
                    ball +=2
                else:
                    score += frameScore
                    ball +=2
        return score
    
    def getCurrentFrame(self):
#        return 1 + flour((self.itsCurrentThrow - 1)/2)
       # return ceil(self.itsCurrentThrow/2)
       return self.itsCurrentFrame
