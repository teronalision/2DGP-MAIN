from pico2d import *


def Quit():
    global run
    run = False

def Run():
    global run, state_stack
    run = True

    while run:
        state_stack[-1].handle()
        state_stack[-1].update()
        state_stack[-1].draw()


    while(len(state_stack)>0):
        state_stack[-1].end()
        state_stack.pop()


def Push_state(state):
    global state_stack
    
    state.start()
    state_stack.append(state)


def Change_state(state):
    global state_stack

    state.start()
    state_stack[-1].end()
    state_stack.remove(-1)
    state_stack.append(state)


#초기화

run = True
state_stack = []


