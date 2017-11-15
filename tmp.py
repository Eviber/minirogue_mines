import curses
import random

class Env(object):
    def __init__(self, stdscr):
        self.map = ["######################################",
                    "#....................................#",
                    "#....................................#",
                    "#....................................#",
                    "#....................................#",
                    "#....................................#",
                    "#....................................#",
                    "#....................................#",
                    "#....................................#",
                    "######################################"]
        self.scr = stdscr
        self.player = Player()

    def display(self):
        self.scr.erase()
        for line in self.map:
            self.scr.addstr(line + '\n')
        self.player.display(self.scr)

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

    def getX(self):
        return self.x

    def moveLeft(self):
        self.x -= 1

    def moveUp(self):
        self.y -= 1

    def moveDown(self):
        self.y += 1

def doturn(env):
    pass

def getinput(env, c):
    action = {curses.KEY_UP : env.player.moveUp,
              curses.KEY_DOWN : env.player.moveDown,
              curses.KEY_LEFT : env.player.moveLeft,
              curses.KEY_RIGHT : env.player.moveRight}
    if c in action:
        action[c]()


def main(stdscr):
    curses.curs_set(False)
    c = 0

    env = Env(stdscr)

    env.display()
    while c != ord('q') :
        c = stdscr.getch()
        getinput(env, c)
        env.display()

if __name__ == "__main__":
    curses.wrapper(main)
