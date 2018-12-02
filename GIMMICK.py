import ENGINE
import ZAKO
import DECO
import random
import json

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
        field_stage = load('Data\\1stage.txt')

    elif(ENGINE.stage_num == 1):
        field_stage = load('Data\\2stage.txt')
        
    else:
        field_stage = load('Data\\3stage.txt')
        
        

    #보스
    if(ENGINE.stage_num == 0):
        boss = sponer.add_monster(ZAKO.WRAITH, 250,600,None,False)
        boss_stage = load('Data\\1boss_stage.txt')
    elif(ENGINE.stage_num == 1):
        boss = sponer.add_monster(ZAKO.D_WRAITH, 250,600,None,False)
        boss_stage = load('Data\\2boss_stage.txt')
    else:
        boss = sponer.add_monster(ZAKO.WITCH,300,550,None,False)
        boss_stage = load('Data\\3boss_stage.txt')

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

    if type(t) == list or type(t) == tuple:
        if len(t) == 4:
            a,b,c,d = t
            sponer.add_monster(a,b,c,d)
        elif len(t) == 2:
            dec = DECO.Deco(ENGINE.bimage[6],10,500,150,50)
            dec.timer =0
            ENGINE.add_obj(dec,4)
   
    else:
        boss.moving = t


def summon_boss():
    if len(ENGINE.object_list[1])>0:
        ENGINE.object_list[1].clear

    ENGINE.add_obj(boss,1)


def save(file,data):
    with open(file, 'w') as f:
        s = json.dumps(data)
        json.dump(s,f)

def load(file):
    with open(file, 'r') as f:
        s = json.load(f)
        o = json.loads(s)
        return o
