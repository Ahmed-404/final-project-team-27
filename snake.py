import pygame
import cube
from pygame.locals import *


class Snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):  # constructor
        self.color = color
        self.head = cube.Cube(pos)
        self.body.append(self.head)
        self.direction = None
        self.direction_x = 0
        self.direction_y = 1

    def move(self):  # move the snake

        pygame.joystick.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
            for joystick in joysticks:
                print(joystick.get_name())

            if event.type == JOYBUTTONDOWN:  # when an input is given and it's pressing a button:
                print(event.button)
                self.direction = event.button  # make the button the direction the cube will go in

                keys = pygame.key.get_pressed()  # trash code
                for key in keys:  # what direction the snake needs to move in when the dance mat is used
                    if self.direction == 2:
                        self.direction_x = -1
                        self.direction_y = 0
                        self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]

                    elif self.direction == 3:
                        self.direction_x = 1
                        self.direction_y = 0
                        self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]

                    elif self.direction == 0:
                        self.direction_x = 0
                        self.direction_y = -1
                        self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]

                    elif self.direction == 1:
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

    # def ai_move(self, snack_x, snack_y):  # move the ai snake
    #     if snack_x < self.body[0].pos[0] and snack_x - self.body[0].pos[0] != 2:  # if the snack position is to the left of the snake's head
    #         self.direction_x = -1
    #         self.direction_y = 0
    #         self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]
    #     else:
    #         self.direction_x = 1
    #         self.direction_y = 0
    #         self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]
    #
    #     if snack_y < self.body[0].pos[1] and snack_y - self.body[0].pos[1] != 2:  # if the snack position is above the snake's head
    #         self.direction_x = 0
    #         self.direction_y = -1
    #         self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]
    #     else:
    #         self.direction_x = 0
    #         self.direction_y = 1
    #         self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]
    #
    #     for i, c in enumerate(self.body):  # get index and cube in self.body
    #         p = c.pos[:]  # all cube objects have a position
    #         if p in self.turns:  # check if position is in turn list
    #             turn = self.turns[p]
    #             c.move(turn[0], turn[1])  # give the cube the direction
    #             if i == len(self.body) - 1:  # if the last cube of the snake is in the turn, remove the turn
    #                 self.turns.pop(p)
    #
    #         else:  # check if the edge of the screen is reached, if yes, teleport to the other side
    #             if c.direction_x == -1 and c.pos[0] <= 0:
    #                 c.pos = (c.rows - 1, c.pos[1])
    #             elif c.direction_x == 1 and c.pos[0] >= c.rows - 1:
    #                 c.pos = (0, c.pos[1])
    #             elif c.direction_y == 1 and c.pos[1] >= c.rows - 1:
    #                 c.pos = (c.pos[0], 0)
    #             elif c.direction_y == -1 and c.pos[1] <= 0:
    #                 c.pos = (c.pos[0], c.rows - 1)
    #             else:
    #                 c.move(c.direction_x, c.direction_y)

    def reset(self, pos):
        self.head = cube.Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.direction_x = 0
        self.direction_y = 1

    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.direction_x, tail.direction_y

        if dx == 1 and dy == 0:
            self.body.append(cube.Cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube.Cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube.Cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube.Cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].direction_x = dx
        self.body[-1].direction_y = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)  # true basically says draw the eyes
            else:
                c.draw(surface)
