from pico2d import *
import ENGINE
import TITLE
import AUDIO

select = 0

def start():
    pass


def end():
    pass


def handle():
    global select
    events = get_events()

    for event in events:
        if(event.type == SDL_KEYDOWN):
            if(event.key == SDLK_LEFT):
                AUDIO.volume = max(0, AUDIO.volume-5)
                AUDIO.set_volume()
            elif(event.key == SDLK_RIGHT):
                AUDIO.volume = min(100, AUDIO.volume+5)
                AUDIO.set_volume()
            elif(event.key == SDLK_SPACE or event.key == SDLK_z):
                pass
            elif(event.key == SDLK_ESCAPE):
                ENGINE.Pop_state()
    pass


def update():
    pass


def draw():
    clear_canvas()

    ENGINE.background[1].draw(400,300)

    ENGINE.bimage[1].draw(150,300 -50*select)

    ENGINE.font.draw(200, 300,'볼륨 :    %r'%AUDIO.volume, (255,255,255))

    update_canvas()
    pass
