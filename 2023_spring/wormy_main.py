import pygame
from wormy_function import *

def main():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Wormy")

    # runGame_base(DISPLAYSURF, FPSCLOCK)
    # runGame_1(DISPLAYSURF, FPSCLOCK)
    # runGame_apple(DISPLAYSURF, FPSCLOCK)
    while True:
        # runGame_wormMove(DISPLAYSURF, FPSCLOCK)
        # runGame_multiApple(DISPLAYSURF, FPSCLOCK, 10)
        # runGame_moveCamera(DISPLAYSURF, FPSCLOCK, 100)
        # runGame_enemyWorm(DISPLAYSURF, FPSCLOCK, 100, 20)
        runGame_enemyHit(DISPLAYSURF, FPSCLOCK, 100, 20)

        showGameOverScreen(DISPLAYSURF)

if __name__ == '__main__':
    main()