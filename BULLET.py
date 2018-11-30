from math import *
from pico2d import *
import ENGINE

STAR, KNIFE, CART, BALL, SUN = range(5)

class Bullet:

    
    def __init__(self,x,y,type):
        self.x, self.y = x, y
        self.v, self.r = 0, 0
        self.name = type
        self.d = 0
        self.dead = False
        if(type == KNIFE):
            self.size = 20
            self.type = ENGINE.RECT
        elif(type == STAR):
            self.size = 20
            self.type = ENGINE.CIRCLE
        elif(type == CART):
            self.size = 10
            self.type = ENGINE.RECT
        elif(type == BALL):
            self.size = 15
            self.type = ENGINE.CIRCLE
        elif(type == SUN):
            self.size = 16
            self.type = ENGINE.RECT
        

    def order(self,v,r):
        self.v += v
        self.r += r

    def kill(self):
        pass

    def update(self):

        self.x -= self.v *sin(self.r) *ENGINE.frame_time *ENGINE.p_per_meter
        self.y += self.v *cos(self.r) *ENGINE.frame_time *ENGINE.p_per_meter

        if(self.x < 0 or self.x > 500 or self.y <0 or self.y >600):
            self.dead = True


    def draw(self):
        gap = 0
        if(ENGINE.rect_mode):
            draw_rectangle(self.x -self.size, self.y -self.size, self.x +self.size, self.y +self.size)
            
        if(self.name == KNIFE):
            ENGINE.bimage[2].clip_composite_draw(32,32*3,32,32,self.r,'',self.x,self.y,self.size*2+gap,self.size*2+gap)
        elif(self.name == STAR):
            ENGINE.bimage[2].clip_composite_draw(32,256-32,32,32,self.d,'',self.x,self.y,self.size*2+gap,self.size*2+gap)
        elif(self.name == CART):
            ENGINE.bimage[2].clip_composite_draw(32*5,32,32,32,self.r,'',self.x,self.y,self.size*2+gap,self.size*2+gap)
        elif(self.name == BALL):
            ENGINE.bimage[4].clip_composite_draw(32*3,16+32*3,32,32,self.r,'',self.x,self.y,self.size*2+gap,self.size*2+gap)
        elif(self.name == SUN):
            ENGINE.bimage[2].clip_composite_draw(32*6,32,32,32,self.r,'',self.x,self.y,self.size*2+gap,self.size*2+gap)
        