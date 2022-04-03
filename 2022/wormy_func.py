import random, pygame, sys
from pygame.locals import QUIT, KEYUP, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN

FPS = 5
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
CELLWIDTH = int(WINDOWHEIGHT / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)
YELLOW = (255, 255, 0)
DARKYELLOW = (155, 155, 0)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0

def terminate():
    pygame.quit()
    sys.exit()

def drawScore(score, DISPLAYSURF):
    BASICFONT = pygame.font.Font(pygame.font.get_default_font(), 18)
    scoreSurf = BASICFONT.render(f'score: {score}', True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

def drawGrid(DISPLAYSURF):
    for x in range(0, WINDOWWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    
    for y in range(0, WINDOWHEIGHT, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))

def runGame_base(DISPLAYSURF, FPSCLOCK):
    score = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                score += 1
        #print(score)
        
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid(DISPLAYSURF)
        drawScore(score, DISPLAYSURF)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def runGame_1(DISPLAYSURF, FPSCLOCK):
    score = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    score -= 1
                elif event.key == K_RIGHT:
                    score += 1
                elif event.key == K_UP:
                    score += 10
                elif event.key == K_DOWN:
                    score -= 10
        
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid(DISPLAYSURF)
        drawScore(score, DISPLAYSURF)
        pygame.display.update()
        FPSCLOCK.tick(FPS)