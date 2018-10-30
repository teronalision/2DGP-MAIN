#from pico2d import *
import time

p_per_meter = 100

frame_time = 0.0

def Quit():
    global run
    run = False

def Run():
    global run, state_stack, frame_time
    run = True
    c_time = time.time()

    while run:
        state_stack[-1].handle()
        state_stack[-1].update()
        state_stack[-1].draw()

        frame_time = time.time() - c_time
        #frame_rate = 1.0 /frame_time
        c_time += frame_time
        

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


#물체들
object_list = []


def add_obj(obj, i):
    object_list.append(obj)

def del_obj(obj):
    object_list.remove(obj)
    del(obj)


def yield_obj():
    for o in object_list:
        yield o