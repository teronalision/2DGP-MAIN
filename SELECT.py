from pico2d import *
import ENGINE
import STAGE
import TITLE

select = 0
image = None

def start():
    global image
    image = load_image('dumy_b.png')


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
                ENGINE.Push_state(STAGE)
            elif(event.key == SDLK_ESCAPE):
                ENGINE.Change_state(TITLE)
    pass


def update():
    pass


def draw():
    clear_canvas()

    image.draw(150 +250*select, 200)

    ENGINE.font.draw(150, 250,'1번', (0,0,0))
    ENGINE.font.draw(400, 250,'2번', (0,0,0))

    update_canvas()
    pass