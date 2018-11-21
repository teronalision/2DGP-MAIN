import ENGINE
import ZAKO

time = 0.0
sponer = ZAKO.Monster_sponer()

doing = []

boss = []

def init():
    global time, doing, boss
    time= 0
    #시간, 실행내용
    doing = [(4+(i*0.3),(ZAKO.STIRGE,0,600,ZAKO.RD)) for i in range(10)]+[
             (7+(i*0.3),(ZAKO.STIRGE,500,600,ZAKO.LD)) for i in range(10)]
    for i in range(10):
        doing.append((15+(i*0.3),(ZAKO.STIRGE,0,550,ZAKO.R)))
        doing.append((15+(i*0.3),(ZAKO.STIRGE,500,500,ZAKO.L)))
    doing += [(20,(ZAKO.FAIRY,100,600,ZAKO.D_400)),(20,(ZAKO.FAIRY,400,600,ZAKO.D_400)),
              (30,(ZAKO.WRAITH,250,600,ZAKO.D_400))]


    #보스
    boss = [(35,ZAKO.HIFEL),
            (40,ZAKO.HIFER)]


def run_stage():
    global time, doing
    if len(doing) == 0:
        if(time > boss[0][0]):
            ENGINE.object_list[1][0].moving = boss[0][1]
            boss.pop



        if(len(ENGINE.object_list[1]) == 0):
            return True

    elif time > doing[0][0]:
        a,b,c,d = doing[0][1]
        sponer.add_monster(a,b,c,d)
        doing.remove(doing[0])



    time += ENGINE.frame_time
    return False