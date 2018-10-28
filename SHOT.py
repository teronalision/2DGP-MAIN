from pico2d import *

class Shot:

    
    def __init__(self,x,y):
        self.x, self.y = x, y
        self.v = 0
        Shot.image = load_image('dumy_b.png')


    def update(self):
        self.y += self.v


    def isOut(self):
        if self.y > 600:
            return True
        else:
            return False


    def draw(self):
        Shot.image.draw(self.x, self.y)