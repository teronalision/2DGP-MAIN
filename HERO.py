from pico2d import *
import SHOT
import ENGINE

round_per_sec = 1.0 / 1
frame_per_round = 8
time = 0

L_UP, L_DOWN, R_UP, R_DOWN, F_UP, F_DOWN, B_UP, B_DOWN, SHOT_UP, SHOT_DOWN, DEAD = range(11)
Key_Table = {(SDL_KEYUP, SDLK_LEFT): L_UP,(SDL_KEYDOWN, SDLK_LEFT): L_DOWN,
             (SDL_KEYUP, SDLK_RIGHT): R_UP,(SDL_KEYDOWN, SDLK_RIGHT): R_DOWN,
             (SDL_KEYUP, SDLK_UP): F_UP,(SDL_KEYDOWN, SDLK_UP): F_DOWN,
             (SDL_KEYUP, SDLK_DOWN): B_UP,(SDL_KEYDOWN, SDLK_DOWN): B_DOWN,
             (SDL_KEYUP, SDLK_z):SHOT_UP, (SDL_KEYDOWN, SDLK_z):SHOT_DOWN,
             (100,100): DEAD}



class Hero:

    def __init__(self):  
        self.x, self.y = 0, 0
        self.vx, self.vy = 0, 0 
        self.size = 5
        self.speed = 1.5 * ENGINE.p_per_meter
        self.life = 4
        self.attack = False
        self.fireList = []
        self.fire = False
        self.power = 2
        self.image = None
        self.frame = 0
        self.que = []
        self.state = StopState
        self.state.enter(self, None)
        self.time = 0

    def shoting(self):
        for i in range(self.power):
            new = SHOT.Shot(self.x -(self.power*10) +(i*20),self.y)
            new.v = 10
            self.fireList.append(new)


    def draw(self):
        self.state.draw(self)
        ENGINE.bimage[3].clip_composite_draw(0,64+16,64,64,time*3.14/16,'',self.x,self.y,64,64)
        for s in self.fireList:
            s.draw()
        
    def add_que(self, q):
        self.que.insert(0,q)

    def update(self):
        global time

        self.state.update(self)
        time += ENGINE.frame_time        

        if len(self.que) >0:
            key = self.que.pop()
            self.state.exit(self,key)
            self.state = Change_State[self.state][key]
            self.state.enter(self, key)


        if self.fire and self.time <= 0:
           self.shoting()
           self.time = 0.3
        elif self.time >0:
            self.time -= ENGINE.frame_time

        for s in self.fireList:
           s.update()
           if s.isOut():
               self.fireList.remove(s)


    def handle(self, event):

        if (event.type, event.key) in Key_Table:
            key = Key_Table[(event.type, event.key)]
            self.add_que(key)


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

        if abs(hero.vx) == 2:
            hero.vx /= hero.vx
        if abs(hero.vy) == 2:
            hero.vy /= hero.vy
    
    @staticmethod
    def exit(hero, event):
        pass

    @staticmethod
    def update(hero):

        if hero.attack:
            hero.life -= 1
            hero.add_que(DEAD)
            pass


        if hero.frame <4:
            hero.frame = (hero.frame+ frame_per_round*round_per_sec*ENGINE.frame_time)
        else:
            hero.frame = 4+(hero.frame+ frame_per_round*round_per_sec*ENGINE.frame_time) %4

        hero.x += hero.vx*hero.speed*ENGINE.frame_time
        hero.y += hero.vy*hero.speed*ENGINE.frame_time

        hero.x = clamp(0 +16,hero.x,500 -16)
        hero.y = clamp(0 +32,hero.y,600 -32)


    @staticmethod
    def draw(hero):
        if hero.vx >0:
            hero.image.clip_draw(32*int(hero.frame),48*0,32,48,hero.x,hero.y)
        elif hero.vx <0:
            hero.image.clip_draw(32*int(hero.frame),48*1,32,48,hero.x,hero.y)
        else:
            hero.image.clip_draw(32*int(hero.frame),48*2,32,48,hero.x,hero.y)


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
        
        if abs(hero.vx) == 2:
            hero.vx /= hero.vx
        if abs(hero.vy) == 2:
            hero.vy /= hero.vy

    @staticmethod
    def exit(hero, event):
        pass

    @staticmethod
    def update(hero):

        if hero.attack:
            hero.life -= 1
            hero.add_que(DEAD)
            pass

        hero.frame = (hero.frame+ frame_per_round*round_per_sec*ENGINE.frame_time) %8

        hero.x += hero.vx*hero.speed*ENGINE.frame_time
        hero.y += hero.vy*hero.speed*ENGINE.frame_time

        hero.x = clamp(0 +16,hero.x,500 -16)
        hero.y = clamp(0 +32,hero.y,600 -32)

    @staticmethod
    def draw(hero):
        hero.image.clip_draw(32*int(hero.frame),0+48*2,32,48,hero.x,hero.y)


class DeadState:

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


        if event == DEAD:
            hero.x, hero.y = 250, 0 -32

        hero.fire = False
        hero.fireList.clear()
        pass

    
    @staticmethod
    def exit(hero, event):
        pass

    @staticmethod
    def update(hero):

        hero.frame = (hero.frame+ frame_per_round*round_per_sec*ENGINE.frame_time) %8

        hero.y += 0.2*hero.speed*ENGINE.frame_time
        if hero.y > 100:
            hero.attack = False
            hero.add_que(DEAD)


    @staticmethod
    def draw(hero):
        hero.image.clip_draw(32*int(hero.frame),0+48*2,32,48,hero.x,hero.y)
        #임시
        ENGINE.font.draw(10, 15,'리스폰', (0,0,0))



Change_State = {StopState:{L_UP:MoveState, L_DOWN:MoveState, R_UP:MoveState, R_DOWN:MoveState,F_UP:MoveState, F_DOWN:MoveState, B_UP:MoveState, B_DOWN:MoveState, SHOT_UP:StopState, SHOT_DOWN:StopState, DEAD:DeadState},
                MoveState:{L_UP:StopState, L_DOWN:StopState, R_UP:StopState, R_DOWN:StopState,F_UP:StopState, F_DOWN:StopState, B_UP:StopState, B_DOWN:StopState, SHOT_UP:MoveState, SHOT_DOWN:MoveState, DEAD:DeadState},
                DeadState:{L_UP:DeadState, L_DOWN:DeadState, R_UP:DeadState, R_DOWN:DeadState,F_UP:DeadState, F_DOWN:DeadState, B_UP:DeadState, B_DOWN:DeadState, SHOT_UP:DeadState, SHOT_DOWN:DeadState, DEAD:StopState}
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
