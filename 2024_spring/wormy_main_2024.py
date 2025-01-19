import pygame
import wormy_func_2024


def main():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    displaysurf = pygame.display.set_mode((wormy_func_2024.WINDOWWIDTH, wormy_func_2024.WINDOWHEIGHT))
    pygame.display.set_caption('Wormy')

    while True:
    # runGame_show_apple(displaysurf, FPSCLOCK)
        # runGame(displaysurf, FPSCLOCK)
        # runGame_multapple(displaysurf, FPSCLOCK)
        wormy_func_2024.runGame_moveCamera(displaysurf, FPSCLOCK)

        wormy_func_2024.showGameOverScreen(displaysurf)


if __name__ == '__main__':
    main()