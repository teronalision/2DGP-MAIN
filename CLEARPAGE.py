from pico2d import *
import ENGINE
import STAGE
import TITLE

time = 0.0


def start():
    ENGINE.stage_num+= 1
    pass


def end():
    if ENGINE.stage_num == 3:
        ENGINE.stage_num = 0
    pass


def handle():
    global select
    events = get_events()

    for e in events:
        if(e.type == SDL_QUIT):
            ENGINE.Quit()
        elif(e.type == SDL_KEYDOWN and time > 3):
            if ENGINE.stage_num <3:
                ENGINE.Change_state(STAGE)
            else:
                ENGINE.Change_state(TITLE)
    pass


def update():
    global time
    time += ENGINE.frame_time
    pass


def draw():
    clear_canvas()

    if( ENGINE.stage_num <3):
        ENGINE.background[7].draw(400,300);
        ENGINE.font.draw(400 -150, 350,'스테이지 클리어 ! !', (255,255,255))
        if time > 3:
            ENGINE.font.draw(400 -170, 200,'Press Any Button', (255,255,255))


    else:
        ENGINE.background[8].draw(400,300);
        ENGINE.font.draw(300, 350,'! ! YOU WIN ! !', (255,255,255))

    update_canvas()
    pass
