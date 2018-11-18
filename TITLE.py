from pico2d import *
import ENGINE
import AUDIO
import SELECT
import OPTION

select = 0
font = None

def start():
    AUDIO.play_music(0)
    pass


def end():
    pass


def handle():
    global select
    events = get_events()

    for event in events:
        if(event.type == SDL_KEYDOWN):
            if(event.key == SDLK_ESCAPE):
                ENGINE.run = False
            elif(event.key == SDLK_DOWN and select < 3):
                select +=1
            elif(event.key == SDLK_UP and select > 0):
                select -=1
            if(event.key == SDLK_SPACE or event.key == SDLK_z):
                if (select == 0):
                    ENGINE.Push_state(SELECT)
                elif (select == 2):
                    ENGINE.Push_state(OPTION)
                elif (select == 3):
                    ENGINE.run = False
    pass


def update():
    pass


def draw():
    clear_canvas()

    ENGINE.background[2].draw(400,300,800,600)

    ENGINE.bimage[1].draw(200,300 -50*select)

    ENGINE.font.draw(300, 300,'스타트', (255,255,255))
    ENGINE.font.draw(300, 250,'난이도', (255,255,255))
    ENGINE.font.draw(300, 200,'옵션', (255,255,255))
    ENGINE.font.draw(300, 150,'종료', (255,255,255))

    update_canvas()
    pass