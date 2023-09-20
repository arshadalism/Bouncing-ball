import pygame
import random

pygame.init()

width, height = 700, 550

clock = pygame.time.Clock()

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bouncy_ball')

ball_X = width/2 - 12
ball_Y = height/2 - 12
ball_XChange = 3 * random.choice((1, -1))
ball_YChange = 3
ballPixel = 24

running = True
while running:
    screen.fill(red)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if ball_X + ballPixel >= width or ball_X <= 0:
        ball_XChange *= -1
    if ball_Y + ballPixel >= height or ball_Y <= 0:
        ball_YChange *= -1

    ball_X += ball_XChange
    ball_Y += ball_YChange

    balling = pygame.draw.circle(screen, (0, 0, 255),(int(ball_X), int(ball_Y)), 15)
    pygame.display.update()
    clock.tick(100)

pygame.quit()
