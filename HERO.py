from pico2d import *



x, y = 0, 0
w, h = 0, 0
key_down = [False,False,False,False] # 왼쪽 오른쪽 위 아래
speed = 0.7
live = True

image = None
frame = 0

def start():
    global image
    image = load_image('C1.png')

def update():
    global x,y,frame

    if live == False:
        #return
        pass

    frame = (frame+1) %(8*30)

    if x +w*speed +40 < 500 and x +w*speed -40 > 0:
        x += w*speed
    if y +h*speed +60 < 600 and y +h*speed -60 > 0:
        y += h*speed

def handle(type, key):
    global w,h
    global key_down

    if type == SDL_KEYDOWN:
        if key == SDLK_LEFT:
            key_down[0] = True
        elif key == SDLK_RIGHT:
            key_down[1] = True
        if key == SDLK_UP:
            key_down[2] = True
        elif key == SDLK_DOWN:
            key_down[3] = True
    elif type == SDL_KEYUP:
        if key == SDLK_LEFT:
            key_down[0] = False
        elif key == SDLK_RIGHT:
            key_down[1] = False
        if key == SDLK_UP:
            key_down[2] = False
        elif key == SDLK_DOWN:
            key_down[3] = False

    if key_down[0] and key_down[1] == False:
        w = -1
    elif key_down[1] and key_down[0] == False:
        w = 1
    else:
        w = 0

    if key_down[2] and key_down[3] == False:
        h = 1
    elif key_down[3] and key_down[2] == False:
        h = -1
    else:
        h = 0


def draw():
    if w == 0:
        image.clip_draw(32*(frame//30),0+48*2,32,48,x,y)
    if w == -1:
        image.clip_draw(32*(frame//30),0+48*1,32,48,x,y)
    if w == 1:
        image.clip_draw(32*(frame//30),0+48*0,32,48,x,y)

