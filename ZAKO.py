import ENGINE
import SPONER
from pico2d import *


class zako:


    def __init__(self, x, y, f, image = None):
        self.x, self.y = x,y
        self.vx, self.vy = 0.0
        self.form = f
        self.image = image

        if f == 0:
            self.x,self.y = 0,600
            self.vx,self.vy = 1,-1
            self.sponer = None
        elif f == 1:
            self.sponer = SPONER.Sponer(200,500)

    def update(self):
        self.x += self.vx*ENGINE.p_per_meter*ENGINE.frame_time
        self.y += self.vy*ENGINE.p_per_meter*ENGINE.frame_time

        self.sponer.update()

        pass


    def draw(self):
        self.image.draw(self.x,self.y)
        
        self.sponer.draw()
        pass