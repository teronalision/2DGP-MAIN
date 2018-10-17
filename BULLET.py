

class bullet:

    
    def __init__(self,x,y,i):
        self.x, self.y = x, y
        self.vx, self.vy = 0, 0
        self.image = i

    def order(self,x,y):
        self.vx, self.vy = x, y

    def update(self):

        self.x += self.vx
        self.y += self.vy