from pico2d import *
import ENGINE
import HERO
import BULLET

image = None
b = [BULLET.bullet()]
bimage = None

def start():
    global image, bimage
    image = load_image('test.png')
    HERO.vy = 1
    HERO.x = 400
    bimage = [load_image('dumy_b.png')]



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
    HERO.update()

    for obj in b:
        if (HERO.x - obj.x)**2 + (HERO.y - obj.y)**2 < 60**2:
            HERO.live = False
    


def draw():
    clear_canvas()

    image.draw(HERO.x,HERO.y,80,120)
    for i in b:
        bimage[i.image].draw(i.x,i.y);

    update_canvas()