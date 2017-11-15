class Entity(object):
    def display(self, stdscr):
        stdscr.addch(self.y, self.x, self.char)

    def getPos(self):
        return (self.x, self.y)

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def loseHP(self, n):
        self.hp -= n
        if self.hp <= 0:
            self.die()

    def die(self):
        pass


class Monster(Entity):
    def __init__(self, x, y, hp):
        self.dead = False
        self.char = 'M'
        self.x = x
        self.y = y
        self.hp = hp

    def followPlayer(self, env):
        player = env.player
        (playerX, playerY) = player.getPos()

        deltaX = abs(playerX - self.x)
        deltaY = abs(playerY - self.y)

        if min(deltaX, deltaY) == 0 and max(deltaX, deltaY) <= 1:
            # si le monstre est cote a cote avec le joueur, il le tape
            player.loseHP(1)
        else:
            # deplacement du monstre selon x ou y
            if deltaX > deltaY:
                # si le joueur est plus eloigne sur l'axe y, il se rapproche
                # d'abord dans cette direction
                if playerX > self.x:
                    self.x += 1
                else:
                    self.x -= 1
            else:
                if playerY > self.y:
                    self.y += 1
                else:
                    self.y -= 1


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
