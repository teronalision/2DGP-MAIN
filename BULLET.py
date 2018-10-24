from math import *

class bullet:

    
    def __init__(self,x,y,i):
        self.x, self.y = x, y
        self.v, self.r = 0, 0
        self.image = i

    def order(self,v,r):
        self.v += v
        self.r += r

    def update(self):

        self.x += self.v *sin(radians(self.r))
        self.y += self.v *cos(radians(self.r))