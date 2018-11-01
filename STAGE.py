from pico2d import *
import ENGINE
import HERO
import SPONER
import ZAKO

hero = HERO.Hero()
#sp = [SPONER.Sponer(100,500),SPONER.Sponer(200,500),SPONER.Sponer(400,500),SPONER.Sponer(300,500)]
bimage = None
simage = None
time = 0

def start():
    global image, bimage, simage,hero

    hero.x,hero.y = 250, 100
    hero.image = load_image('C1.png')
    bimage = [load_image('dumy_b.png'), load_image('dumy_c.png')]
    simage = [load_image('bg1.png')]

    ENGINE.add_obj(SPONER.Sponer(200,500),1)
    ENGINE.add_obj(ZAKO.zako(0,600,0,bimage[1]),0)


def end():
    pass


def handle():
    events = get_events()

    for e in events:
        if(e.type == SDL_QUIT):
            ENGINE.Quit()
        elif(e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE):
            ENGINE.Quit()

        hero.handle(e)



def update():
    global time

    #캐릭터 이동
    hero.update()

    #생성
    for list in ENGINE.all_obj():
        list.update()

    for s_list in ENGINE.yield_obj(1):
        for obj in s_list.b_list:
            #탄 이동
            obj.update()

            #충돌판정
            if ENGINE.is_crash(hero,obj):
                hero.attack = True
                for s in ENGINE.object_list[1]:
                    s.kill()
                
    


    time +=1


def draw():
    clear_canvas()
    #캐릭터
    hero.draw()
    #총알
    for a in ENGINE.all_obj():
        a.draw()


    #UI
    simage[0].draw(400,300)
    for i in range(hero.life -1):
        bimage[0].draw(600 +50*i,500)
    
    update_canvas()
