import ENGINE
import SPONER
import ITEM
from pico2d import *

frame_per_round = 5

U, D, L, R, LU, LD, RU, RD ,PATROL,D_400,HIFEL,HIFER = range(12)
Moving_dic = {U:(0,1), D:(0,-1), L:(-1,0), R:(1,0), LU:(-1,1), LD:(-1,-1), RU:(1,1), RD:(1,-1) ,PATROL:(0,0),D_400:(0,-1),HIFEL:(-1,0),HIFER:(1,0)}

def set_moving(order, obj, speed):
    if(order == PATROL):
        if(obj.x>450 or obj.vx==0):
            obj.vx = -1
        elif(obj.x<50):
            obj.vx = 1

    elif(order == HIFEL):
        if(math.fabs(obj.x-100) > 1 or math.fabs(obj.y- 400) > 1):
            r =math.atan2(400-obj.y,100-obj.x)
            obj.vx, obj.vy = math.cos(r), math.sin(r)
        else:
            obj.vx = obj.vy = 0
    elif(order == HIFER):
        if(math.fabs(obj.x-400) > 1 or math.fabs(obj.y- 400) > 1):
            r =math.atan2(400-obj.y,400-obj.x)
            obj.vx, obj.vy = math.cos(r), math.sin(r)
        else:
            obj.vx = obj.vy = 0

    elif(order == D_400 and obj.y <= 400):
        obj.vy = 0

    elif(order != None):
        obj.vx, obj.vy = Moving_dic[order]
    obj.vx *=speed
    obj.vy *=speed


class Zako:


    def __init__(self, x, y):
        self.x, self.y = x,y
        self.vx, self.vy = 0.0, 0.0
        self.hp = 0
        self.type = ENGINE.CIRCLE
        self.size = 20
        self.point = 5
        self.moving = None
        self.speed = 1
        self.draw_m = None
        self.drap = None
        self.dead = False
        self.sponer = None

        self.frame = 0
        self.time = 0.0

    def update(self):

        #
        if self.sponer != None:
                self.sponer.x = self.x
                self.sponer.y = self.y
                self.sponer.update()

        set_moving(self.moving,self,self.speed)

        
        self.x += self.vx*ENGINE.p_per_meter*ENGINE.frame_time
        self.y += self.vy*ENGINE.p_per_meter*ENGINE.frame_time

        self.frame = (self.frame +frame_per_round*ENGINE.frame_time)%5
        self.time +=ENGINE.frame_time
        pass


    def draw(self):
        if self.dead == False and self.draw_m != None:
           self.draw_m(self)
        
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
            ENGINE.add_obj(self.drap(self.x,self.y),3)



#몬스터 드로우
def draw_jwraith(mob):
    d = ''
    if(mob.vx >0):
        d+='h'
    ENGINE.mimage[0].clip_composite_draw(int(mob.frame)*50,60,50,50,0,d,mob.x,mob.y,mob.size*2,mob.size*2)
def draw_wraith(mob):
    d = ''
    if(mob.vx >0):
        d+='h'
    ENGINE.mimage[1].clip_composite_draw(int(mob.frame)*75,0,75,70,0,d,mob.x,mob.y,mob.size*2,mob.size*2)
def draw_stirge(mob):
    d = ''
    if(mob.vx >0):
        d+='h'
    ENGINE.mimage[2].clip_composite_draw(int(mob.frame%2)*46,0,46,46,0,d,mob.x,mob.y,mob.size*2,mob.size*2)


#몬스터 스포너
FAIRY, JWRAITH, WRAITH, STIRGE, RUNE = range(5)
#체력, 크기,속도, 탄스포너, 아이템, 그리기
Monster_dic = {FAIRY:(50,20,1,1,None,draw_jwraith), JWRAITH:(1,20,2,0,None,draw_jwraith),
               WRAITH:(100,70,1,2,ITEM.LifeUp,draw_wraith), STIRGE:(1,20,2,0,None,draw_stirge),
               RUNE:(50,30,1,2,ITEM.PowerUp,draw_wraith)}

class Monster_sponer:

    def __init__(self):
        pass

    def add_monster(self, name, x ,y, order, auto = True):
        m = Zako(x,y)
        m.hp, m.size,m.speed, sp, m.drap, m.draw_m = Monster_dic[name]
        m.sponer = SPONER.Sponer(x,y,sp)
        m.moving = order
        m.frame = ENGINE.randint(0,4)

        if(auto):
            ENGINE.add_obj(m,1)
        else:
            return m