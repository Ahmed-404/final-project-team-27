import pygame


class Cube(object):
    rows = 30
    w = 750

    def __init__(self, start, color):
        self.pos = start
        self.direction_x = 0
        self.direction_y = 0
        self.color = color

    def move(self, direction_x, direction_y):  # keep direction with the object
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.pos = (self.pos[0] + self.direction_x, self.pos[1] + self.direction_y)

    def draw(self, surface, eyes=False):  # draw the actual cubes
        dis = self.w // self.rows
        head_x = self.pos[0]
        head_y = self.pos[1]
        pygame.draw.rect(surface, self.color, (head_x * dis + 1, head_y * dis + 1, dis - 2, dis - 2))

        if eyes:  # draw eyes on the head
            centre = dis // 2.3
            radius = 3
            circle_middle = (head_x * dis + centre - radius, head_y * dis + 7)
            circle_middle2 = (head_x * dis + dis - radius * 2, head_y * dis + 7)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle, radius)  # left eye
            pygame.draw.circle(surface, (0, 0, 0), circle_middle2, radius)  # right eye
