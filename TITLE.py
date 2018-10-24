from ENGINE import *
import STAGE

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
            if(event.key == SDLK_DOWN and select < 3):
                select +=1
            elif(event.key == SDLK_UP and select > 0):
                select -=1
            if(event.key == SDLK_SPACE and select == 0):
                Push_state(STAGE)
    pass


def update():
    pass


def draw():
    clear_canvas()



    update_canvas()
    pass