import curses
import random
from env import *
from entities import *

def doturn(env):
    pass

def getinput(env, c):
    action = {curses.KEY_UP : env.player.moveUp(),
              curses.KEY_DOWN : env.player.moveDown(),
              curses.KEY_LEFT : env.player.moveLeft(),
              curses.KEY_RIGHT : env.player.moveRight()}



def main(stdscr):
    curses.curs_set(False)
    c = 0

    env = Env(stdscr)

    env.display()
    while c != ord('q') :
        c = stdscr.getch()
        #getinput()
        env.display()



if __name__ == "__main__":
    curses.wrapper(main)
