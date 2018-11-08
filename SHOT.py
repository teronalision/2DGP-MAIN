from pico2d import *
import ENGINE

class Shot:

    
    def __init__(self,x,y):
        self.x, self.y = x, y
        self.v = 0
        self.size = 10
        Shot.image = load_image('Image\dumy_b.png')


    def update(self):
        self.y += self.v *ENGINE.frame_time * ENGINE.p_per_meter


    def isOut(self):
        if self.y > 600:
            return True
        else:
            return False


    def draw(self):
        Shot.image.draw(self.x, self.y,20,20)
