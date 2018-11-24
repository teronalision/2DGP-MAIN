import ENGINE
import ZAKO

time = 0.0
stage_num = 0
sponer = ZAKO.Monster_sponer()

doing = []

move_boss = []
boss = None

def init():
    global time, doing, move_boss
    time= 0
    #시간, 실행내용
    doing = [(4+(i*0.3),(ZAKO.STIRGE,0,600,ZAKO.RD)) for i in range(10)]+[
             (7+(i*0.3),(ZAKO.STIRGE,500,600,ZAKO.LD)) for i in range(10)]
    for i in range(10):
        doing.append((15+(i*0.3),(ZAKO.STIRGE,0,550,ZAKO.R)))
        doing.append((15+(i*0.3),(ZAKO.STIRGE,500,500,ZAKO.L)))
    doing += [(20,(ZAKO.FAIRY,100,600,ZAKO.D_400)),(20,(ZAKO.FAIRY,400,600,ZAKO.D_400))]


    #보스
    b1 = ZAKO.WRAITH
    b2
    b3
    boss = [b1,b2,b3]

    move_boss = [(63,ZAKO.HIFEL),
                 (70,ZAKO.HIFER)]


def run_stage():
    global time, doing, move_boss

    if time <60:
        if time > doing[0][0]:
            a,b,c,d = doing[0][1]
            sponer.add_monster(a,b,c,d)
            doing.remove(doing[0])

    elif(time > boss[0][0]):
        boss[stage_num].moving = move_boss[0][1]
        move_boss.remove(move_boss[0])



        if(len(ENGINE.object_list[1]) == 0):
            return True

    



    time += ENGINE.frame_time
    return False