from pico2d import *
import ENGINE



class Deco:

    def __init__(self,image,x,y,w,h):
        self.image = image
        self.x, self.y = x,y
        self.w, self.h = w,h
        self.timer = -1.0
        self.o = 1.0

    def update(self):
        if self.timer >=0:
            if self.timer <=2:
                self.o -= 0.1
            
        if(self.timer >4):
            self.o=0

        self.timer += ENGINE.frame_time
        self.image.opacify(self.o)
        pass

    def draw(self):

        self.image.draw_to_origin(self.x,self.y,self.w,self.h)