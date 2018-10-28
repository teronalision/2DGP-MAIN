from pico2d import *

class shot:

    
    def __init__(self,x,y,i):
        self.x, self.y = x, y
        self.v = 0
        shot.image = load_image('dumy_b')


    def update(self):
        self.y += self.v


    def isOut(self):
        if self.y > 600:
            return True
        else:
            return False


    def draw(self):
        shot.image.draw(self.x, self.y)