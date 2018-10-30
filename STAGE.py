from pico2d import *
import ENGINE
import HERO
import SPONER

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

    ENGINE.add_obj(SPONER.Sponer(200,500),None)


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
    for list in ENGINE.yield_obj():
        list.update()

    for s_list in ENGINE.yield_obj():
        for obj in s_list.b_list:
            #탄 이동
            obj.update()

            #충돌판정
            if (hero.x - obj.x)**2 + (hero.y - obj.y)**2 < (obj.size +10)**2:
                hero.attack = True
                
    


    time +=1


def draw():
    clear_canvas()
    #캐릭터
    hero.draw()
    #총알
    for s_list in ENGINE.yield_obj():
        for i in s_list.b_list:
            bimage[i.image].draw(i.x,i.y,10,10);


    #UI
    simage[0].draw(400,300)
    for i in range(hero.life):
        bimage[0].draw(600 +50*i,500)
    
    update_canvas()
