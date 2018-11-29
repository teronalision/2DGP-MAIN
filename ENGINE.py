from pico2d import *
from random import *
import time
import AUDIO


#초기화
p_per_meter = 100
frame_time = 0.0


run = True
state_stack = []
stage_num = 0

#디버그 모드
rect_mode = False
undead = True

#이미지
hero_image, bimage, mimage = None, None, None
background = None
bgm = None
font = None


def init():
    global hero_image,bimage,simage,mimage,background,bgm,font

    hero_image = [load_image('Image\C1.png'),load_image('Image\\C2.png')]
    bimage = [load_image('Image\dumy_b.png'), load_image('Image\dumy_c.png'),
              load_image('Image\etama6.png'), load_image('Image\etama2.png'),
              load_image('Image\etama.png'), load_image('Image\\UI.png')]
    mimage = [load_image('Image\\jr_wraith.png'),load_image('Image\\wraith.png'),load_image('Image\\stirge.png'),load_image('Image\\d_wraith.png')]
    background = [load_image('Image\\bg1.png'),load_image('Image\\bg2.png'),load_image('Image\\sky0.png'),
                  load_image('Image\\sky1.jpg'),load_image('Image\\sky2.jpg'),load_image('Image\\bg3.png'),
                  load_image('Image\\cloud.png'),load_image('Image\\clear0.jpg'),load_image('Image\\clear1.jpg')]

    AUDIO.init()
    font = load_font('Image\Maplestory Bold.TTF',40)



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

    state_stack[-1].end()
    state_stack.pop()

def Change_state(state):
    global state_stack

    state.start()
    state_stack[-1].end()
    state_stack.pop()
    state_stack.append(state)




#물체들
object_list = [[],[],[],[],[]]   #0아군 1적 2총알 3아이템 4장식


def add_obj(obj, i):
    object_list[i].append(obj)

def del_obj(num = -1):
    global object_list

    if(num == -1):
        for i in range(1,len(object_list)):
            object_list[i].clear()
       
    else:
        object_list[num].clear()

def yield_obj(i):
    for o in object_list[i]:
        yield o

def all_obj():
    for i in range(len(object_list)):
        for o in object_list[i]:
            yield o



#충돌박스
CIRCLE, SQUARE, RECT = range(3)

def is_circle_crash(A,B):
    x , y = A.x - B.x, A.y - B.y
    if(x**2 + y**2 < (B.size +A.size)**2):
        return True
    else:
        return False
def crash_p2c(C,p):
    x , y = C.x - p[0], C.y - p[1]
    if(x**2 + y**2 < C.size**2):
        return True
    else:
        return False

def is_crash(A, B):
    if(A.type == None or B.type == None):
        return False

    


    if (A.type == CIRCLE and B.type == CIRCLE):
        if is_circle_crash(A,B):
            return True
    elif (A.type == CIRCLE and B.type == SQUARE):
        p1,p2,p3,p4 = (B.x-B.size,B.y-B.size),(B.x+B.size,B.y-B.size),(B.x-B.size,B.y+B.size),(B.x+B.size,B.y+B.size)
        if crash_p2c(A,p1) or crash_p2c(A,p2) or crash_p2c(A,p3) or crash_p2c(A,p4):
            return True
    elif (A.type == CIRCLE and B.type == RECT):
        dx, dy = B.size*(math.sin(B.r))/2, B.size*(math.cos(B.r))
        p1,p2,p3,p4 = (B.x -dx,B.y -dy), (B.x +dx,B.y -dy), (B.x -dx,B.y +dy), (B.x +dx,B.y +dy)
        if crash_p2c(A,p1) or crash_p2c(A,p2) or crash_p2c(A,p3) or crash_p2c(A,p4):
            return True


    else:
        return False

