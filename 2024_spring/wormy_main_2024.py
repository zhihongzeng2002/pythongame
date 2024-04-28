import pygame
from wormy_func_2024 import *


def main():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    displaysurf = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Wormy')

    while True:
    # runGame_show_apple(displaysurf, FPSCLOCK)
        runGame(displaysurf, FPSCLOCK)

        showGameOverScreen(displaysurf)


if __name__ == '__main__':
    main()