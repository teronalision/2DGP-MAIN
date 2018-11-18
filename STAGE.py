from pico2d import *
import ENGINE
import AUDIO
import GIMMICK
import HERO
import ZAKO
import ITEM
import GAME_OVER

hero = None


def start():
    global hero

    GIMMICK.init()
    AUDIO.play_music(1)
    ENGINE.add_obj(HERO.Hero(250, 100),0)
    hero = ENGINE.object_list[0][0]
    

def end():
    global hero

    AUDIO.stop_music()
    ENGINE.del_obj()
    del(hero)
    time = 0.0
    step = 0
    pass


def handle():
    events = get_events()

    for e in events:
        if(e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE):
            ENGINE.Pop_state()
            ENGINE.state_stack[-1].start()
            break

        hero.handle(e)



def update():
    #로직
    GIMMICK.run_stage()



    #캐릭터 이동
    hero.update()

    #내부 업데이트
    for obj in ENGINE.all_obj():
        obj.update()

    #캐릭터 충돌
    for obj in ENGINE.object_list[1] + ENGINE.object_list[2]:
        if ENGINE.is_crash(hero,obj):
            if hero.attacked == False and ENGINE.undead == False:
                hero.attacked = True
                ENGINE.add_obj(ITEM.PowerUp(hero.x,hero.y),3)
            
                if hero.life == 1:
                    ENGINE.Change_state(GAME_OVER)
                    return
            obj.kill()
            break
    for item in ENGINE.object_list[3]:
        if ENGINE.is_crash(hero,item):
            item.effect(hero)


    #자코-공격 충돌
    for e in ENGINE.object_list[1]:
        for h_b in hero.fireList:
            if ENGINE.is_crash(e, h_b) and e.dead == False:
                if(HERO.hero_select == 0):
                    e.attacked(hero.power)
                else:
                    e.attacked(1)
                h_b.x = -100
                break
    
    #시체 청소
    for i in range(1,4):
        for obj in ENGINE.object_list[i]:
            if obj.dead:
                obj.kill()
                ENGINE.object_list[i].remove(obj)



def draw():
    clear_canvas()
    #BG
    ENGINE.background[3].clip_draw(0,int(ENGINE.frame_time),500,600,250,300)

    #캐릭터
    hero.draw()
    #모든 객체
    for a in ENGINE.all_obj():
        a.draw()


    #UI
    ENGINE.background[0].draw(400,300)
    ENGINE.font.draw(510, 550,'Point', (255,255,255))

    for i in range(hero.life -1):
        ENGINE.bimage[0].draw(600 +50*i,500)
    ENGINE.font.draw(510, 490,'Life', (255,255,255))

    ENGINE.font.draw(510, 430,'boom', (255,255,255))

    update_canvas()
