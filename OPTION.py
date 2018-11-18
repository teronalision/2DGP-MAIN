from pico2d import *
import ENGINE
import TITLE
import AUDIO

select = 0

def start():
    pass


def end():
    pass


def handle():
    global select
    events = get_events()

    for event in events:
        if(event.type == SDL_KEYDOWN):
            if(event.key == SDLK_DOWN):
                select = (select+1)%2
                AUDIO.play_se(0)
            elif(event.key == SDLK_UP):
                select = (select+1)%2
                AUDIO.play_se(0)
            elif(event.key == SDLK_LEFT):
                if(select == 0):
                    AUDIO.bgm_volume = max(0, AUDIO.bgm_volume-5)
                    AUDIO.set_volume()
                else:
                    AUDIO.se_volume = max(0, AUDIO.se_volume-5)
                    AUDIO.set_SEvolume()
            elif(event.key == SDLK_RIGHT):
                if(select == 0):
                    AUDIO.bgm_volume = min(100, AUDIO.bgm_volume+5)
                    AUDIO.set_volume()
                else:
                    AUDIO.se_volume = min(100, AUDIO.se_volume+5)
                    AUDIO.set_SEvolume()
            elif(event.key == SDLK_ESCAPE):
                ENGINE.Pop_state()
    pass


def update():
    pass


def draw():
    clear_canvas()
    
    ENGINE.background[5].draw(400,300,800,600)

    color = [(100,100,100) for i in range(2)]
    color[select] = (255,255,255)
    ENGINE.font.draw(100, 350,'BGM 볼륨 :    %r'%AUDIO.bgm_volume, color[0])
    ENGINE.font.draw(100, 300,'SE     볼륨 :    %r'%AUDIO.se_volume, color[1])

    update_canvas()
    pass
