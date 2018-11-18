from pico2d import *
import ENGINE

round_per_sec = 1.0 / 1
frame_per_round = 8
time = 0
hero_select = 0


L_UP, L_DOWN, R_UP, R_DOWN, F_UP, F_DOWN, B_UP, B_DOWN, SHOT_UP, SHOT_DOWN, DEAD = range(11)
Key_Table = {(SDL_KEYUP, SDLK_LEFT): L_UP,(SDL_KEYDOWN, SDLK_LEFT): L_DOWN,
             (SDL_KEYUP, SDLK_RIGHT): R_UP,(SDL_KEYDOWN, SDLK_RIGHT): R_DOWN,
             (SDL_KEYUP, SDLK_UP): F_UP,(SDL_KEYDOWN, SDLK_UP): F_DOWN,
             (SDL_KEYUP, SDLK_DOWN): B_UP,(SDL_KEYDOWN, SDLK_DOWN): B_DOWN,
             (SDL_KEYUP, SDLK_z):SHOT_UP, (SDL_KEYDOWN, SDLK_z):SHOT_DOWN,
             (100,100): DEAD}


class Shot:
    
    def __init__(self,x,y):
        self.x, self.y = x, y
        self.v = 0.1 * ENGINE.p_per_meter
        self.size = 10
        self.type = ENGINE.RECT
        self.r = 0


    def update(self):
        self.x += math.cos(math.radians(self.r)) *self.v *ENGINE.frame_time * ENGINE.p_per_meter
        self.y += math.sin(math.radians(self.r)) *self.v *ENGINE.frame_time * ENGINE.p_per_meter


    def isOut(self):
        if self.y > 600:
            return True
        else:
            return False


    def draw(self):
        if(ENGINE.rect_mode):
            draw_rectangle(self.x-10,self.y-40,self.x+10,self.y+40)
        ENGINE.hero_image[hero_select].clip_composite_draw(0,96,64,16,math.radians(self.r),'',self.x, self.y,80,20)

class Hero:

    def __init__(self,x,y):  
        self.x, self.y = x, y
        self.vx, self.vy = 0, 0 
        self.type = ENGINE.CIRCLE
        self.size = 10
        if hero_select == 0:
            self.speed = 1.5 * ENGINE.p_per_meter
        else:
            self.speed = 1.0 * ENGINE.p_per_meter
        self.life = 4
        self.attacked = False
        self.fireList = []
        self.fire = False
        self.power = 1
        self.frame = 0
        self.que = []
        self.state = StopState
        self.state.enter(self, None)
        self.time = 0

    def shoting(self):
        if hero_select == 0:
            new = Shot(self.x,self.y)
            new.r = 90
            self.fireList.append(new)
        else:
            for i in range(self.power):
                new = Shot(self.x,self.y)
                if self.power%2== 0:
                    new.r = 90
                else:
                    new.r = 90-30 +(30/self.power)*i
                self.fireList.append(new)


    def draw(self):
        self.state.draw(self)
        if(ENGINE.rect_mode):
            draw_rectangle(self.x -self.size, self.y -self.size, self.x +self.size, self.y +self.size)
        #ENGINE.bimage[3].clip_composite_draw(0,64+16,64,64,time*3.14/16,'',self.x,self.y,64,64)
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
           self.time = 0.1
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

        if hero.attacked:
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
        if hero.vx == 0:
            ENGINE.hero_image[hero_select].clip_draw(32*int(hero.frame),256-48*1,32,48,hero.x,hero.y)
        elif hero.vx <0:
            ENGINE.hero_image[hero_select].clip_draw(32*int(hero.frame),256-48*2,32,48,hero.x,hero.y)
        else:
            ENGINE.hero_image[hero_select].clip_draw(32*int(hero.frame),256-48*3,32,48,hero.x,hero.y)


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

        if hero.attacked:
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
        ENGINE.hero_image[hero_select].clip_draw(32*int(hero.frame),256-48,32,48,hero.x,hero.y)


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
            hero.power = max(1, hero.power - 5)

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
            hero.attacked = False
            hero.add_que(DEAD)


    @staticmethod
    def draw(hero):
        ENGINE.hero_image[hero_select].clip_draw(32*int(hero.frame),256-48,32,48,hero.x,hero.y)
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
