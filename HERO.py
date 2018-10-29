from pico2d import *
import SHOT

L_UP, L_DOWN, R_UP, R_DOWN, F_UP, F_DOWN, B_UP, B_DOWN, SHOT_UP, SHOT_DOWN = range(10)
Key_Table = {(SDL_KEYUP, SDLK_LEFT): L_UP,(SDL_KEYDOWN, SDLK_LEFT): L_DOWN,
             (SDL_KEYUP, SDLK_RIGHT): R_UP,(SDL_KEYDOWN, SDLK_RIGHT): R_DOWN,
             (SDL_KEYUP, SDLK_UP): F_UP,(SDL_KEYDOWN, SDLK_UP): F_DOWN,
             (SDL_KEYUP, SDLK_DOWN): B_UP,(SDL_KEYDOWN, SDLK_DOWN): B_DOWN,
             (SDL_KEYUP, SDLK_z):SHOT_UP, (SDL_KEYDOWN, SDLK_z):SHOT_DOWN}



class Hero:

    def __init__(self):  
        self.x, self.y = 0, 0
        self.vx, self.vy = 0, 0 
        self.speed = 0.7
        self.live = True
        self.fireList = []
        self.fire = False
        self.image = None
        self.frame = 0
        self.state = StopState
        self.state.enter(self, None)
        self.time = 0

    def shoting(self):
        new = SHOT.Shot(self.x,self.y)
        new.v = 1
        self.fireList.append(new)


    def draw(self):
        self.state.draw(self)
        for s in self.fireList:
            s.draw()
        

    def update(self):

        self.state.update(self)

        if self.fire and self.time == 0:
           self.shoting()
           self.time = 100
        elif self.time >0:
            self.time -=1

        for s in self.fireList:
           s.update()
           if s.isOut():
               self.fireList.remove(s)


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

        elif event == SHOT_DOWN:
            hero.fire = True
        elif event == SHOT_UP:
            hero.fire = False
    
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
        if hero.vx >0:
            hero.image.clip_draw(32*(hero.frame//30),48*0,32,48,hero.x,hero.y)
        elif hero.vx <0:
            hero.image.clip_draw(32*(hero.frame//30),48*1,32,48,hero.x,hero.y)
        else:
            hero.image.clip_draw(32*(hero.frame//30),48*2,32,48,hero.x,hero.y)


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

        if event == B_DOWN:
            hero.vy -= 1
        elif event == B_UP:
            hero.vy += 1
        elif event == F_DOWN:
            hero.vy += 1
        elif event == F_UP:
            hero.vy -= 1

        elif event == SHOT_DOWN:
            hero.fire = True
        elif event == SHOT_UP:
            hero.fire = False
    
    @staticmethod
    def exit(hero, event):
        pass

    @staticmethod
    def update(hero):

        if hero.live == False:
            #return
            pass

        hero.frame = (hero.frame+1) %(8*30)
        hero.y += hero.vy*hero.speed
        

    @staticmethod
    def draw(hero):
        hero.image.clip_draw(32*(hero.frame//30),0+48*2,32,48,hero.x,hero.y)



Change_State = {StopState:{L_UP:MoveState, L_DOWN:MoveState, R_UP:MoveState, R_DOWN:MoveState,F_UP:MoveState, F_DOWN:MoveState, B_UP:MoveState, B_DOWN:MoveState, SHOT_UP:StopState, SHOT_DOWN:StopState},
                MoveState:{L_UP:StopState, L_DOWN:StopState, R_UP:StopState, R_DOWN:StopState,F_UP:StopState, F_DOWN:StopState, B_UP:StopState, B_DOWN:StopState, SHOT_UP:MoveState, SHOT_DOWN:MoveState},
                }


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