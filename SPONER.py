import BULLET
import math

class Sponer:

    def __init__(self,x,y,m=0):
        self.x, self.y = x ,y
        self.m = m
        self.time = 0
        self.b_list = []

    def update(self):

        if self.m == 0 and self.time % 100 == 0:
            for i in range(0,360,30):
                b = BULLET.bullet(self.x,self.y,1)
                b.vx = math.sin(math.radians(i))
                b.vy = math.cos(math.radians(i))
                self.b_list.append(b)

        #self.x+=1

        self.time+=1