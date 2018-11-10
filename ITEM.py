from pico2d import *
import ENGINE



class Item:

    def __init__(self,x,y):
        self.x, self.y = x, y
        self.size = 10
        self.v = -1


    def update(self):
        self.y += self.v * ENGINE.frame_time *ENGINE.p_per_meter

        self.v = max(self.v-0.1 , 1)
        pass


    def draw(self):
        ENGINE.bimage[1].clip_draw(32,256-64*5,16,16,self.x,self.y,self.size,self.size)
        pass