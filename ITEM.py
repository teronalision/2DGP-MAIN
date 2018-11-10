from pico2d import *
import ENGINE
import HERO



class Item:

    def __init__(self,x,y):
        self.x, self.y = x, y
        self.size = 10
        self.v = 1.0
        self.image = 0
        self.dead = False


    def update(self):
        self.y += self.v * ENGINE.frame_time *ENGINE.p_per_meter

        self.v = max(self.v-(1*ENGINE.frame_time) , -1)
        pass


    def draw(self):
        if(ENGINE.rect_mode):
            draw_rectangle(self.x -self.size, self.y -self.size, self.x +self.size, self.y +self.size)
        ENGINE.bimage[3].clip_draw(16*self.image,256-(16*5),16,16,self.x,self.y,self.size*2,self.size*2)
        pass



class PowerUp(Item):

    def __init__(self, x, y):
        Item.__init__(self,x, y)
        self.image = 2


    def effect(self, hero):
        hero.power = min(hero.power+1, 10)
        self.dead = True