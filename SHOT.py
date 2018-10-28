
class shot:

    
    def __init__(self,x,y,i):
        self.x, self.y = x, y
        self.v = 0

    def update(self):
        self.y += self.v