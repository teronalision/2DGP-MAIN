from pico2d import *


def Quit():
    global run
    run = False

def Run(state):
    global run, state_stack
    run = True

    state_stack = [state]
    state.start()

    while run:
        state_stack[-1].handle()
        state_stack[-1].update()
        state_stack[-1].draw()


    while(len(state_stack)>0):
        state_stack[-1].end()
        state_stack.pop()


def Handle():
    es = get_events()

    for e in es:
        if (e.type, e.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
            Quit()
         


#초기화

run = True
state_stack = None


