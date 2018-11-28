import math
import BULLET
import ENGINE
import AUDIO

class Sponer:

    def __init__(self,x,y,m=0):
        self.x, self.y = x ,y
        self.m = m
        self.count = 0.0
        self.time = 0.0
        self.dead = False

    def update(self):
        #생성
        if self.dead == False:

            if self.m == 0 and self.count >0.5:#저격탄
                x, y = ENGINE.object_list[0][0].x-self.x, ENGINE.object_list[0][0].y-self.y

                b = BULLET.Bullet(self.x, self.y,BULLET.CART)
                b.order(1, math.atan2(x,y))
                ENGINE.add_obj(b,2)
                #AUDIO.play_se(4)
                self.count = 0


            elif self.m == 1 and self.count > 1:#페어리
                for i in range(0,360,15):
                    b = BULLET.Bullet(self.x,self.y,BULLET.SUN)
                    b.order(1,math.radians(i))
                    ENGINE.add_obj(b,2)
                    AUDIO.play_se(5)
                    self.count = 0
           
            elif self.m == 2 and self.count >0.25:#4방향
                for i in range(0,360,90):
                    b = BULLET.Bullet(self.x,self.y,BULLET.BALL)
                    b.order(1,math.radians(i))
                    ENGINE.add_obj(b,2)
                    AUDIO.play_se(3)
                    self.count = 0

            elif self.m == 3 and self.count >0.2:#회오리
                for i in range(0,360,60):
                    b = BULLET.Bullet(self.x,self.y,BULLET.BALL)
                    b.order(1,math.radians(i+(self.time*10)))
                    ENGINE.add_obj(b,2)
                    self.count = 0
                    
            elif self.m == 4 and self.count > 0.1:
                for i in range(3):
                    b = BULLET.Bullet(self.x,self.y,BULLET.BALL)
                    b.order(1,math.radians(ENGINE.randint(0,360)))
                    ENGINE.add_obj(b,2)
                    self.count = 0


        self.count+= ENGINE.frame_time
        self.time+= ENGINE.frame_time



    def kill(self):
        pass
        