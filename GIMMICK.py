import ENGINE
import ZAKO

time = 0
sponer = ZAKO.Monster_sponer()

#시간, 실행내용
doing = [(0,sponer.add_monster(ZAKO.JWRAITH,0,500,ZAKO.R)),
      (0,sponer.add_monster(ZAKO.STIRGE,500,500,ZAKO.L)),
      (2,sponer.add_monster(ZAKO.JWRAITH,0,500,ZAKO.R)),
      (2,sponer.add_monster(ZAKO.STIRGE,500,500,ZAKO.L)),
      (5,sponer.add_monster(ZAKO.WRAITH,250,500,ZAKO.PATROL))]


def init():
    global time
    time= 0


def run_stage():
    global time
    if len(doing) == 0:
        return


    if time > doing[0][0]:
        doing[0][1]
        doing.remove(doing[0])



    time += ENGINE.frame_time
    pass