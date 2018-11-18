from pico2d import *
import ENGINE
import STAGE
import TITLE
import HERO

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
            if(event.key == SDLK_RIGHT and select < 1):
                select +=1
            elif(event.key == SDLK_LEFT and select > 0):
                select -=1
            elif(event.key == SDLK_SPACE or event.key == SDLK_z and select == 0):
                HERO.hero_select = 0
                ENGINE.Change_state(STAGE)
            elif(event.key == SDLK_ESCAPE):
                HERO.hero_select = 1
                ENGINE.Pop_state()
    pass


def update():
    pass


def draw():
    clear_canvas()
    ENGINE.background[5].draw(400,300,800,600)

    ENGINE.bimage[1].draw(150 +250*select, 200)

    ENGINE.font.draw(150, 250,'1번', (255,255,255))
    ENGINE.font.draw(400, 250,'2번', (255,255,255))

    update_canvas()
    pass