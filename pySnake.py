import pygame
import random
from pygame.locals import *


pygame.init()
score = 0
max_score = score


def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10*10, y//10 * 10)

def collision(c1,c2):
    return (c1[0] == c2[0] and c1[1] == c2[1])

def change_direction(my_direction):
    for i in range(len(snake)-1,0,-1):
       snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1]-10)
    
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1]+10)

    if my_direction == LEFT:
        snake[0] = (snake[0][0]-10, snake[0][1])

    if my_direction == RIGHT:
        snake[0] = (snake[0][0]+10, snake[0][1])

def check_boundaries(snake, score, max_score):
    if snake[0][0] == 600 or snake[0][0] == 0 or snake[0][1] == 600 or snake[0][1] == 0:    
        snake =   [(200,200),(210,200),(220,200)]
        if score > max_score:
            max_score = score
        score = 0



UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3



myfont = pygame.font.SysFont("monospace", 16)
WHITE = (255,255,255)


snake = [(200,200),(210,200),(220,200)]
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

apple = pygame.Surface((10,10))
apple.fill((255,0,0))
apple_pos = on_grid_random()
my_direction = -1

clock = pygame.time.Clock()
while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                if my_direction != DOWN:
                    my_direction = UP
            if event.key == K_DOWN:
                if my_direction != UP:
                    my_direction = DOWN
            if event.key == K_RIGHT:
                if my_direction != LEFT:
                    my_direction = RIGHT
            if event.key == K_LEFT:
                if my_direction != RIGHT:
                    my_direction = LEFT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1
    
    for pos in snake[1:]:
        if snake[0][0] == pos[0] and snake[0][1] == pos[1]:
            snake =  [(200,200),(210,200),(220,200)]
            if score > max_score:
                max_score = score
            score = 0

    if snake[0][0] == 600 or snake[0][0] == 0 or snake[0][1] == 600 or snake[0][1] == 0:    
        snake =   [(200,200),(210,200),(220,200)]
        if score > max_score:
            max_score = score
        score = 0
    change_direction(my_direction)
 

    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin,pos)

    scoretext = myfont.render("score", 1, (255,255,255))
    maxscoretext = myfont.render("max" , 1, (255,255,255))

    scorevalue = myfont.render(str(score),1,(255,255,255))
    maxscorevalue = myfont.render(str(max_score),1,(255,255,255))

    screen.blit(scoretext, (500, 10))
    screen.blit(maxscoretext, (500, 20))

    screen.blit(scorevalue,(560,10))
    screen.blit(maxscorevalue,(560,20))
    
    pygame.display.update()
