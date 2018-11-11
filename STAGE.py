from pico2d import *
import ENGINE
import HERO
import ZAKO
import ITEM
import GAME_OVER

hero = None
sponer = ZAKO.Monster_sponer()
time = 0.0
step = 0

def start():
    global hero

    ENGINE.add_obj(HERO.Hero(250, 100),0)
    hero = ENGINE.object_list[0][0]
    

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
    if step == 0 and time-int(time) < 0.01 :
        sponer.add_monster(ZAKO.FAIRY,0,500,ZAKO.R)

        if(time>5):
            step += 1
    elif step == 1:
        sponer.add_monster(ZAKO.RUNE,250,500,ZAKO.PATROL)

        step += 1
    elif step == 2 and int(time) == 10:
        time, step = 0, 0



    #캐릭터 이동
    hero.update()

    #내부 업데이트
    for obj in ENGINE.all_obj():
        obj.update()

    #캐릭터 충돌
    for obj in ENGINE.object_list[1] + ENGINE.object_list[2]:
        if ENGINE.is_crash(hero,obj) and hero.attacked == False and ENGINE.undead == False:
            hero.attacked = True
            obj.kill()

            ENGINE.add_obj(ITEM.PowerUp(hero.x,hero.y),3)

            if hero.life == 1:
                ENGINE.Change_state(GAME_OVER)
                return
            break
    for item in ENGINE.object_list[3]:
        if ENGINE.is_crash(hero,item):
            item.effect(hero)


    #자코-공격 충돌
    for e in ENGINE.object_list[1]:
        for h_b in hero.fireList:
            if ENGINE.is_crash(e, h_b) and e.dead == False:
                e.attacked(hero.power)
                h_b.x = -100
                break
    
    #시체 청소
    for i in range(1,4):
        for obj in ENGINE.object_list[i]:
            if obj.dead:
                obj.kill()
                ENGINE.object_list[i].remove(obj)


    time += ENGINE.frame_time


def draw():
    clear_canvas()
    #BG
    ENGINE.background[1].clip_draw(0,0,720,1280,250,250)

    #캐릭터
    hero.draw()
    #모든 객체
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
