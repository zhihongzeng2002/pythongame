# Zhihong (John)
# 3/22/2020

import pygame
from wormy_2021_func import *


def main():

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Wormy')

    # runGame_base(DISPLAYSURF, FPSCLOCK)

    while True:
        # runGame_apple_worm_update_multiple_apple(DISPLAYSURF, FPSCLOCK, 5)
        # run_game_camera_move_apple_worm(DISPLAYSURF, FPSCLOCK, 100)
        run_game_camera_move_apple_worm_image_optimization(DISPLAYSURF, FPSCLOCK, 100)
        showGameOverScreen(DISPLAYSURF)



if __name__ == '__main__':
    main()
