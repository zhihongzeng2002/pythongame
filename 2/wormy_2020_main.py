# Zhihong (John)
# 3/22/2020

import pygame
from wormy_2020_func import *


def main():

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Wormy')

##    runGame_base(DISPLAYSURF, FPSCLOCK)
##    runGame_1(DISPLAYSURF, FPSCLOCK)
##    runGame_show_apple(DISPLAYSURF, FPSCLOCK)
##    runGame_show_worm(DISPLAYSURF, FPSCLOCK)
##    showGameOverScreen_base(DISPLAYSURF)

    while True:
        # runGame(DISPLAYSURF, FPSCLOCK)
        # runGame_multi_apple(DISPLAYSURF, FPSCLOCK, 10)
        runGame_camera_move(DISPLAYSURF, FPSCLOCK, 100)
        showGameOverScreen(DISPLAYSURF)


if __name__ == '__main__':
    main()
