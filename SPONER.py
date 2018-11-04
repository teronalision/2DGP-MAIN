import BULLET
import ENGINE

class Sponer:

    def __init__(self,x,y,m=0):
        self.x, self.y = x ,y
        self.m = m
        self.time = 0.0
        self.dead = False
        self.b_list = []

    def update(self):
        #생성
        if self.dead == False:

            if self.m == 0 and self.time > 1:
                for i in range(0,360,30):
                    b = BULLET.bullet(self.x,self.y,5)
                    b.order(0.5,i+self.time)
                    self.b_list.append(b)
                    self.time = 0
            
        #소멸
        for b in self.b_list:
            if b.x <0 or b.x >500 or b.y <0 or b.y >600:
                self.b_list.remove(b)
                del(b)

        #탄이동
        for b in self.b_list:
            b.update()

        self.time+= ENGINE.frame_time


    def draw(self):
        for b in self.b_list:
            b.draw()


    def kill(self):
        for b in self.b_list:
            #b.kill()
            pass
        self.b_list.clear()
        