from random import randint
from env import *

class Loot(Entity):
    def __init__(self, env, x = False, y = False):
        if x and y:
            self.x, self.y = x, y
        else:
            self.x, self.y = env.getRandPos()
        self.char = '*'
        self.value = randint(1, 50)
        self.exists = True

    def getValue(self):
        return self.value
