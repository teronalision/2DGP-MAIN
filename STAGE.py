from pico2d import *
import ENGINE
import HERO
import SPONER
import ZAKO

hero = HERO.Hero()
#sp = [SPONER.Sponer(100,500),SPONER.Sponer(200,500),SPONER.Sponer(400,500),SPONER.Sponer(300,500)]
bimage = None
simage = None
time = 0.0
step = 0

def start():
    global image, bimage, simage,hero

    hero.x,hero.y = 250, 100
    hero.image = load_image('C1.png')
    bimage = [load_image('dumy_b.png'), load_image('dumy_c.png')]
    simage = [load_image('bg1.png')]

    #ENGINE.add_obj(SPONER.Sponer(200,500),1)
   
    

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
    global time,step

    #로직
    if step == 0 and int(time) == 0:
        ENGINE.add_obj(ZAKO.zako(200,600,1,bimage[1]),1)
        ENGINE.add_obj(ZAKO.zako(300,600,1,bimage[1]),1)
        step += 1
    elif step == 1 and int(time) == 2:
        ENGINE.add_obj(ZAKO.zako(100,600,1,bimage[1]),1)
        ENGINE.add_obj(ZAKO.zako(400,600,1,bimage[1]),1)
        step += 1
    elif step == 2 and int(time) == 4:
        time, step = 0, 0



    #캐릭터 이동
    hero.update()

    #내부 업데이트
    for list in ENGINE.all_obj():
        list.update()

    #캐릭터 충돌
    for s_list in ENGINE.yield_obj(1):
        for obj in s_list.sponer.b_list:

            if ENGINE.is_crash(hero,obj):
                hero.attack = True
                for s in ENGINE.object_list[1]:
                    s.kill()

    #자코 충돌
    for e in ENGINE.yield_obj(1):
        for h_b in hero.fireList:
            if ENGINE.is_crash(h_b, e) and e.dead == False:
                e.kill()
                #총알 펑
                hero.fireList.remove(h_b)
                #ENGINE.object_list[1].remove(e)
                break
    


    time += ENGINE.frame_time


def draw():
    clear_canvas()
    #캐릭터
    hero.draw()
    #총알
    for a in ENGINE.all_obj():
        a.draw()


    #UI
    simage[0].draw(400,300)
    ENGINE.font.draw(510, 550,'Point', (0,0,0))

    for i in range(hero.life -1):
        bimage[0].draw(600 +50*i,500)
    ENGINE.font.draw(510, 500,'Lift', (0,0,0))

    ENGINE.font.draw(510, 450,'boom', (0,0,0))

    update_canvas()
