from math import *
from pico2d import *
import ENGINE



class Bullet:

    
    def __init__(self,x,y,type):
        self.x, self.y = x, y
        self.v, self.r = 0, 0
        self.type = type
        #self.image = 2
        self.d = 0
        self.dead = False
        if(type == ENGINE.RECT):
            self.size = 20
        elif(type == ENGINE.CIRCLE):
            self.size = 10


    def order(self,v,r):
        self.v += v
        self.r += r

    def kill(self):
        pass

    def update(self):

        self.x += self.v *sin(self.r) *ENGINE.frame_time *ENGINE.p_per_meter
        self.y += self.v *cos(self.r) *ENGINE.frame_time *ENGINE.p_per_meter

        if(self.type == ENGINE.CIRCLE):
            self.d +=radians(1)

        if(self.x < 0 or self.x > 500 or self.y <0 or self.y >600):
            self.dead = True


    def draw(self):
        if(ENGINE.rect_mode):
            draw_rectangle(self.x -self.size, self.y -self.size, self.x +self.size, self.y +self.size)
        
        if(self.type == ENGINE.RECT):
            ENGINE.bimage[2].clip_composite_draw(32,32*3,32,32,-self.r,'',self.x,self.y,self.size*2,self.size*2)
        if(self.type == ENGINE.CIRCLE):
            ENGINE.bimage[2].clip_composite_draw(32,256-32,32,32,self.d,'',self.x,self.y,self.size*2,self.size*2)