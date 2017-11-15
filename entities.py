from env import *

class Entity(object):
    def display(self, stdscr):
        stdscr.addch(self.y, self.x, self.char)

class Monster(Entity):
     def __init__(self, x, y):
        self.x = x
        self.y = y
        self.char = 'M'

class Player(Entity):
    def __init__(self):
        self.x = 5
        self.y = 5
        self.hp = 15
        self.char = '@'

    def moveRight(self):
        self.x += 1

    def moveLeft(self):
        self.x -= 1

    def moveUp(self):
        self.y -= 1

    def moveDown(self):
        self.y += 1

    def getPos(self):
        return (self.x, self.y)
