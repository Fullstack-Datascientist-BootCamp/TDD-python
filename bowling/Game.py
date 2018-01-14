
class Game(object):
    itsScore = 0
    itsThrows = []
    itsCurrentThrow = 0
    itsCurrentFrame = 1
    firstThrow = True
    def score(self):
        return self.itsScore 
    def add(self, pins):
        self.itsThrows.insert(self.itsCurrentThrow, pins) 
        self.itsCurrentThrow += 1
        self.itsScore += pins
        self.adjustCurrentFrame()

    def adjustCurrentFrame(self):
                
        if(self.firstThrow):
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
            if(frameScore == 10):
                score += frameScore + self.itsThrows[ball + 2]
             
            else:
                score += frameScore
            ball +=2
        return score
    def getCurrentFrame(self):
#        return 1 + flour((self.itsCurrentThrow - 1)/2)
       # return ceil(self.itsCurrentThrow/2)
       return self.itsCurrentFrame
