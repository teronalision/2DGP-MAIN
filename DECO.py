from pico2d import *
import ENGINE

new_deco = 1

class Deco:

    def __init__(self,image,x,y,w,h,frame = 0):
        self.image = image
        self.x, self.y = x,y
        self.w, self.h = w,h
        self.timer = -1.0
        self.o = 1.0
        self.frame = frame

    def update(self):
        if self.timer >=0:
            if self.timer <=2:
                self.o -= 0.1
            
        if(self.timer >4):
            self.o=0

        self.timer += ENGINE.frame_time
        if self.frame == 0:
            self.image.opacify(self.o)
        pass

    def draw(self):
        if self.frame == 0:
            self.image.draw_to_origin(self.x,self.y,self.w,self.h)
        else:
            frame = int(self.timer*self.frame)
            self.image.clip_draw(frame*150,0,150,150,self.x,self.y,self.w,self.h)