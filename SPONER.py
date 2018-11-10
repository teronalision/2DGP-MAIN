import BULLET
import ENGINE

class Sponer:

    def __init__(self,x,y,m=0):
        self.x, self.y = x ,y
        self.m = m
        self.time = 0.0
        self.dead = False

    def update(self):
        #생성
        if self.dead == False:

            if self.m == 0 and self.time > 1:
                for i in range(0,360,30):
                    b = BULLET.Bullet(self.x,self.y,10)
                    b.order(0.5,i+self.time)
                    ENGINE.object_list[2].append(b)
                    self.time = 0
      

        self.time+= ENGINE.frame_time



    def kill(self):
        pass
        