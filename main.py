import curses
import random
from env import *
from entities import *


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

    # cree l'environnement
    env = Env(stdscr)
    env.display()

    while c != ord('q') :
        # fait jouer le joueur
        c = stdscr.getch()
        getinput(env, c)

        # fait jouer les monstres
        env.finishTurn()

        env.display()



if __name__ == "__main__":
    curses.wrapper(main)
