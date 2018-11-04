from math import *
from pico2d import *
import ENGINE



class bullet:

    
    def __init__(self,x,y,size):
        self.x, self.y = x, y
        self.v, self.r = 0, 0
        self.size = size
        self.image = 2

    def order(self,v,r):
        self.v += v
        self.r += r

    def update(self):

        self.x += self.v *sin(radians(self.r)) *ENGINE.frame_time *ENGINE.p_per_meter
        self.y += self.v *cos(radians(self.r)) *ENGINE.frame_time *ENGINE.p_per_meter

    def draw(self):
        ENGINE.bimage[self.image].clip_draw(16,772-(16*4),16,16,self.x,self.y,10,10)