from pico2d import *
from builtins import staticmethod


L_UP, L_DOWN, R_UP, R_DOWN, F_UP, F_DOWN, B_UP, B_DOWN, SHOTING = range(9)
Key_Table = {(SDL_KEYUP, SDLK_LEFT): L_UP,(SDL_KEYDOWN, SDLK_LEFT): L_DOWN,
             (SDL_KEYUP, SDLK_RIGHT): R_UP,(SDL_KEYDOWN, SDLK_RIGHT): R_DOWN,
             (SDL_KEYUP, SDLK_UP): F_UP,(SDL_KEYDOWN, SDLK_UP): F_DOWN,
             (SDL_KEYUP, SDLK_DOWN): B_UP,(SDL_KEYDOWN, SDLK_DOWN): B_DOWN}



class Hero:

    def __init__(self):  
        self.x, self.y = 0, 0
        self.vx, self.vy = 0, 0 
        self.speed = 0.7
        self.live = True

        Hero.image = load_image("C1.png")
        self.frame = 0
        self.state = StopState
        self.state.enter(self, None)

       
    def draw(self):
        self.state.draw(self)
        pass

    def update(self):
       self.state.update(self)

    def handle(self, event):
        if (event.type, event.key) in Key_Table:
            key = Key_Table[(event.type, event.key)]
            self.state.exit(self,key)
            self.state = Change_State[self.state][key]
            self.state.enter(self, key)


class MoveState:

    @staticmethod
    def enter(hero, event):
        if event == L_DOWN:
            hero.vx -= 1
        elif event == L_UP:
            hero.vx += 1
        elif event == R_DOWN:
            hero.vx += 1
        elif event == R_UP:
            hero.vx -= 1
        elif event == B_DOWN:
            hero.vy -= 1
        elif event == B_UP:
            hero.vy += 1
        elif event == F_DOWN:
            hero.vy += 1
        elif event == F_UP:
            hero.vy -= 1
    
    @staticmethod
    def exit(hero, event):
        pass

    @staticmethod
    def update(hero):

        if hero.live == False:
            #return
            pass

        hero.frame = (hero.frame+1) %(8*30)
        hero.x += hero.vx*hero.speed
        hero.y += hero.vy*hero.speed

    @staticmethod
    def draw(hero):
        hero.image.clip_draw(32*(hero.frame//30),1+48*2,32,48,hero.x,hero.y)

class StopState:

    @staticmethod
    def enter(hero, event):
        if event == L_DOWN:
            hero.vx -= 1
        elif event == L_UP:
            hero.vx += 1
        elif event == R_DOWN:
            hero.vx += 1
        elif event == R_UP:
            hero.vx -= 1
        elif event == B_DOWN:
            hero.vy -= 1
        elif event == B_UP:
            hero.vy += 1
        elif event == F_DOWN:
            hero.vy += 1
        elif event == F_UP:
            hero.vy -= 1
    
    @staticmethod
    def exit(hero, event):
        pass

    @staticmethod
    def update(hero):

        if hero.live == False:
            #return
            pass

        hero.frame = (hero.frame+1) %(8*30)
        

    @staticmethod
    def draw(hero):
        hero.image.clip_draw(32*(hero.frame//30),0+48*2,32,48,hero.x,hero.y)



Change_State = {StopState:{L_UP:MoveState, L_DOWN:MoveState, R_UP:MoveState, R_DOWN:MoveState,F_UP:MoveState, F_DOWN:MoveState, B_UP:MoveState, B_DOWN:MoveState},
                MoveState:{L_UP:StopState, L_DOWN:StopState, R_UP:StopState, R_DOWN:StopState,F_UP:StopState, F_DOWN:StopState, B_UP:StopState, B_DOWN:StopState}}


if __name__ == '__main__':
    open_canvas()
    
    hero = Hero()
    while 1:
        clear_canvas()
        events = get_events()
        for e in events:
            hero.handle(e)
        hero.update()
        hero.draw()
        update_canvas()
        #delay(0.1)

    close_canvas()