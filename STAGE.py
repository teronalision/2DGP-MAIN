from pico2d import *
import ENGINE
import AUDIO
import GIMMICK
import HERO
import ZAKO
import ITEM
import GAME_OVER
import CLEARPAGE

hero = None
cloud = None
point = 0
stageclear = 5.0


def start():
    global hero,cloud,point,stageclear

    GIMMICK.init()
    AUDIO.play_music(ENGINE.stage_num+1)
    if hero == None:
        ENGINE.add_obj(HERO.Hero(250, 100),0)
        hero = ENGINE.object_list[0][0]
        point = 0
    cloud = [0.0,0.0]
    stageclear = 5.0
    
    

def end():


    AUDIO.stop_music()
    ENGINE.del_obj()
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
        elif(e.type == SDL_KEYDOWN and e.key == SDLK_F1):
            if ENGINE.undead:
                ENGINE.undead = False
            else:
                ENGINE.undead = True
        elif(e.type == SDL_KEYDOWN and e.key == SDLK_F2):
            GIMMICK.time = 56

        hero.handle(e)



def update():
    global cloud, point, stageclear
    cloud[0] += ENGINE.frame_time
    cloud[1] += ENGINE.frame_time/3
    #로직
    if GIMMICK.run_stage():
        stageclear -= ENGINE.frame_time
        ENGINE.del_obj();
        if stageclear <0:
            AUDIO.play_se(2)
            #스테이지 교체
            ENGINE.Change_state(CLEARPAGE)
            return
    


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
                AUDIO.play_se(1)
                ENGINE.add_obj(ITEM.PowerUp(hero.x,hero.y),3)
            
                if hero.life == 1:
                    ENGINE.Change_state(GAME_OVER)
                    return
            obj.kill()
            break
    for item in ENGINE.object_list[3]:
        if ENGINE.is_crash(hero,item):
            item.effect(hero)
            point += 100


    #자코-공격 충돌
    for e in ENGINE.object_list[1]:
        for h_b in hero.fireList:
            if ENGINE.is_crash(e, h_b) and e.dead == False:
                if(HERO.hero_select == 0):
                    e.attacked(hero.power)
                else:
                    e.attacked(1)
                h_b.x = -1000
                point += e.point
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
    ENGINE.background[6].clip_draw(0,0,800,350,250,150-cloud[0],500,300)
    ENGINE.background[6].clip_draw(800,0,200,200,150,550-cloud[1],200,200)
    #캐릭터
    hero.draw()
    #모든 객체
    for a in ENGINE.all_obj():
        a.draw()


    #UI
    ENGINE.background[0].draw(400,300)

    ENGINE.font.draw(510, 550,'Point  %r'%point, (255,255,255))

    for i in range(hero.life -1):
        ENGINE.bimage[5].clip_draw(0,0,100,100,620 +50*i,490,40,40)
    ENGINE.font.draw(510, 490,'Life', (255,255,255))

    ENGINE.font.draw(510, 430,'boom', (255,255,255))

    ENGINE.font.draw(510, 370,'Power  %r'%hero.power, (255,255,255))

    ENGINE.font.draw(510, 100,'%r' %ENGINE.stage_num, (255,255,255))
    update_canvas()
