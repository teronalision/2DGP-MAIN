import ENGINE
import SPONER
import ITEM
from pico2d import *

frame_per_round = 5

#이동
U, D, L, R, LU, LD, RU, RD ,PATROL,D_400,HIFEL,HIFER, SPINE = range(13)
Moving_dic = {None:(0,0),U:(0,1), D:(0,-1), L:(-1,0), R:(1,0), LU:(-1,1), LD:(-1,-1), RU:(1,1), RD:(1,-1),
              PATROL:(0,0),D_400:(0,-1),HIFEL:(-1,0),HIFER:(1,0),SPINE:(0,0)}

#몬스터
FAIRY, JWRAITH, WRAITH, STIRGE, RUNE, D_WRAITH, WING = range(7)
#그리기
drawing_dic = {FAIRY:(4,4,64,64), JWRAITH:(0,5,50,50), WRAITH:(1,5,75,70), STIRGE:(2,2,46,46), D_WRAITH:(3,5,75,70), WING:(0,5,50,50)}

def set_moving(obj):
    order = obj.moving
    speed = obj.speed

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

    elif(order == SPINE):
        obj.x, obj.y = 250 +150*math.sin(math.radians(obj.time*120)), 400 +100*math.cos(math.radians(obj.time*120))

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
        self.name = None
        self.size = 20
        self.point = 5
        self.moving = None
        self.speed = 1
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

        set_moving(self)

        
        self.x += self.vx*ENGINE.p_per_meter*ENGINE.frame_time
        self.y += self.vy*ENGINE.p_per_meter*ENGINE.frame_time

        self.frame = (self.frame +frame_per_round*ENGINE.frame_time)%5
        self.time +=ENGINE.frame_time
        pass


    def draw(self):
        if self.dead == False:
            num, f, x, y =drawing_dic[self.name]
            d = ''
            if(self.vx >0):
                d+='h'
            ENGINE.mimage[num].clip_composite_draw(int(self.frame%f)*x,0,x,y,0,d,self.x,self.y,self.size*2,self.size*2)
        
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



#체력, 크기,속도, 탄스포너, 아이템
Monster_dic = {FAIRY:(50,20,1,1,None), JWRAITH:(50,20,2,0,None),
               WRAITH:(500,70,1,2,ITEM.LifeUp), STIRGE:(1,20,2,0,None),
               RUNE:(50,30,1,2,ITEM.PowerUp), D_WRAITH:(1000,70,1,3,ITEM.LifeUp),
               WING:(30,20,0,4,ITEM.PowerUp)}

class Monster_sponer:

    def __init__(self):
        pass

    def add_monster(self, name, x ,y, order, auto = True):
        m = Zako(x,y)
        m.name = name
        m.hp, m.size,m.speed, sp, m.drap = Monster_dic[name]
        m.sponer = SPONER.Sponer(x,y,sp)
        m.moving = order
        m.frame = ENGINE.randint(0,4)

        if(auto):
            ENGINE.add_obj(m,1)
        else:
            return m