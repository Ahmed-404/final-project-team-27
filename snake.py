import pygame
import cube_S
import speechrecognition


class Snake(object):
    body = []  # list with amount of body parts
    turns = {}  # dictionary with te turn state of each body part

    def __init__(self, color, pos):  # constructor
        self.color = color
        self.head = cube_S.Cube_S(pos)
        self.body.append(self.head)
        self.direction = None
        self.direction_x = 0
        self.direction_y = 1
        self.src = speechrecognition.SpeechRecognition()
        self.timer = 40
        self.iter_val = 10
        self.score = 0
        self.in_game_time = 0

    def move(self):  # move the snake and change its speed
        self.timer = self.timer + self.iter_val
        self.in_game_time = self.in_game_time + 1
        if self.src.speech() == "fast":  # increase speed snake
            self.iter_val = self. iter_val + 10
            print('going faster!')
        if self.src.speech() == "slow":  # decrease speed snake
            self.iter_val = self.iter_val - 10
            print('Slowing down!')
        if self.src.speech() == "quit":  # close the game
            pygame.quit()

        if self.timer >= 30:  # speed limit on player snake
            self.timer = 0
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
                    c.move_S(turn[0], turn[1])  # give the cube the direction
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
                        c.move_S(c.direction_x, c.direction_y)

    def add_cube_S(self):
        tail = self.body[-1]  # in order to not let a body part spawn in the head
        dx, dy = tail.direction_x, tail.direction_y

        if dx == 1 and dy == 0:  # add a body part to the right side of the snake based on the direction it's going
            self.body.append(cube_S.Cube_S((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube_S.Cube_S((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube_S.Cube_S((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube_S.Cube_S((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].direction_x = dx
        self.body[-1].direction_y = dy
        self.score = self.score + 1

    def draw_S(self, surface):  # draw player snake
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw_S(surface, True)  # true basically says draw the eyes
            else:
                c.draw_S(surface)

