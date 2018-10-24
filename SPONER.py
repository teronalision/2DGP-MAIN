import BULLET
import math

class Sponer:

    def __init__(self,x,y,m=0):
        self.x, self.y = x ,y
        self.m = m
        self.time = 0
        self.b_list = []

    def update(self):
        #생성
        if self.m == 0 and self.time % 100 == 0:
            for i in range(0,360,30):
                b = BULLET.bullet(self.x,self.y,1)
                b.vx = math.sin(math.radians(i+self.time))
                b.vy = math.cos(math.radians(i+self.time))
                self.b_list.append(b)

        #소멸
        for b in self.b_list:
            if b.x <0 or b.x >500 or b.y <0 or b.y >500:
                self.b_list.remove(b)

        self.time+=1

    def kill():

        pass