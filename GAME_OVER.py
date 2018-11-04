from pico2d import *
import ENGINE
import TITLE

time = 0.0


def start():
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

    ENGINE.font.draw(400 -30, 350,'게임 오버', (0,0,0))
    ENGINE.font.draw(400 -100, 200,'Press Any Button', (0,0,0))

    update_canvas()
    pass
