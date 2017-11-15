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
        self.dead = True



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
        (x, y) = (self.x, self.y)

        deltaX = abs(playerX - x)
        deltaY = abs(playerY - y)

        if min(deltaX, deltaY) == 0 and max(deltaX, deltaY) <= 1:
            # si le monstre est cote a cote avec le joueur, il le tape
            player.loseHP(1)
        else:
            # deplacement du monstre selon x ou y
            if deltaX > deltaY:
                # si le joueur est plus eloigne sur l'axe y, il se rapproche
                # d'abord dans cette direction
                if playerX > x:
                    x += 1
                else:
                    x -= 1
            else:
                if playerY > y:
                    y += 1
                else:
                    y -= 1

            if env.map[y][x] != '#' and env.map[y][x] != ' ':
                self.setPos(x, y)


class Player(Entity):
    def __init__(self):
        self.char = '@'
        self.dead = False
        self.x = 5
        self.y = 5
        self.hp = 15
        self.gold = 0
