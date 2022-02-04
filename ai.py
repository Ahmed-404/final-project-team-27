import pygame
import cube
import cube1
import cube2
import cube_S
import speechrecognition


class Ai:
    body = []
    turns = {}

    def __init__(self, color, pos):  # constructor
        self.color = color
        self.head = cube.Cube(pos, self.color)
        self.body.append(self.head)
        self.direction = None
        self.direction_x = 0
        self.direction_y = 1
        self.src = speechrecognition.SpeechRecognition()
        self.timer = 0
        self.limit = 15
        self.cimer = 40
        self.iter_val = 10
        self.score = 0
        self.in_game_time = 0

    def p_move(self):  # move the snake and change its speed
        self.cimer = self.cimer + self.iter_val
        self.in_game_time = self.in_game_time + 1
        if self.src.speech() == "fast":  # increase speed snake
            self.iter_val = self. iter_val + 10
            print('going faster!')
        if self.src.speech() == "slow":  # decrease speed snake
            self.iter_val = self.iter_val - 10
            print('Slowing down!')
        if self.src.speech() == "quit":  # close the game
            pygame.quit()

        if self.cimer >= 30:  # speed limit on player snake
            self.cimer = 0
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                for key in keys:
                    if keys[pygame.K_LEFT]:  # go left with left arrow
                        self.direction_x = -1
                        self.direction_y = 0
                        self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]

                    elif keys[pygame.K_RIGHT]:  # go right with right arrow
                        self.direction_x = 1
                        self.direction_y = 0
                        self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]

                    elif keys[pygame.K_UP]:  # go up with up arrow
                        self.direction_x = 0
                        self.direction_y = -1
                        self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]

                    elif keys[pygame.K_DOWN]:  # go down with down arrow
                        self.direction_x = 0
                        self.direction_y = 1
                        self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]

                    if keys[pygame.K_r]:  # record voice of user when pressing r for input
                        self.src.set_speech(True)
                    else:
                        self.src.set_speech(False)
                    if keys[pygame.K_ESCAPE]:
                        pygame.quit()

            for i, c in enumerate(self.body):  # get index and cube in self.body
                p = c.pos[:]  # all cube objects have a position
                if p in self.turns:  # check if position is in turn list
                    turn = self.turns[p]
                    c.move(turn[0], turn[1])  # give the cube the direction
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
                        c.move(c.direction_x, c.direction_y)



    def ai_move(self, snack_x, snack_y):  # move the ai snake
        if self.src.speech() == "hard":  # hard mode
            self.timer = self.timer + 1.5
            print("hard mode on")
        else:  # normal mode
            self.timer = self.timer + 1
        if self.timer >= 10:
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
                    c.move(turn[0], turn[1])  # give the cube the direction
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
                        c.move(c.direction_x, c.direction_y)
            self.timer = 0

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
                        c.move(turn[0], turn[1])  # give the cube the direction
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
                            c.move(c.direction_x, c.direction_y)
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
                        c.move(turn[0], turn[1])  # give the cube the direction
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
                            c.move(c.direction_x, c.direction_y)
                self.timer = 0

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
                    c.move(turn[0], turn[1])  # give the cube the direction
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
                        c.move(c.direction_x, c.direction_y)
            self.timer = 0

    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.direction_x, tail.direction_y

        if len(self.body) == 1:
            if dx == 1 and dy == 0:  # add a body part to the right side of the snake based on the direction it's going
                self.body.append(cube.Cube((tail.pos[0] - 1, tail.pos[1]), self.color))
            elif dx == -1 and dy == 0:
                self.body.append(cube.Cube((tail.pos[0] + 1, tail.pos[1]), self.color))
            elif dx == 0 and dy == 1:
                self.body.append(cube.Cube((tail.pos[0], tail.pos[1] - 1), self.color))
            elif dx == 0 and dy == -1:
                self.body.append(cube.Cube((tail.pos[0], tail.pos[1] + 1), self.color))
        else:
            self.limit = self.limit - 1

        self.body[-1].direction_x = dx
        self.body[-1].direction_y = dy

    def draw(self, surface):  # draw red snake
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)  # true basically says draw the eyes

            else:
                c.draw(surface)
