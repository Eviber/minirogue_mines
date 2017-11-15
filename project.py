import curses

class Entity(object):
    def display(self, stdscr):
        stdscr.addch(self.y, self.x, self.char)


class Player(Entity):
    def __init__(self, map):
        self.x = 5
        self.y = 5
        self.hp = 15
        self.char = '@'
        self.map = map

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


class Monster(Entity):
     def __init__(self, x, y):
        self.x = x
        self.y = y
        self.char = 'M'





def main(stdscr):
    curses.curs_set(False)
    c = 0

    player = Player(1)

    while c != ord('q') :
        c = stdscr.getch()

        if c == curses.KEY_LEFT:
            player.moveLeft()
        elif c == curses.KEY_RIGHT:
            player.moveRight()
        if c == curses.KEY_UP:
            player.moveUp()
        elif c == curses.KEY_DOWN:
            player.moveDown()

        stdscr.erase()
        player.display(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
