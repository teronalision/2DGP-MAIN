from pico2d import *
import time



#초기화
p_per_meter = 100
frame_time = 0.0


run = True
state_stack = []

himage, bimage, simage = None, None, None
font = None

def init():
    global himage,bimage,simage,font

    himage = load_image('C1.png')
    bimage = [load_image('dumy_b.png'), load_image('dumy_c.png'), load_image('91834.png')]
    simage = [load_image('bg1.png')]
    font = load_font('Maplestory Bold.TTF')


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
    state_stack.pop()
    state_stack.append(state)




#물체들
object_list = [[],[]]   #0아군 1적


def add_obj(obj, i):
    object_list[i].append(obj)

def del_obj():
    global object_list

    for i in range(len(object_list)):
        object_list[i].clear()
            
            
            


def yield_obj(i):
    for o in object_list[i]:
        yield o

def all_obj():
    for i in range(len(object_list)):
        for o in object_list[i]:
            yield o


def is_crash(A, B):
     if (A.x - B.x)**2 + (A.y - B.y)**2 < (B.size +10)**2:
         return True
     else:
         return False