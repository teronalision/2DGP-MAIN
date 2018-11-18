import ENGINE
from ZAKO import *



class Dolphin(Zako):

    def __init__(self):
        Zako.__init__(250,550)
        self.hp = 500
        self.size = 20
        self.speed = 0.8
        self.sponer = []
        self.drap = ITEM.LifeUp

    def draw(self):
        pass

    def kill():
        self.dead = True
        #ENGINE.del_obj()

        if(self.drap != None):
            ENGINE.add_obj(self.drap(self.x,self.y),3)

    def update(self):
        for sp in self.sponer:
            sp.update()

        set_moving(self.moving,self,self.speed)

        
        self.x += self.vx*ENGINE.p_per_meter*ENGINE.frame_time
        self.y += self.vy*ENGINE.p_per_meter*ENGINE.frame_time

        self.frame = (self.frame +frame_per_round*ENGINE.frame_time)%5
        self.time +=ENGINE.frame_time
        pass
