
import speechrecognition


class Ai1:
    body = []
    turns = {}

    def __init__(self, color, pos):  # constructor
        self.color = color
        self.head = cube1.Cube1(pos)
        self.body.append(self.head)
        self.direction = None
        self.direction_x = 0
        self.direction_y = 1
        self.timer = 0
        self.limit = 15
        self.src = speechrecognition.SpeechRecognition()

    def ai1_move(self, target_x, target_y, snack_x, snack_y):  # move the ai snake
        if self.src.speech() == "hard":  # hard mode
            self.timer = self.timer + 1.5
        else:  # normal mode
            self.timer = self.timer + 1
        if self.timer >= self.limit:
            if abs(target_x - self.body[0].pos[0]) <= 3 and abs(target_y - self.body[0].pos[1]) <= 3: # if the Snake's head is closer than 2
                if target_x < self.body[0].pos[0]:  # if the snake position is to the left of the ai snake's head
                    self.direction_x = -1
                    self.direction_y = 0
                    self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]
                elif target_x > self.body[0].pos[0]:  # if the snake position is to the right of the ai snake's head
                    self.direction_x = 1
                    self.direction_y = 0
                    self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]

                elif target_y < self.body[0].pos[1]:  # if the snakes position is above the ai snake's head
                    self.direction_x = 0
                    self.direction_y = -1
                    self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]
                elif target_y > self.body[0].pos[1]:  # if the snakes position is under the ai snake's head
                    self.direction_x = 0
                    self.direction_y = 1
                    self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]

                for i, c in enumerate(self.body):  # get index and cube in self.body
                    p = c.pos[:]  # all cube objects have a position
                    if p in self.turns:  # check if position is in turn list
                        turn = self.turns[p]
                        c.move1(turn[0], turn[1])  # give the cube the direction
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
                            c.move1(c.direction_x, c.direction_y)
                self.timer = 0
            else:
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
                        c.move1(turn[0], turn[1])  # give the cube the direction
                        if i == len(self.body) - 1:  # if the last cube of the snake is in the turn, remove the turn
                            self.turns.pop(p)

                    else:  # check if the edge of the screen is reached, if yes, teleport to the other side
                        if c.direction_x == -1 and c.pos[0] <= 0:
                            c.pos = (c.rows - 1, c.pos[1])
                        elif c.direction_x == 1 and c.pos[0] >= c.rows - 1:
                            c.pos = (0, c.pos[1])
                        elif c.direction_y == 1 and c.pos[1] >= c.rows - 1:
                            c.pos = (c.pos[0], 0)
                        elif c.direction_y == -1 and c.pos[1] <= 0:
                            c.pos = (c.pos[0], c.rows - 1)
                        else:
                            c.move1(c.direction_x, c.direction_y)
                self.timer = 0

    def add_cube1(self):
        tail = self.body[-1]
        dx, dy = tail.direction_x, tail.direction_y

        if len(self.body) == 1:
            if dx == 1 and dy == 0:  # add a body part to the right side of the snake based on the direction it's going
                self.body.append(cube1.Cube1((tail.pos[0] - 1, tail.pos[1])))
            elif dx == -1 and dy == 0:
                self.body.append(cube1.Cube1((tail.pos[0] + 1, tail.pos[1])))
            elif dx == 0 and dy == 1:
                self.body.append(cube1.Cube1((tail.pos[0], tail.pos[1] - 1)))
            elif dx == 0 and dy == -1:
                self.body.append(cube1.Cube1((tail.pos[0], tail.pos[1] + 1)))
        else:
            self.limit = self.limit - 1

        self.body[-1].direction_x = dx
        self.body[-1].direction_y = dy

    def draw1(self, surface):  # draw purple snake
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw1(surface, True)  # true basically says draw the eyes
            else:
                c.draw1(surface)
