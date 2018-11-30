import ENGINE
import ZAKO
import DECO
import random

time = 0.0
sponer = ZAKO.Monster_sponer()


doing = None
field_stage = []
boss_stage = []
boss = None
snext = False

def init():
    global time, field_stage, boss_stage,boss, doing, snext
    time= 0
    snext = False
    #시간, 실행내용
    if(ENGINE.stage_num == 0):
        field_stage = [(4+(i*0.3),(ZAKO.STIRGE,0,600,ZAKO.RD)) for i in range(10)]+[
                       (7+(i*0.3),(ZAKO.STIRGE,500,600,ZAKO.LD)) for i in range(10)]
        for i in range(10):
            field_stage.append((15+(i*0.3),(ZAKO.STIRGE,0,550,ZAKO.R)))
            field_stage.append((15+(i*0.3),(ZAKO.STIRGE,500,500,ZAKO.L)))
        field_stage += [(20,(ZAKO.FAIRY,100,600,ZAKO.D_400)),(23,(ZAKO.FAIRY,400,600,ZAKO.D_400))]+[
                        (39+(i*0.1),(ZAKO.STIRGE,random.randint(-200,400),600,ZAKO.RD)) for i in range(30)]+[
                        (44+(i*0.1),(ZAKO.STIRGE,random.randint(200,700),600,ZAKO.LD)) for i in range(30)]+[
                        (50,(ZAKO.FAIRY,100,600,ZAKO.D_400)),(50,(ZAKO.FAIRY,400,600,ZAKO.D_400)),
                        (56,(DECO.Deco(ENGINE.bimage[6],10,500,150,50),None)),(60,None)]

    elif(ENGINE.stage_num == 1):
        field_stage = [(4+(i*0.3),(ZAKO.STIRGE,0,600,ZAKO.RD)) for i in range(10)]+[
                       (46,(DECO.Deco(ENGINE.bimage[6],10,500,150,50),None)),(52,None)]
        pass
        

    #보스
    if(ENGINE.stage_num == 0):
        boss = sponer.add_monster(ZAKO.WRAITH, 250,600,None,False)
        boss_stage = [(0,ZAKO.HIFEL),
                      (5,ZAKO.HIFER),(5,(ZAKO.WING,100,400,None)),
                      (10,(ZAKO.WING,400,400,None))]
    elif(ENGINE.stage_num == 1):
        boss = sponer.add_monster(ZAKO.D_WRAITH, 250,600,None,False)
        boss_stage = [(0,ZAKO.D_400)]+[
                      (5+(i/2),(ZAKO.JWRAITH,150,400,ZAKO.SPINE)) for i in range(6)]+[
                      (60,None)]
        pass
    else:
        pass

    #
    doing = field_stage


def run_stage():
    global doing, time, field_stage, boss_stage, boss, snext


    if(boss.hp <= 0):
        return True



    if len(doing) != 0:
        if time > doing[0][0]:
            play_order(doing[0][1])
            doing.remove(doing[0])

    elif(snext == False):
        ENGINE.del_obj(1)
        summon_boss()
        snext = True

    else:
        doing += boss_stage
        time = 0  
    

    time += ENGINE.frame_time
    return False


def play_order(t):
    global boss
    if t == None:
        return

    if type(t) == tuple:
        if len(t) == 4:
            a,b,c,d = t
            sponer.add_monster(a,b,c,d)
        elif len(t) == 2:
            dec = t[0]
            dec.timer =0
            ENGINE.add_obj(dec,4)
   
    else:
        boss.moving = t


def summon_boss():
    if len(ENGINE.object_list[1])>0:
        ENGINE.object_list[1].clear

    ENGINE.add_obj(boss,1)