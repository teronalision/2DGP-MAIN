from pico2d import *
import ENGINE
import SELECT

select = 0
image = None
font = None

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
            if(event.key == SDLK_DOWN and select < 3):
                select +=1
            elif(event.key == SDLK_UP and select > 0):
                select -=1
            if(event.key == SDLK_SPACE and select == 0):
                ENGINE.Push_state(SELECT)
    pass


def update():
    pass


def draw():
    clear_canvas()

    image.draw(200,300 -50*select)

    ENGINE.font.draw(300, 300,'스타트', (0,0,0))
    ENGINE.font.draw(300, 250,'난이도', (0,0,0))
    ENGINE.font.draw(300, 200,'옵션', (0,0,0))
    ENGINE.font.draw(300, 150,'종료', (0,0,0))

    update_canvas()
    pass