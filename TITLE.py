from pico2d import *
import ENGINE
import SELECT

select = 0
font = None

def start():
    pass


def end():
    pass


def handle():
    global select
    events = get_events()

    for event in events:
        if(event.type == SDL_KEYDOWN):
            if(event.key == SDLK_DOWN and select < 3):
                select +=1
            elif(event.key == SDLK_UP and select > 0):
                select -=1
            if(event.key == SDLK_SPACE or event.key == SDLK_z):
                if (select == 0):
                    ENGINE.Push_state(SELECT)
                elif (select == 3):
                    ENGINE.run = False
    pass


def update():
    pass


def draw():
    clear_canvas()

    ENGINE.background[0].draw(400,300,800,600)

    ENGINE.bimage[1].draw(200,300 -50*select)

    ENGINE.font.draw(300, 300,'스타트', (0,0,0))
    ENGINE.font.draw(300, 250,'난이도', (0,0,0))
    ENGINE.font.draw(300, 200,'옵션', (0,0,0))
    ENGINE.font.draw(300, 150,'종료', (0,0,0))

    update_canvas()
    pass