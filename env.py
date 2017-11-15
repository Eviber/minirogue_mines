import curses
from entities import *

class Env(object):

    def __init__(self, stdscr):
        self.map = [
                    "##########################               ######################",
                    "#........................#               #....................#",
                    "#........................#               #....................#",
                    "#........................#      ::::::::::....................#",
                    "#........................#      :        #....................#",
                    "#........................::::::::        #....................#",
                    "#........................#               #....................#",
                    "#........................#               #....................#",
                    "#........................#               #....................#",
                    "#........................#               #....................#",
                    "############:#############               #######:##############",
                    "            :                                   :              ",
                    "            :                                   :              ",
                    "          :::                                   :              ",
                    "         ::                                     :              ",
                    "         :                                      :              ",
                    "#########:################               #######:##############",
                    "#........................#               #....................#",
                    "#........................#               #....................#",
                    "#........................#    ::::::::::::....................#",
                    "#........................#    :          #....................#",
                    "#........................::::::          #....................#",
                    "#........................#               #....................#",
                    "#........................#               #....................#",
                    "#........................#               #....................#",
                    "#........................#               #....................#",
                    "##########################               ######################",
                    ]
        self.scr = stdscr
        self.player = Player()
        self.monster = Monster(1, 1, 2)


    def finishTurn(self):
        if self.monster.dead == False:
            self.monster.followPlayer(self)

    def display(self):
        self.scr.erase()

        # affiche la map
        for line in self.map:
            self.scr.addstr(line + '\n')

        # affiche le joueur et les ennemis
        self.player.display(self.scr)
        if self.monster.dead == False:
            self.monster.display(self.scr)

    def checkInput(self, c):
        action = [curses.KEY_UP,
                  curses.KEY_DOWN,
                  curses.KEY_LEFT,
                  curses.KEY_RIGHT]
        if c in action:
            x, y = self.player.getPos()
            newx, newy = x, y
            if c == curses.KEY_UP:
                newy -= 1
            elif c == curses.KEY_DOWN:
                newy += 1
            elif c == curses.KEY_LEFT:
                newx -= 1
            elif c == curses.KEY_RIGHT:
                newx += 1
            if (newx, newy) == self.monster.getPos() and not self.monster.dead:
                self.monster.loseHP(1)
            elif self.map[newy][newx] != '#' and self.map[newy][newx] != ' ':
                self.player.setPos(newx, newy)
