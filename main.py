"""""""""
Code made for the final project of AI & P, Creative Technology. This code has been written by Ahmed Mahran and Ferdy 
Sloot. The code has been made with inspiration of an online tutorial by freeCodeCamp.org
https://www.youtube.com/watch?v=XGf2GcyHPhc&t=5693s

The code consists of a main class with an update and main function, and an area class(draws the area), snake class
(handles the snake and it's movement, array of cube class) and a cube class(draws cubes and remembers their directions).
"""""""""

import snake
import cube
import area
import pygame


def update(surface):  # update all values every loop
    global rows, width, s, snack
    surface.fill((205, 133, 63))
    s.draw(surface)
    snack.draw(surface)
    area.Area.draw_grid(width, rows, surface)
    pygame.display.update()


def main():
    global width, rows, s, snack
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, 500))  # window
    s = snake.Snake((0, 255, 0), (10, 10))
    snack = cube.Cube(area.Area.random_snack(rows, s), color=(255, 0, 0))  # first snack

    while True:
        pygame.time.delay(50)  # Otherwise code will get unreachable/game will get unplayable because of high speed

        s.move()
        if s.body[0].pos == snack.pos:
            s.add_cube()
            snack = cube.Cube(area.Area.random_snack(rows, s), color=(255, 0, 0))  # spawning snacks

        for x in range(len(s.body)):  # losing condition
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                print('Game over')

        update(win)

    pass


main()
