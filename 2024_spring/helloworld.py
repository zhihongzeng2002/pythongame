import pygame, sys
from pygame.locals import QUIT

speed = [1,1]
width, height = 800, 600

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("This is a surface")

ball = pygame.image.load('831.png')
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(ball, ballrect)
    pygame.display.update()
