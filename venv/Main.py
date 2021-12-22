import random
import pygame
scrnw, scrnh = 480, 400
win = pygame.display.set_mode((scrnw, scrnh))

repeat = 0
repeat2 = 0
re = 0

x,  y = 100, 100
xv, yv = 20, 0

run = True

tsze = 20

score = 1
snake_tiles = [[x, y]]
fruit = [[200, 200]]

green = [0, 250, 0]
grey = [100, 100, 100]
red = [250, 0, 0]


def screen_draw(w, h):
    global repeat
    global repeat2
    global re
    repeat = 0
    repeat2 = 0
    while repeat < w:
        repeat2 = 0

        while repeat2 < h:
            if snake_tiles.__contains__([repeat, repeat2]):
                pygame.draw.rect(win, green, (repeat, repeat2, tsze, tsze))

            elif fruit.__contains__([repeat, repeat2]):
                pygame.draw.rect(win, red, (repeat, repeat2, tsze, tsze))

            else:
                pygame.draw.rect(win, grey, (repeat, repeat2, tsze, tsze))
            repeat2 += 20
            re += 1

        repeat += 20
        re += 1


while run:
    pygame.time.delay(80)

    win.fill((0, 0, 0))

    pygame.display.set_caption("Snake Game    Score: " + str(score))

    screen_draw(scrnw, scrnh)

    pygame.draw.rect(win, (0, 200, 0), (x, y, tsze, tsze))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        yv = -20
        xv = 0

    if keys[pygame.K_DOWN]:
        yv = 20
        xv = 0

    if keys[pygame.K_RIGHT]:
        xv = 20
        yv = 0

    if keys[pygame.K_LEFT]:
        xv = -20
        yv = 0

    x += xv
    y += yv

    if snake_tiles.__contains__([x, y]):
        run = False
        print("Good job! Your score was:", score)

    if x < 0 or x > scrnw:
        run = False
        print("Good job! Your score was:", score)

    if y < 0 or y > scrnh:
        run = False
        print("Good job! Your score was:", score)

    snake_tiles[0] = [x, y]
    snake_tiles.append([x, y])

    if fruit.__contains__(snake_tiles[0]):
        score += 1
        fruit[0] = [random.randint(0, scrnw/20 - 2) * 20, random.randint(0, scrnh/20 - 2) * 20]

    if len(snake_tiles) > (score + 1):
        snake_tiles.remove(snake_tiles[1])

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
