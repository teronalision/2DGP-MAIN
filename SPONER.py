import math
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
        if self.dead == False:#저격탄

            if self.m == 0 and self.time >1:
                x, y = ENGINE.object_list[0][0].x-self.x, ENGINE.object_list[0][0].y-self.y

                b = BULLET.Bullet(self.x, self.y,ENGINE.RECT)
                b.order(1, math.atan2(x,y))     
                ENGINE.add_obj(b,2)
                self.time = 0


            elif self.m == 1 and self.time > 1:#12개 원형
                for i in range(0,360,30):
                    b = BULLET.Bullet(self.x,self.y,ENGINE.CIRCLE)
                    b.order(0.5,math.radians(i))
                    ENGINE.add_obj(b,2)
                    self.time = 0
      
            


        self.time+= ENGINE.frame_time



    def kill(self):
        pass
        