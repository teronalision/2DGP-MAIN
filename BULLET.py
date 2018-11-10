from math import *
from pico2d import *
import ENGINE



class bullet:

    
    def __init__(self,x,y,size):
        self.x, self.y = x, y
        self.v, self.r = 0, 0
        self.size = size
        self.image = 2
        self.d = 0
        self.dead = False

    def order(self,v,r):
        self.v += v
        self.r += r

    def update(self):

        self.x += self.v *sin(radians(self.r)) *ENGINE.frame_time *ENGINE.p_per_meter
        self.y += self.v *cos(radians(self.r)) *ENGINE.frame_time *ENGINE.p_per_meter

        self.d +=1

        if(self.x < 0 or self.x > 500 or self.y <0 or self.y >600):
            self.dead = True


    def draw(self):
        if(ENGINE.rect_mode):
            draw_rectangle(self.x -self.size, self.y -self.size, self.x +self.size, self.y +self.size)
        ENGINE.bimage[self.image].clip_composite_draw(32,256-32,32,32,radians(self.d),'',self.x,self.y,self.size*2,self.size*2)