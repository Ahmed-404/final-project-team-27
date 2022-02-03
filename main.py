"""""""""
Code made for the final project of AI & P, Creative Technology. This code has been written by Ahmed Mahran and Ferdy 
Sloot. The code has been made with inspiration of an online tutorial by freeCodeCamp.org
https://www.youtube.com/watch?v=XGf2GcyHPhc&t=5693s

The code consists of a main class with an update and main function, and an area class(draws the area), snake class
(handles the snake and it's movement, array of cube class), three ai classes (try to kill, trap or pressure the player)
and their respective cube classes(draws cubes and remembers their directions).
"""""""""
import snake
import cube_S
import area
import pygame
import ai
import ai1
import ai2
import random


def update(surface):  # update all values every loop
    global rows, width, s, snack
    surface.fill((205, 133, 63))
    s.draw_S(surface)  # update player snake position
    a.draw(surface)  # update red snake position
    a1.draw1(surface)  # update purple snake position
    a2.draw2(surface)  # update blue snake position
    snack.draw_S(surface)
    area.Area.draw_grid(width, rows, surface)
    pygame.display.update()


def main():
    global width, rows, s, a, a1, a2, snack
    width = 750
    rows = 30
    win = pygame.display.set_mode((width, 750))  # window
    s = snake.Snake((0, 255, 0), (10, 10))  # initialize player snake
    a = ai.Ai((80, 0, 255), (random.randrange(rows), random.randrange(rows)))  # initialize red snake
    a1 = ai1.Ai1((50, 20, 150), (random.randrange(rows), random.randrange(rows)))  # initialize purple snake
    a2 = ai2.Ai2((50, 0, 110), (random.randrange(rows), random.randrange(rows)))  # initialize blue snake
    snack = cube_S.Cube_S(area.Area.random_snack(rows, s), color=(255, 0, 0))  # first snack
    pygame.display.set_caption('SNAKE')

    while True:
        pygame.time.delay(50)  # otherwise code will get unreachable/game will get unplayable because of high speed
        s.move()  # move the player snake
        a.ai_move(s.body[0].pos[0], s.body[0].pos[1])  # move the red snake
        a1.ai1_move(s.body[0].pos[0], s.body[0].pos[1], snack.pos[0], snack.pos[1])  # move the purple
        a2.ai2_move(s.body[0].pos[0], s.body[0].pos[1])  # move the blue snake

        if s.body[0].pos == snack.pos:  # if player snake is at the snack's position
            s.add_cube_S()
            snack = cube_S.Cube_S(area.Area.random_snack(rows, s), color=(255, 0, 0))  # spawning snacks
        elif a1.body[0].pos == snack.pos:  # increase size of purple snake
            a1.add_cube1()  # increase size ai snake
            snack = cube_S.Cube_S(area.Area.random_snack(rows, s), color=(255, 0, 0))  # spawning snacks

        for x in range(len(s.body)):  # losing condition (When player snake touches an ai snake)
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])) or s.body[x].pos in list(
                    map(lambda z: z.pos, a.body[x:])) or s.body[x].pos in list(map(lambda z: z.pos, a1.body[x:])) or \
                    s.body[x].pos in list(map(lambda z: z.pos, a2.body[x:])):
                print('Game over')
                print('Time survived: ', s.in_game_time)
                print('Score: ', s.score)
                pygame.quit()

        update(win)  # update the window


main()
