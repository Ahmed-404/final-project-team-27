import pygame
import random


class Area:
    def draw_grid(w, rows, surface):  # draw the visible grid
        size_between = w // rows

        x = 0
        y = 0
        for l in range(rows):
            x = x + size_between
            y = y + size_between

            pygame.draw.line(surface, (180, 133, 63), (x, 0), (x, w))
            pygame.draw.line(surface, (180, 133, 63), (0, y), (w, y))

    def random_snack(rows, item):  # calculate where the snack needs to spawn
        positions = item.body

        while True:
            x = random.randrange(rows)
            y = random.randrange(rows)
            if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0: # take every value of grid, filter out
                # snake's coordinates
                continue
            else:
                break

        return x, y # pass the coordinates

