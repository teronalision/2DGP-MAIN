import ENGINE
import ZAKO

time = 0.0
sponer = ZAKO.Monster_sponer()


doing = None
field_stage = []
boss_stage = []
boss = None
boss_idx = 0

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
    global time, field_stage, boss_stage, boss,boss_idx


    if len(field_stage) != 0:
        if time > field_stage[0][0]:
            a,b,c,d = field_stage[0][1]
            sponer.add_monster(a,b,c,d)
            field_stage.remove(field_stage[0])
    elif(int(time) == 60):
        if len(ENGINE.object_list[1])>0:
            ENGINE.object_list[1].clear

        ENGINE.add_obj(boss,1)
        time = 61

    elif(boss.hp >0):
        if(time > boss_stage[boss_idx][0]):
            boss.moving = boss_stage[boss_idx][1]
        
        #끝나면 다시 처음부터
        if(len(boss_stage) <= boss_idx):
            boss_idx = 0
            time = 61



    
    else:
        return True

    time += ENGINE.frame_time
    return False


def play_order(tuple):
    if(len(tuple) == 4):
         a,b,c,d = tuple
         sponer.add_monster(a,b,c,d)

    else:
         boss.moving = boss_stage[boss_idx][1]

    pass