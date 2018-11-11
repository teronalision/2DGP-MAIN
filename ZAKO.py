import ENGINE
import SPONER
import ITEM
from pico2d import *


class Zako:


    def __init__(self, x, y, f):
        self.x, self.y = x,y
        self.vx, self.vy = 0.0, 0.0
        self.hp = 1
        self.type = ENGINE.CIRCLE
        self.size = 20
        self.form = f
        self.dead = False
        self.sponer = None
        self.cnt = 0
        if f == 0:
            self.sponer = SPONER.Sponer(self.x,self.y,0)
        elif f == 1:
            self.sponer = SPONER.Sponer(self.x,self.y,1)

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

    def attacked(self, damage):
        self.hp -= damage
        if(self.hp <=0):
            self.dead = True


    def kill_zako(self):
        self.dead = True
        if(self.sponer != None):
            self.sponer.dead = True



class fairy(Zako):

    def __init__(self,x,y,version):
        Zako.__init__(self,x,y,0)
        self.version = version
        self.hp = 5
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
        
        if(ENGINE.rect_mode):
            draw_rectangle(self.x -self.size, self.y -self.size, self.x +self.size, self.y +self.size)


    def kill(self):
        ENGINE.add_obj(ITEM.PowerUp(self.x, self.y),3)

        self.kill_zako()


class rune(Zako):

    def __init__(self,x,y,version):
        Zako.__init__(self,x,y,1)
        self.version = version
        self.vy = -0.3
        self.size = 30
        self.hp = 50
        self.timer = 0.0

    def update(self):
        #
        if(self.version == 1):
            pass
        
        if(self.y < 400):
            self.vy = 0
        
        self.update_zako()
        self.timer += ENGINE.frame_time


    def draw(self):
        if self.dead == False:
            ENGINE.bimage[3].clip_draw(0,16,64,64,self.x,self.y,self.size*2,self.size*2)
        
        if(ENGINE.rect_mode):
            draw_rectangle(self.x -self.size, self.y -self.size, self.x +self.size, self.y +self.size)


    def kill(self):
        ENGINE.add_obj(ITEM.PowerUp(self.x, self.y),3)

        self.kill_zako()


class j_wraith(Zako):

    def __init__(self,x,y,ver):
        Zako.__init__(self,x,y,-1)
        self.version = ver
        self.size = 20
        self.hp = 2



    def update(self):


        self.update_zako()


    def draw(self):
        if self.dead == False:
            ENGINE.mimage[0].clip_draw(0,60,50,50,self.x,self.y,self.size*2,self.size*2)
        
        if(ENGINE.rect_mode):
            draw_rectangle(self.x -self.size, self.y -self.size, self.x +self.size, self.y +self.size)


    def kill(self):
        
        self.kill_zako()