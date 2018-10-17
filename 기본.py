from pico2d import *
import ENGINE
import HERO
import BULLET

image = None
b = [BULLET.bullet(400,500,1), BULLET.bullet(300,500,1), BULLET.bullet(500,500,1)]
bimage = None
time = 0

def start():
    global image, bimage
    image = load_image('test.png')
    HERO.x,HERO.y = 400, 300
    bimage = [load_image('dumy_b.png'), load_image('dumy_c.png')]



def end():
    global image
    del(image)


def handle():
    events = get_events()

    for e in events:
        if(e.type == SDL_QUIT):
            ENGINE.Quit()
        elif(e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE):
            ENGINE.Quit()
    


def update():
    global time

    #캐릭터 이동
    HERO.update()

    for obj in b:
        #탄 이동
        obj.update()

        #충돌판정
        if (HERO.x - obj.x)**2 + (HERO.y - obj.y)**2 < 60**2:
            HERO.live = False
    

    if time>10:
        b[0].order(0,-1)
    if time>20:
        b[1].order(1,-1)
    if time>30:
        b[2].order(-1,-1)

    time +=1


def draw():
    clear_canvas()

    image.draw(HERO.x,HERO.y,80,120)
    for i in b:
        bimage[i.image].draw(i.x,i.y);

    update_canvas()