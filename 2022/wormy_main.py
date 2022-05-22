import pygame
from wormy_func import *

def main():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Wormy')

    #runGame_base(DISPLAYSURF, FPSCLOCK)
    #runGame_1(DISPLAYSURF, FPSCLOCK)
    #runGame_Apple(DISPLAYSURF, FPSCLOCK)
    # runGame_Apple_Worm(DISPLAYSURF, FPSCLOCK)

    while True:
        #runGame_Apple_Worm_update(DISPLAYSURF, FPSCLOCK)
        #runGame_Multi_apple(DISPLAYSURF, FPSCLOCK, 10)
        runGame_camera_move(DISPLAYSURF, FPSCLOCK, 100)
        showGameOverScreen_base(DISPLAYSURF)

if __name__ == '__main__':
    main()