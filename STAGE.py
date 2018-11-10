from pico2d import *
import ENGINE
import HERO
import SPONER
import ZAKO
import GAME_OVER

hero = None
#sp = [SPONER.Sponer(100,500),SPONER.Sponer(200,500),SPONER.Sponer(400,500),SPONER.Sponer(300,500)]
time = 0.0
step = 0

def start():
    global hero

    hero = HERO.Hero()
    hero.x,hero.y = 250, 100
    
    

def end():
    global hero

    ENGINE.del_obj()
    del(hero)
    time = 0.0
    step = 0
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
        ENGINE.add_obj(ZAKO.fairy(0,500,1),1)

        step += 1
    elif step == 1 and int(time) == 5:
        ENGINE.add_obj(ZAKO.fairy(500, 500, 2), 1)
        step += 1
    elif step == 2 and int(time) == 10:
        time, step = 0, 0



    #캐릭터 이동
    hero.update()

    #내부 업데이트
    for list in ENGINE.all_obj():
        list.update()

    #캐릭터 충돌
    for obj in ENGINE.object_list[1] + ENGINE.object_list[2]:
        if ENGINE.is_crash(hero,obj):
            if hero.life == 1:
                ENGINE.Change_state(GAME_OVER)
                return

            hero.attack = True
            break


    #자코-공격 충돌
    for e in ENGINE.object_list[1]:
        for h_b in hero.fireList:
            if ENGINE.is_crash(h_b, e) and e.dead == False:
                e.kill()
                break
    
    #시체 청소
    for obj in ENGINE.object_list[1]:
        if obj.dead:
            ENGINE.object_list[1].remove(obj)
            del(obj)
    for obj in ENGINE.object_list[2]:
        if obj.dead:
            ENGINE.object_list[2].remove(obj)
            del(obj)


    time += ENGINE.frame_time


def draw():
    clear_canvas()
    #BG
    ENGINE.background[1].clip_draw(0,0,720,1280,250,250)

    #캐릭터
    hero.draw()
    #총알
    for a in ENGINE.all_obj():
        a.draw()


    #UI
    ENGINE.simage[0].draw(400,300)
    ENGINE.font.draw(510, 550,'Point', (0,0,0))

    for i in range(hero.life -1):
        ENGINE.bimage[0].draw(600 +50*i,500)
    ENGINE.font.draw(510, 500,'Life', (0,0,0))

    ENGINE.font.draw(510, 450,'boom', (0,0,0))

    update_canvas()
