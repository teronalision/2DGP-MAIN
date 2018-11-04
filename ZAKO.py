import ENGINE
import SPONER
from pico2d import *


class zako:


    def __init__(self, x, y, f, image = None):
        self.x, self.y = x,y
        self.vx, self.vy = 0.0, 0.0
        self.form = f
        self.size = 50
        self.image = image
        self.dead = False
        self.sponer = None
        self.cnt = 0
        if f == 0:
            self.vx,self.vy = 1,-1
        elif f == 1:
            self.sponer = SPONER.Sponer(self.x,self.y)
            self.vx = 1

    def update(self):
        if self.sponer != None:
                self.sponer.x = self.x
                self.sponer.y = self.y
                self.sponer.update()


        if self.dead:
            if self.cnt > 100:#임시 값
                pass

            
            self.cnt += 1
            return


        else:
            self.x += self.vx*ENGINE.p_per_meter*ENGINE.frame_time
            self.y += self.vy*ENGINE.p_per_meter*ENGINE.frame_time
        pass


    def draw(self):
        if self.dead == False:
            self.image.draw(self.x,self.y)

        if self.sponer != None:
            self.sponer.draw()
            pass


    def kill(self):
        self.dead = True
        self.sponer.dead = True
