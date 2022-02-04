
import speechrecognition


class Ai2:
    body = []  # list with amount of body parts
    turns = {}  # dictionary with te turn state of each body part

    def __init__(self, color, pos):  # constructor
        self.color = color
        self.head = cube2.Cube2(pos)
        self.body.append(self.head)
        self.direction = None
        self.direction_x = 0
        self.direction_y = 1
        self.timer = 0
        self.src = speechrecognition.SpeechRecognition()

    def ai2_move(self, snack_x, snack_y):  # move the ai snake
        if self.src.speech() == "hard":  # hard mode
            self.timer = self.timer + 1.5
        else:  # normal mode
            self.timer = self.timer + 1
        if self.timer >= 7:
            if snack_x < self.body[0].pos[0]:  # if the snake position is to the left of the ai snake's head
                self.direction_x = -1
                self.direction_y = 0
                self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]
            elif snack_x > self.body[0].pos[0]:  # if the snake position is to the right of the ai snake's head
                self.direction_x = 1
                self.direction_y = 0
                self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]

            elif snack_y < self.body[0].pos[1]:  # if the snakes position is above the ai snake's head
                self.direction_x = 0
                self.direction_y = -1
                self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]
            elif snack_y > self.body[0].pos[1]:  # if the snakes position is under the ai snake's head
                self.direction_x = 0
                self.direction_y = 1
                self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]

            for i, c in enumerate(self.body):  # get index and cube in self.body
                p = c.pos[:]  # all cube objects have a position
                if p in self.turns:  # check if position is in turn list
                    turn = self.turns[p]
                    c.move2(turn[0], turn[1])  # give the cube the direction
                    if i == len(self.body) - 1:  # if the last cube of the snake is in the turn, remove the turn
                        self.turns.pop(p)

                else:  # check if the edge of the screen is reached, if yes, teleport to the other side
                    if c.direction_x == -1 and c.pos[0] <= 0:  # from left to right
                        c.pos = (c.rows - 1, c.pos[1])
                    elif c.direction_x == 1 and c.pos[0] >= c.rows - 1:  # from right to left
                        c.pos = (0, c.pos[1])
                    elif c.direction_y == 1 and c.pos[1] >= c.rows - 1:  # from up to down
                        c.pos = (c.pos[0], 0)
                    elif c.direction_y == -1 and c.pos[1] <= 0:  # from down to up
                        c.pos = (c.pos[0], c.rows - 1)
                    else:
                        c.move2(c.direction_x, c.direction_y)
            self.timer = 0

    def draw2(self, surface):  # draw blue snake
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw2(surface, True)  # true basically says draw the eyes
            else:
                c.draw2(surface)
