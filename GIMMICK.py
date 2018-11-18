import ENGINE
import ZAKO

time = 0.0
sponer = ZAKO.Monster_sponer()

doing = []



def init():
    global time, doing
    time= 0
    #시간, 실행내용
    doing = [(4+(i*0.3),(ZAKO.STIRGE,0,600,ZAKO.RD)) for i in range(10)]+[
             (7+(i*0.3),(ZAKO.STIRGE,500,600,ZAKO.LD)) for i in range(10)]+[
             (10,(ZAKO.WRAITH,250,500,ZAKO.PATROL))]
    for i in range(10):
        doing.append((15+(i*0.3),(ZAKO.STIRGE,0,550,ZAKO.R)))
        doing.append((15+(i*0.3),(ZAKO.STIRGE,500,500,ZAKO.L)))
    doing += [(20,(ZAKO.FAIRY,100,600,ZAKO.D_400)),(20,(ZAKO.FAIRY,400,600,ZAKO.D_400))]


def run_stage():
    global time
    if len(doing) == 0:
        return


    if time > doing[0][0]:
        a,b,c,d = doing[0][1]
        sponer.add_monster(a,b,c,d)
        doing.remove(doing[0])



    time += ENGINE.frame_time
    pass