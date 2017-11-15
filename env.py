import curses
from entities import *
from loot import *
from random import random, randint

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
        self.monsters = []
        self.loots = []
        maxloot = randint(3, 6)
        for i in range(maxloot):
            self.loots.append(Loot(self))


    def finishTurn(self):
        self.loots = [l for l in self.loots if l.exists]
        self.monsters = [m for m in self.monsters if not m.dead]
        for m in self.monsters:
            m.followPlayer(self)

        if len(self.monsters) < 5 and random() < 0.1:
            (x, y) = self.getRandPos()
            self.monsters.append(Monster(x, y, randint(1,3)))


    def display(self):
        self.scr.erase()

        # affiche la map
        for line in self.map:
            self.scr.addstr(line + '\n')

        # affiche les loots
        for l in self.loots:
            l.display(self.scr)

        # affiche le joueur et les ennemis
        self.player.display(self.scr)
        for m in self.monsters:
            m.display(self.scr)

        # affiche les infos sur le jeu
        n = len(self.map)
        self.scr.addstr(n, 0, '\n\n HP : ' + str(self.player.hp) + ', gold : ' + str(self.player.gold))

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
            if self.map[newy][newx] != '#' and self.map[newy][newx] != ' ':
                self.player.setPos(newx, newy)
            for l in self.loots:
                if (newx, newy) == l.getPos():
                    self.player.gold += l.value
                    l.exists = False
            for m in self.monsters:
                if (newx, newy) == m.getPos():
                    m.loseHP(1)
                    self.player.setPos(x, y)

    def getRandPos(self):
        x = 0
        y = 0
        cols = len(self.map[0])
        lines = len(self.map)
        while (x, y) == self.player.getPos() or self.map[y][x] != '.':
            x = randint(0, cols-1)
            y = randint(0, lines-1)
        return (x, y)
