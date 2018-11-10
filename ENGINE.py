from pico2d import *
import time



#초기화
p_per_meter = 100
frame_time = 0.0


run = True
state_stack = []

#디버그 모드
rect_mode = True
undead = False

#이미지
hero_image, bimage, simage = None, None, None
background = None
bgm = None
font = None


def init():
    global hero_image,bimage,simage,background,bgm,font

    hero_image = [load_image('Image\C1.png')]
    bimage = [load_image('Image\dumy_b.png'), load_image('Image\dumy_c.png'),
              load_image('Image\etama6.png'), load_image('Image\etama2.png')]
    simage = [load_image('Image\\bg1.png')]
    background = [load_image('Image\sky0.png'),load_image('Image\sky1.jpg'),load_image('Image\sky2.jpg')]

    bgm
    font = load_font('Image\Maplestory Bold.TTF')



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

def Pop_state():
    global state_stack

    state.end()
    state_stack.remove(-1)

def Change_state(state):
    global state_stack

    state.start()
    state_stack[-1].end()
    state_stack.pop()
    state_stack.append(state)




#물체들
object_list = [[],[],[],[]]   #0아군 1적 2총알 3아이템


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
    if(A.size == 0 or B.size == 0):
        return False

    if (A.x - B.x)**2 + (A.y - B.y)**2 < (B.size +A.size)**2:
        return True
    else:
        return False