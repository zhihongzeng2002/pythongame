import pygame, sys
from pygame.locals import QUIT
import time

speed = [1,1]
width, height = 800, 600
delay = 0.01
black = (0, 0, 0)

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
    
    screen.fill(black)
    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.blit(ball, ballrect)
    pygame.display.update()

    time.sleep(delay)
