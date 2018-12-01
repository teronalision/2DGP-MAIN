from pico2d import *
import ENGINE
import TITLE

time = 0.0


def start():
    ENGINE.del_obj()
    ENGINE.del_obj(0)
    ENGINE.stage_num = 0
    pass


def end():
    pass


def handle():
    global select
    events = get_events()

    for e in events:
        if(e.type == SDL_QUIT):
            ENGINE.Quit()
        elif(e.type == SDL_KEYDOWN and time > 2):
            ENGINE.Change_state(TITLE)
    pass


def update():
    global time
    time += ENGINE.frame_time
    pass


def draw():
    clear_canvas()
    ENGINE.background[7].draw(400,300);
    ENGINE.font.draw(400 -60, 350,'게임 오버', (255,255,255))
    ENGINE.font.draw(400 -170, 200,'Press Any Button', (255,255,255))

    update_canvas()
    pass
