class Entity(object):
    def display(self, stdscr):
        stdscr.addch(self.y, self.x, self.char)

    def loseHP(self, n):
        self.hp -= n
        if self.hp <= 0:
            self.die()

    def die(self):
        pass


class Monster(Entity):
    def __init__(self, x, y):
        self.dead = False
        self.x = x
        self.y = y
        self.char = 'M'

    def followPlayer(self, player):
        (playerX, playerY) = player.getPos()

        # deplacement du monstre
        moveX = 0
        moveY = 0

        if playerX < self.x:
            moveX = -1
        elif playerX > self.x:
            moveX = 1

        if playerY < self.y:
            moveY = -1
        elif playerY > self.y:
            moveY = 1

        self.x += moveX
        self.y += moveY

    def die(self):
        self.dead = True


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

    def setPos(self, x, y):
        self.x = x
        self.y = y
