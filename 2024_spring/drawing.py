import pygame, sys
from pygame.locals import QUIT

width, height = 800, 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("This is a surface")

screen.fill(white)

pygame.draw.rect(screen, red, (500, 300, 100, 50), 0)
pygame.draw.rect(screen, green, (600, 250, 100, 50), 5)

pygame.draw.polygon(screen, blue, ((146, 0), (291, 106), (236, 277),\
                                   (56, 277), (0, 106)))

pygame.draw.line(screen, black, (687, 500), (745, 500))
pygame.draw.line(screen, black, (700, 300), (745, 500))
pygame.draw.line(screen, black, (400, 300), (231, 333), 10)

pygame.draw.circle(screen, red, (300, 50), 20, 0)
pygame.draw.circle(screen, red, (400, 150), 50, 5)

pygame.draw.ellipse(screen, green, (200, 400, 10, 50), 5)

pixObj = pygame.PixelArray(screen)
pixObj[500][100] = red
pixObj[500][120] = red
pixObj[500][140] = red

pixObj[400][100] = blue
pixObj[400][120] = blue
pixObj[400][140] = blue

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
