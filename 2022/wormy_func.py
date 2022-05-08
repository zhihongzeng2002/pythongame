import random, pygame, sys
from pygame.locals import QUIT, KEYUP, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN

FPS = 5
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
CELLWIDTH = int(WINDOWWIDTH/ CELLSIZE)
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

class Worm(object):
    def __init__(self, cell_width, cell_height, cell_size):
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.cell_size = cell_size
        self.direction = RIGHT

        margin = 5
        startx = random.randint(margin, cell_width - margin)
        starty = random.randint(margin, cell_height - margin)
        self.Coords = [{'x': startx, 'y': starty}, {'x': startx - 1, 'y':starty}, {'x': startx - 2, 'y':starty}]

    def draw(self, DISPLAYSURF):
        for coord in self.Coords:
            x = coord['x'] * self.cell_size
            y = coord['y'] * self.cell_size
            wormSegmentRect = pygame.Rect(x, y, self.cell_size, self.cell_size)
            pygame.draw.rect(DISPLAYSURF, DARKGREEN, wormSegmentRect)

            wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, self.cell_size - 8, self.cell_size - 8)
            pygame.draw.rect(DISPLAYSURF, GREEN, wormInnerSegmentRect)

    def change_direction(self, direction):
        if (direction in [UP, DOWN] and self.direction in \
            [LEFT, RIGHT]) or (direction in [LEFT, RIGHT] \
                and self.direction in [UP, DOWN]):
            self.direction = direction

    def update(self):
        if self.direction == UP:
            newHead = {'x': self.Coords[HEAD]['x'], 'y': self.Coords[HEAD]['y']-1}
        if self.direction == DOWN:
            newHead = {'x': self.Coords[HEAD]['x'], 'y': self.Coords[HEAD]['y']+1}
        if self.direction == LEFT:
            newHead = {'x': self.Coords[HEAD]['x']-1, 'y': self.Coords[HEAD]['y']}
        if self.direction == RIGHT:
            newHead = {'x': self.Coords[HEAD]['x']+1, 'y': self.Coords[HEAD]['y']}

        self.Coords.insert(0, newHead) 

    def remove_tail(self):
        del self.Coords[-1]   

    def update_remove_tail(self):
        self.update()
        self.remove_tail()

    def hit_edge(self):
        if self.Coords[HEAD]['x'] < 0 or self.Coords[HEAD]['x'] >= self.cell_width or self.Coords[HEAD]['y'] < 0 or self.Coords[HEAD]['y'] >= self.cell_height:
            return True
        else:
            return False
    
    def hit_self(self):
        if self.Coords[HEAD] in self.Coords[1:]:
            return True
        else:
            return False

class Apple(object):
    def __init__(self, cell_width, cell_height, cell_size):
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.cell_size = cell_size
        self.update()
    
    def draw(self, DISPLAYSURF):
        x = self.Coord['x'] * self.cell_size
        y = self.Coord['y'] * self.cell_size
        appleRect = pygame.Rect(x, y, self.cell_size,\
            self.cell_size)
        pygame.draw.rect(DISPLAYSURF, RED, appleRect)

    def update(self):
        self.Coord = \
        {'x': random.randint(0, self.cell_width - 1), \
        'y': random.randint(0, self.cell_height - 1)}

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

def showGameOverScreen_base(DISPLAYSURF):
    gameOverFont = pygame.font.Font(pygame.font.get_default_font(), 100)
    gameSurf = gameOverFont.render('Game Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    gameRect.midtop = (int(WINDOWWIDTH / 2), (int(WINDOWHEIGHT / 2)-50))
    DISPLAYSURF.blit(gameSurf, gameRect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYUP:
                return

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

def runGame_Apple(DISPLAYSURF, FPSCLOCK):
    score = 0
    apple = Apple(CELLWIDTH, CELLHEIGHT, CELLSIZE)

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
                else:
                    apple.update()
        
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid(DISPLAYSURF)
        drawScore(score, DISPLAYSURF)
        apple.draw(DISPLAYSURF)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def runGame_Apple_Worm(DISPLAYSURF, FPSCLOCK):
    score = 0
    apple = Apple(CELLWIDTH, CELLHEIGHT, CELLSIZE)
    worm = Worm(CELLWIDTH, CELLHEIGHT, CELLSIZE)

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
                else:
                    apple.update()
        
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid(DISPLAYSURF)
        drawScore(score, DISPLAYSURF)
        apple.draw(DISPLAYSURF)
        worm.draw(DISPLAYSURF)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def runGame_Apple_Worm_update(DISPLAYSURF, FPSCLOCK):
    score = 0
    apple = Apple(CELLWIDTH, CELLHEIGHT, CELLSIZE)
    worm = Worm(CELLWIDTH, CELLHEIGHT, CELLSIZE)

    while True:
        if worm.hit_edge() or worm.hit_self():
            return

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    worm.change_direction(LEFT)
                elif event.key == K_RIGHT:
                    worm.change_direction(RIGHT)
                elif event.key == K_UP:
                    worm.change_direction(UP)
                elif event.key == K_DOWN:
                    worm.change_direction(DOWN)
        
        worm.update()

        if worm.Coords[HEAD] == apple.Coord:
            score += 1
            apple.update()
        else:
            worm.remove_tail()

        DISPLAYSURF.fill(BGCOLOR)
        drawGrid(DISPLAYSURF)
        drawScore(score, DISPLAYSURF)
        apple.draw(DISPLAYSURF)
        worm.draw(DISPLAYSURF)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def runGame_Multi_apple(DISPLAYSURF, FPSCLOCK, num_apples):
    score = 0
    apples = [Apple(CELLWIDTH, CELLHEIGHT, CELLSIZE) \
        for i in range(num_apples)]
    worm = Worm(CELLWIDTH, CELLHEIGHT, CELLSIZE)

    while True:
        if len(apples) < num_apples:
            apples.append(Apple(CELLWIDTH, CELLHEIGHT, CELLSIZE))

        if worm.hit_edge() or worm.hit_self():
            return

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    worm.change_direction(LEFT)
                elif event.key == K_RIGHT:
                    worm.change_direction(RIGHT)
                elif event.key == K_UP:
                    worm.change_direction(UP)
                elif event.key == K_DOWN:
                    worm.change_direction(DOWN)
        
        worm.update()

        apple_bite = False
        for i in range(len(apples) - 1, -1, -1):
            apple = apples[i]
            if worm.Coords[HEAD] == apple.Coord:
                del apples[i]
                apple_bite = True
                break
        if not apple_bite:
            worm.remove_tail()

        DISPLAYSURF.fill(BGCOLOR)
        drawGrid(DISPLAYSURF)
        drawScore(len(worm.Coords) - 3, DISPLAYSURF)
        worm.draw(DISPLAYSURF)

        for apple in apples:
            apple.draw(DISPLAYSURF)

        pygame.display.update()
        FPSCLOCK.tick(FPS)