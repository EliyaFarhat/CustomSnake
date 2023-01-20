

# modules
import pygame
import math
import sys
import time
import random

pygame.init()

# constants
SCREEN_H = 710
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLOCK = 25
SPEED = 0.6
TICK = 15
SIZE = 4


# initialize window
win = pygame.display.set_mode((SCREEN_H, SCREEN_H))
pygame.display.set_caption('Snake lol')

font_style = pygame.font.SysFont('Comic Sans', 25)

clock = pygame.time.Clock()


def scores(score):
    val = font_style.render("Score: " + str(score), True, (100, 100, 100))
    win.blit(val, [7,5])


def snake(BLOCK, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, GREEN, [x[0], x[1], BLOCK, BLOCK], 10)


def message(msg, colour):
    mesgDisplay = font_style.render(msg, True, colour)
    win.blit(mesgDisplay, [SCREEN_H/6, SCREEN_H/3])

def message2(msg, colour):
    mesDisplay = font_style.render(msg, True, colour)
    win.blit(mesDisplay, [SCREEN_H/5, SCREEN_H/2])


def gameLooping():
    game_over = False
    game_close = False

    playerX = SCREEN_H/2
    playerY = SCREEN_H/2

    pXChange = 0
    pYChange = 0

    snake_List = []
    snake_length = 1

    foodX = round(random.randrange(0, SCREEN_H - BLOCK) / BLOCK) * BLOCK
    foodY = round(random.randrange(0, SCREEN_H - BLOCK) / BLOCK) * BLOCK

    foodSX = round(random.randrange(0, SCREEN_H - BLOCK + 1) / BLOCK) * BLOCK
    foodSY = round(random.randrange(0, SCREEN_H - BLOCK + 1) / BLOCK) * BLOCK
    i = random.randint(0, 5)
    while not game_over:


        while game_close == True:
            win.fill((20,20,20))
            message("GAME OVER - R to Play Again - Q to Quit", RED)
            message2("HINT: Blue Food provides +3 length.", (0, 0, 255))
            scores(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLooping()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            # key events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pXChange = -BLOCK
                    pYChange = 0
                elif event.key == pygame.K_RIGHT:
                    pXChange = BLOCK
                    pYChange = 0
                elif event.key == pygame.K_UP:
                    pYChange = -BLOCK
                    pXChange = 0
                elif event.key == pygame.K_DOWN:
                    pYChange = BLOCK
                    pXChange = 0
        # coll detection
        if playerX >= SCREEN_H or playerX < 0 or playerY >= SCREEN_H or playerY < 0:
            game_close = True

        playerX += pXChange
        playerY += pYChange
        win.fill((0, 0, 0))
        # draw snake
        if i == 4:
            pygame.draw.circle(win, (0, 0, 255), [foodSX, foodSY], BLOCK / 2.5)
        pygame.draw.circle(win, RED, [foodX, foodY], BLOCK/2.5)
        snake_Head = []
        snake_Head.append(playerX)
        snake_Head.append(playerY)
        snake_List.append(snake_Head)
        if len(snake_List) > snake_length:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake(BLOCK, snake_List)
        scores(snake_length - 1)

        pygame.display.update()

        # fps

        if (playerX == foodX and playerY == foodY) or (foodX - BLOCK <= playerX <= foodX + BLOCK and foodY - BLOCK <= playerY <= foodY + BLOCK ):
            foodX = round(random.randrange(0, SCREEN_H - BLOCK) / BLOCK) * BLOCK
            foodY = round(random.randrange(0, SCREEN_H - BLOCK) / BLOCK) * BLOCK
            snake_length += 1
            i = random.randint(0, 5)
        if (playerX == foodSX and playerY == foodSY) or (foodSX - BLOCK <= playerX <= foodSX + BLOCK and foodSY - BLOCK <= playerY <= foodSY + BLOCK ):
            foodSX = round(random.randrange(0, SCREEN_H - BLOCK) / BLOCK) * BLOCK
            foodSY = round(random.randrange(0, SCREEN_H - BLOCK) / BLOCK) * BLOCK
            snake_length += 3
            i = random.randint(0, 5)
        clock.tick(TICK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    pygame.quit()
    quit()


gameLooping()
