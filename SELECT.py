from pico2d import *
import ENGINE
import AUDIO
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
            if(event.key == SDLK_RIGHT):
                select = (select+1) %2
                AUDIO.play_se(0)
            elif(event.key == SDLK_LEFT):
                select = (select+1) %2
                AUDIO.play_se(0)
            elif(event.key == SDLK_SPACE or event.key == SDLK_z):
                HERO.hero_select = select
                ENGINE.Change_state(STAGE)
            elif(event.key == SDLK_ESCAPE):
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