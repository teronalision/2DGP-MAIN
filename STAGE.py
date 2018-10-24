from pico2d import *
import ENGINE
import HERO
import BULLET
import SPONER


sp = [SPONER.Sponer(100,500),SPONER.Sponer(200,500),SPONER.Sponer(400,500),SPONER.Sponer(300,500)]
bimage = None
simage = None
time = 0

def start():
    global image, bimage, simage
    HERO.start()
    HERO.x,HERO.y = 250, 100
    bimage = [load_image('dumy_b.png'), load_image('dumy_c.png')]
    simage = [load_image('bg1.png')]



def end():
    pass


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
    for list in sp:
        list.update()

    for s_list in sp:
        for obj in s_list.b_list:
            #탄 이동
            obj.update()

            #충돌판정
            if (HERO.x - obj.x)**2 + (HERO.y - obj.y)**2 < 60**2:
                HERO.live = False
    


    time +=1


def draw():
    clear_canvas()

    HERO.draw()

    for s_list in sp:
        for i in s_list.b_list:
            bimage[i.image].draw(i.x,i.y,10,10);


    #UI
    simage[0].draw(400,300)
    update_canvas()