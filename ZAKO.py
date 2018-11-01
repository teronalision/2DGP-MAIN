import ENGINE
import SPONER
from pico2d import *


class zako:


    def __init__(self, x, y, f, image = None):
        self.x, self.y = x,y
        self.vx, self.vy = 0.0, 0.0
        self.form = f
        self.image = image
        self.sponer = None
        if f == 0:
            self.vx,self.vy = 1,-1
        elif f == 1:
            self.sponer = SPONER.Sponer(self.x,self.y)
            self.vx = 1

    def update(self):
        self.x += self.vx*ENGINE.p_per_meter*ENGINE.frame_time
        self.y += self.vy*ENGINE.p_per_meter*ENGINE.frame_time

        if self.sponer != None:
            self.sponer.x = self.x
            self.sponer.y = self.y
            self.sponer.update()

        pass


    def draw(self):
        self.image.draw(self.x,self.y)

        if self.sponer != None:
            self.sponer.draw()
            pass