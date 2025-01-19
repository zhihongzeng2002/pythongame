import random, pygame, sys, time
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_UP, K_DOWN

FPS = 5
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
CELLWIDTH = int(WINDOWWIDTH/CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT/CELLSIZE)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)
YELLOW = (255, 255, 0)
DARKYELLOW = (155, 155, 0)

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

def terminate():
    pygame.quit()
    sys.exit()

def drawGrid(DISPLAYSURF):
    for x in range(0, WINDOWWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))

def drawScore(score, DISPLAYSURF):
    BASICFONT = pygame.font.Font(pygame.font.get_default_font(), 18)
    scoreSurf = BASICFONT.render(f'Score: {score}', True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

def showGameOverScreen (DISPLAYSURF):
    gameOverFont = pygame.font.Font(pygame.font.get_default_font(), 100)
    gameSurf = gameOverFont.render(f'Game Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    gameRect.midtop = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) - 50)
    DISPLAYSURF.blit(gameSurf, gameRect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYUP:
                return

class Apple(object):
    def __init__(self, cell_width, cell_height, cell_size):
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.cell_size = cell_size
        self.update()
        
    def draw(self, DISPLAYSURF):
        x = self.Coord['x'] * self.cell_size
        y = self.Coord['y'] * self.cell_size
        appleRect = pygame.Rect(x, y, self.cell_size, self.cell_size)
        pygame.draw.rect(DISPLAYSURF, RED, appleRect)

    def update(self): 
        self.Coord = {'x': random.randint(0, self.cell_width -1), \
                      'y': random.randint(0, self.cell_height-1)}

class Apple_move(Apple):
    def update(self): 
        self.Coord = {'x': random.randint(-self.cell_width, \
                                          2 * self.cell_width -1), \
                      'y': random.randint(-self.cell_height, \
                                          2 * self.cell_height-1)}
    
    def adjust_coord(self, adjust_x, adjust_y):
        self.Coord['x'] -= adjust_x
        self.Coord['y'] -= adjust_y
    
    def inside_camera(self, camera):
        if self.Coord['x'] >= camera['left'] and self.Coord['x'] < camera['right'] \
            and self.Coord['y'] >= camera['bottom'] and self.Coord['y'] < \
            camera['top']:
            return True
        return False

class Worm(object):
    def __init__(self, cell_width, cell_height, cell_size):
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.cell_size = cell_size
        self.direction = RIGHT
        margin = 5
        startx = random.randint(margin, cell_width - margin)
        starty = random.randint(margin, cell_height - margin)
        self.Coords = [{'x': startx, 'y': starty}, 
                       {'x': startx-1, 'y': starty}, 
                       {'x': startx-2, 'y': starty}]     
        
    def draw(self, DISPLAYSURF):
        for coord in self.Coords:
            x = coord['x'] * self.cell_size
            y = coord['y'] * self.cell_size
            wormSegmentRect = pygame.Rect(x, y, self.cell_size, self.cell_size)
            pygame.draw.rect(DISPLAYSURF, DARKGREEN, wormSegmentRect)
            wormInnerSegmentRect = pygame.Rect(x+4, y+4, self.cell_size-8, self.cell_size-8)
            pygame.draw.rect(DISPLAYSURF, GREEN, wormInnerSegmentRect)
     
    def update(self):
        if (self.direction == UP):
            newHead = {'x': self.Coords[0]['x'], 'y': self.Coords[0]['y'] - 1}
        elif (self.direction == DOWN):
            newHead = {'x': self.Coords[0]['x'], 'y': self.Coords[0]['y'] + 1}
        elif (self.direction == LEFT):
            newHead = {'x': self.Coords[0]['x'] - 1, 'y': self.Coords[0]['y']}
        elif (self.direction == RIGHT):
            newHead = {'x': self.Coords[0]['x'] + 1, 'y': self.Coords[0]['y']}

        self.Coords.insert(0, newHead)
    
    def remove_tail(self):
        del self.Coords[-1]
    
    def hit_self(self):
        if self.Coords[0] in self.Coords[1:]:
            return True
        else:
            return False
        
    def hit_edge(self):
        if self.Coords[0]['x'] == -1\
            or self.Coords[0]['x'] == self.cell_width \
            or self.Coords[0]['y'] == -1 \
            or self.Coords[0]['y'] == self.cell_height:
            return True
        else:
            return False

    def change_direction(self, direction):
        if (direction in [UP, DOWN] and self.direction in [LEFT, RIGHT]) \
        or (direction in [LEFT, RIGHT] and self.direction in [UP, DOWN]):
            self.direction = direction

class Worm_move(Worm):
    def __init__(self, cell_width, cell_height, cell_size, slack):
        super().__init__(cell_width, cell_height, cell_size)
        self.slack = slack
        self.adjust_coord(0, 0)

    def adjust_coord(self, adjust_x, adjust_y):
        for i in range(len(self.Coords)):
            self.Coords[i]['x'] -= adjust_x
            self.Coords[i]['y'] -= adjust_y
    
    def calc_adjust_coord(self):
        def calc_adjust(header, camera_center, slack):
            adjust = 0
            dist = header - camera_center
            if abs(dist) > slack:
                adjust = abs(dist) - slack
            return adjust if dist > 0 else -adjust
        
        adjust_x = calc_adjust(self.Coords[0]['x'], \
                               int(self.cell_width / 2), self.slack)
        adjust_y = calc_adjust(self.Coords[0]['y'], \
                               int(self.cell_height / 2), self.slack)
        self.adjust_coord(adjust_x, adjust_y)

        return adjust_x, adjust_y
    
    def update_eat_apple(self, apples):
        self.update()

        apple_bite = False
        for i in range(len(apples) - 1, -1, -1):
            apple = apples[i]
            if self.Coords[0] == apple.Coord:
                apple_bite = True
                del apples[i]
                break
        if apple_bite == False:
            self.remove_tail()
    
    def change_direction_update (self, direction, apples):
        self.change_direction(direction)
        self.update_eat_apple(apples)
        return self.calc_adjust_coord()

def runGame_base(DISPLAYSURF, FPSCLOCK):
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
        
        DISPLAYSURF.fill(BLACK)

        drawGrid(DISPLAYSURF)
        drawScore(score, DISPLAYSURF)
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def runGame_show_apple(DISPLAYSURF, FPSCLOCK):
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
        
        DISPLAYSURF.fill(BLACK)

        drawGrid(DISPLAYSURF)
        drawScore(score, DISPLAYSURF)
        apple.draw(DISPLAYSURF)
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def runGame_show_worm(DISPLAYSURF, FPSCLOCK):
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
        
        DISPLAYSURF.fill(BLACK)

        drawGrid(DISPLAYSURF)
        drawScore(score, DISPLAYSURF)
        apple.draw(DISPLAYSURF)
        worm.draw(DISPLAYSURF)
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def runGame(DISPLAYSURF, FPSCLOCK):
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

        if worm.Coords[0] == apple.Coord:
            apple.update()
        else:
            worm.remove_tail()
        
        DISPLAYSURF.fill(BLACK)

        drawGrid(DISPLAYSURF)
        drawScore(score, DISPLAYSURF)
        apple.draw(DISPLAYSURF)
        worm.draw(DISPLAYSURF)
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def runGame_multapple(DISPLAYSURF, FPSCLOCK):
    score = 0
    apples = [Apple(CELLWIDTH, CELLHEIGHT, CELLSIZE) for i in range(10)]
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

        apple_bite = False
        for i in range(len(apples) - 1, -1, -1):
            apple = apples[i]
            if worm.Coords[0] == apple.Coord:
                apple_bite = True
                del apples[i]
                break
        if apple_bite == False:
            worm.remove_tail()
        
        DISPLAYSURF.fill(BLACK)

        drawGrid(DISPLAYSURF)
        drawScore(score, DISPLAYSURF)

        for apple in apples:
            apple.draw(DISPLAYSURF)

        worm.draw(DISPLAYSURF)
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def runGame_moveCamera(DISPLAYSURF, FPSCLOCK):
    slack = 8
    score = 0
    numApples = 50

    apples = [Apple_move(CELLWIDTH, CELLHEIGHT, CELLSIZE) for i in range(numApples)]
    worm = Worm_move(CELLWIDTH, CELLHEIGHT, CELLSIZE, slack)
    #changed to subclass

    camera = {'left':0, 'right': CELLWIDTH, 'top':0, 'bottom': CELLHEIGHT}
    while True:
        adjust_x, adjust_y = 0, 0

        while (len(apples) < numApples):
            apple = Apple_move(CELLWIDTH, CELLHEIGHT, CELLSIZE)
            if not apple.inside_camera(camera):
                apples.append(apple) #check if inside camera

        if worm.hit_edge() or worm.hit_self():
            return
        
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN: #changed to adjustx, adjudty
                if event.key == K_LEFT:
                    adjust_x, adjust_y = \
                        worm.change_direction_update(LEFT, apples)
                elif event.key == K_RIGHT:
                    adjust_x, adjust_y = \
                        worm.change_direction_update(RIGHT, apples)
                elif event.key == K_UP:
                    adjust_x, adjust_y = \
                        worm.change_direction_update(UP, apples)
                elif event.key == K_DOWN:
                    adjust_x, adjust_y = \
                        worm.change_direction_update(DOWN, apples)
        
        DISPLAYSURF.fill(BLACK)

        drawGrid(DISPLAYSURF)
        drawScore(score, DISPLAYSURF)

        for apple in apples:
            apple.adjust_coord(adjust_x, adjust_y)
            apple.draw(DISPLAYSURF) #updated all coords of apples

        worm.draw(DISPLAYSURF)
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)