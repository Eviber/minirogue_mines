from entities import *

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
        self.monster = Monster(10, 10)


    def finishTurn(self):
        self.monster.followPlayer(self.player)

    def display(self):
        self.scr.erase()

        # affiche la map
        for line in self.map:
            self.scr.addstr(line + '\n')

        # affiche le joueur et les ennemis
        self.player.display(self.scr)
        self.monster.display(self.scr)
