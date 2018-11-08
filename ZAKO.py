import ENGINE
import SPONER
from pico2d import *


class zako:


    def __init__(self, x, y, f):
        self.x, self.y = x,y
        self.vx, self.vy = 0.0, 0.0
        self.form = f
        self.size = 20
        self.dead = False
        self.sponer = None
        self.cnt = 0
        if f == 0:
            self.size = 15
        elif f == 1:
            self.sponer = SPONER.Sponer(self.x,self.y)
            self.vy = -1

    def update_zako(self):

        #
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


    def kill(self):
        self.dead = True
        self.sponer.dead = True



class fairy(zako):

    def __init__(self,x,y,version):
        zako.__init__(self,x,y,1)
        self.version = version
        self.timer = 0.0

    def update(self):
        #
        if(self.version == 1):
            if(self.timer == 0):
                self.vx = 1
                self.vy = -0.3


        elif(self.version == 2):
            if(self.timer == 0):
                self.vx = -1
                self.vy = -0.3


                
        
        self.update_zako()
        self.timer += ENGINE.frame_time


    def draw(self):
        if self.dead == False:
            ENGINE.bimage[1].draw(self.x,self.y,50,50)
