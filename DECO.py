from pico2d import *




class Deco:

    def __init__(self,image,x,y,w,h):
        self.image = image
        self.x, self.y = x,y
        self.w, self.h = w,h

    def update(self):
        pass

    def draw(self):

        self.image.draw_to_origin(self.x,self.y,self.w,self.h)