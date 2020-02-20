from random import randrange

# colors
GREEN = (0,255,0)

class Food:

    def __init__(self):
        self.row_ = randrange(10)
        self.col_ = randrange(10)
        self.color_ = GREEN

    def ChangeLocation(self):
        self.row_ = randrange(10)
        self.col_ = randrange(10)