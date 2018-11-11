import ENGINE
import SPONER
import ITEM
from pico2d import *


class Zako:


    def __init__(self, x, y):
        self.x, self.y = x,y
        self.vx, self.vy = 0.1, -0.1
        self.hp = 0
        self.type = ENGINE.CIRCLE
        self.size = 20
        self.moving = None
        self.drap = None
        self.dead = False
        self.sponer = None
        self.cnt = 0

    def update(self):

        #
        if self.sponer != None:
                self.sponer.x = self.x
                self.sponer.y = self.y
                self.sponer.update()

        else:
            self.x += self.vx*ENGINE.p_per_meter*ENGINE.frame_time
            self.y += self.vy*ENGINE.p_per_meter*ENGINE.frame_time
        pass


    def draw(self):
        if self.dead == False:
            ENGINE.mimage[0].clip_draw(0,60,50,50,self.x,self.y,self.size*2,self.size*2)
        
        if(ENGINE.rect_mode):
            draw_rectangle(self.x -self.size, self.y -self.size, self.x +self.size, self.y +self.size)


    def attacked(self, damage):
        self.hp -= damage
        if(self.hp <=0):
            self.dead = True


    def kill(self):
        self.dead = True
        if(self.sponer != None):
            self.sponer.dead = True
        if(self.drap != None):
            self.drap(self.x,self.y)





#몬스터 스포너
FAIRY, JWRAITH, RUNE = range(3)
#체력, 크기, 탄스포너, 아이템
Monster_dic = {FAIRY:(1,20,0,None), JWRAITH:(20,20,-1,None), RUNE:(50,30,1,ITEM.PowerUp)}

class Monster_sponer:

    def __init__(self):
        pass

    def add_monster(self, name, x ,y):
        m = Zako(x,y)
        m.hp, m.size, sp, m.drap = Monster_dic[name]
        m.sponer = SPONER.Sponer(x,y,sp)


        ENGINE.add_obj(m,1)
        pass