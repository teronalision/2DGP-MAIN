import ENGINE
import ZAKO

time = 0.0
sponer = ZAKO.Monster_sponer()


doing = None
field_stage = []
boss_stage = []
boss = None
snext = False

def init():
    global time, field_stage, boss_stage,boss, boss_idx, doing
    time= 30
    boss_idx = 0
    #시간, 실행내용
    field_stage = [(4+(i*0.3),(ZAKO.STIRGE,0,600,ZAKO.RD)) for i in range(10)]+[
             (7+(i*0.3),(ZAKO.STIRGE,500,600,ZAKO.LD)) for i in range(10)]
    for i in range(10):
        field_stage.append((15+(i*0.3),(ZAKO.STIRGE,0,550,ZAKO.R)))
        field_stage.append((15+(i*0.3),(ZAKO.STIRGE,500,500,ZAKO.L)))
    field_stage += [(20,(ZAKO.FAIRY,100,600,ZAKO.D_400)),(20,(ZAKO.FAIRY,400,600,ZAKO.D_400))]


    #보스
    if(ENGINE.stage_num == 0):
        boss = sponer.add_monster(ZAKO.WRAITH, 250,600,None,False)
        boss_stage = [(63,ZAKO.HIFEL),
                      (70,ZAKO.HIFER)]


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
        summon_boss()
        snext = True

    else:
        doing += boss_stage
        time = 0  
    

    time += ENGINE.frame_time
    return False


def play_order(tuple):
    global boss
    if(len(tuple) == 4):
         a,b,c,d = tuple
         sponer.add_monster(a,b,c,d)

    else:
         boss.moving = tuple[1]

    pass

def summon_boss():
    if len(ENGINE.object_list[1])>0:
        ENGINE.object_list[1].clear

    ENGINE.add_obj(boss,1)