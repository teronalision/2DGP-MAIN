from pico2d import *
import ENGINE
import HERO
import BULLET
import SPONER

image = None
b = []
sp = SPONER.Sponer(200,500)
bimage = None
simage = None
time = 0

def start():
    global image, bimage, simage
    image = load_image('test.png')
    HERO.x,HERO.y = 250, 100
    bimage = [load_image('dumy_b.png'), load_image('dumy_c.png')]
    simage = [load_image('bg1.png')]



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

        HERO.handle(e.type, e.key)


        

    


def update():
    global time

    #캐릭터 이동
    HERO.update()

    #생성
    sp.update(b)

    for obj in b:
        #탄 이동
        obj.update()

        #충돌판정
        if (HERO.x - obj.x)**2 + (HERO.y - obj.y)**2 < 60**2:
            HERO.live = False
    

    if time>10:
        b[0].order(0,-0.2)
    if time>20:
        b[1].order(0.2,-0.2)
    if time>30:
        b[2].order(-0.2,-0.2)

    time +=1


def draw():
    clear_canvas()

    image.draw(HERO.x,HERO.y,80,120)
    for i in b:
        bimage[i.image].draw(i.x,i.y,10,10);


    #UI
    simage[0].draw(400,300)
    update_canvas()
