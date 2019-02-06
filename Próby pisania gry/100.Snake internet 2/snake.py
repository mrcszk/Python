#!/usr/bin/env python
import pygame, sys, random, time
from pygame.locals import *

PIXEL_SIZE = (15, 15)
PIXELS_IN_WIDTH = 40
PIXELS_IN_HEIGHT = 30
MENU_HEIGHT = 30
pygame.init()
screen = pygame.display.set_mode((PIXEL_SIZE[0] * PIXELS_IN_WIDTH, PIXEL_SIZE[1] * PIXELS_IN_HEIGHT + MENU_HEIGHT),
                                 HWSURFACE)
pygame.display.set_caption("Snake!")


class ScoreBoard(pygame.Surface):
    def __init__(self):
        super(ScoreBoard, self).__init__((screen.get_size()[0], MENU_HEIGHT))
        self.font = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.score = 0

    def incrementScore(self):
        self.score = self.score + 1

    def draw(self):
        img = self.font.render("SCORE: " + str(self.score), 1, (0, 0, 255))
        self.blit(img, (0, 0))

    def update(self):
        self.fill((0, 0, 0))
        self.draw()


class Background(pygame.Surface):
    def __init__(self, size):
        super(Background, self).__init__(size, pygame.SRCALPHA, 32)
        self.font = pygame.font.Font(pygame.font.get_default_font(), 15)
        self.img = self.font.render("#", 1, (255, 0, 0))
        self.img = pygame.transform.scale(self.img, (15, 15))
        self.prepare()

    def prepare(self):
        for i in range(PIXELS_IN_WIDTH):
            self.blit(self.img, (PIXEL_SIZE[0] * i, 0))
            self.blit(self.img, (PIXEL_SIZE[0] * i, PIXEL_SIZE[1] * (PIXELS_IN_HEIGHT - 1)))
        for i in range(PIXELS_IN_HEIGHT):
            self.blit(self.img, (0, PIXEL_SIZE[1] * i))
            self.blit(self.img, (PIXEL_SIZE[0] * (PIXELS_IN_WIDTH - 1), PIXEL_SIZE[1] * i))


class Apple(pygame.Surface):
    '''Controls creation of apples, scoreboard and the snake'''

    def __init__(self, size, snake, board):
        super(Apple, self).__init__(size, SRCALPHA, 32)
        self.snake = snake
        self.apple = pygame.font.Font(pygame.font.get_default_font(), 15).render('&', 1, (0, 255, 0))
        self.board = board
        self.board.update()

        self.apples = []

    def update(self):
        '''Add apple if needed'''
        if len(self.apples) == 0:
            x = range(1, PIXELS_IN_WIDTH - 1)
            y = range(1, PIXELS_IN_HEIGHT - 1)
            new_apple = (random.choice(x), random.choice(y))
            while True:
                do_break = True
                for part in self.snake.parts:
                    if part[1] == new_apple:
                        do_break = False
                if do_break:
                    break
                else:
                    new_apple = random.choice(x), random.choice(y)
            self.apples.append(new_apple)
        else:
            if self.snake.parts[0][1] == self.apples[0]:
                self.apples = []
                self.snake.append_body()
                self.board.incrementScore()
                self.board.update()

        self.draw()

    def draw(self):
        self.fill((0, 0, 0))
        self.blit(self.snake, (0, 0))
        for apple in self.apples:
            self.blit(self.apple, (apple[0] * PIXEL_SIZE[0], apple[1] * PIXEL_SIZE[1]))


class Snake(pygame.Surface):
    '''All parts are stored in list of tuples like this - (type_of_part, coordinates)
    for example: ('head', (10,20)) , part can be 'rest' or 'head'
    parts are stored self.parts
    '''

    def __init__(self, size):
        super(Snake, self).__init__(size)
        self.dt = 0
        self.font = pygame.font.Font(pygame.font.get_default_font(), 15)
        self.head = pygame.transform.scale(self.font.render("@", 1, (255, 0, 0)), PIXEL_SIZE)
        self.rest = pygame.transform.scale(self.font.render("#", 1, (0, 255, 0)), PIXEL_SIZE)

        self.DIRECTION = "UP"
        self.parts = [("head", (PIXELS_IN_WIDTH // 2, PIXELS_IN_HEIGHT // 2))]
        for i in range(1, 2):
            self.parts.append(("rest", (PIXELS_IN_WIDTH // 2, PIXELS_IN_HEIGHT // 2 + i)))
        self.draw()
        self.over = False

    def append_body(self):
        '''Make the snake longer :) '''

        last = self.parts[-1]
        x, y = last[1]
        new = ('rest', (x, y + 1))
        self.parts.append(new)

    def check_snake(self):
        '''Maybe it's time to end the game?'''

        head = self.parts[0]
        head_like_rest = ('rest', head[1])
        new_parts = [head_like_rest]
        for i in range(1, len(self.parts)):
            new_parts.append(self.parts[i])

        for part in new_parts:
            if new_parts.count(part) > 1:
                print("GAME OVER")
                raise Exception("snake on snake")
        for part in new_parts:
            if part[1][0] == 0:
                raise Exception("snake on wall")
            elif part[1][0] == PIXELS_IN_WIDTH - 1:
                raise Exception("snake on wall")
            elif part[1][1] == 0:
                raise Exception("snake on wall")
            elif part[1][1] == PIXELS_IN_HEIGHT - 1:
                raise Exception("snake on wall")

    def move(self):
        def move_parts(parts, old_head):
            '''Simple algorithm to move all parts to the place
            where the next part was previously.'''

            new_parts = []
            for i in range(len(parts)):
                if i == 0:
                    old_head = ('rest', old_head[1])
                    new_parts.append(old_head)
                else:
                    new_parts.append(parts[i - 1])
            return new_parts

        head = self.parts[0]
        if self.DIRECTION == "UP":
            new_head = ("head", (head[1][0], head[1][1] - 1))
        elif self.DIRECTION == "RIGHT":
            new_head = ("head", (head[1][0] + 1, head[1][1]))
        elif self.DIRECTION == "LEFT":
            new_head = ("head", (head[1][0] - 1, head[1][1]))
        elif self.DIRECTION == "DOWN":
            new_head = ("head", (head[1][0], head[1][1] + 1))

        if not len(self.parts) > 1:
            self.parts = [new_head]
        else:
            parts = self.parts[1:]
            new_parts = move_parts(parts, head)

            self.parts = [new_head]
            self.parts.extend(new_parts)

    def draw(self):
        for part in self.parts:
            coords = part[1][0] * PIXEL_SIZE[0], part[1][1] * PIXEL_SIZE[1]
            if part[0] == "head":
                im = self.head
            elif part[0] == "rest":
                im = self.rest
            self.blit(im, coords)

    def gameOver(self):
        font = pygame.font.Font(pygame.font.get_default_font(), 30)
        img = font.render("GAME OVER!", 1, (0, 0, 255))
        w, h = self.get_size()
        self.blit(img, (w // 2 - font.size("GAME OVER!")[0] / 2, h // 2))

    def update(self, dt, keys):
        self.dt += dt
        if keys[K_LEFT] and not self.DIRECTION == "RIGHT":
            self.DIRECTION = "LEFT"
        elif keys[K_RIGHT] and not self.DIRECTION == "LEFT":
            self.DIRECTION = "RIGHT"
        elif keys[K_DOWN] and not self.DIRECTION == "UP":
            self.DIRECTION = "DOWN"
        elif keys[K_UP] and not self.DIRECTION == "DOWN":
            self.DIRECTION = "UP"

        minus = (len(self.parts) - 1) * 10
        if self.dt > (200 - minus) and not self.over:
            print("sekunda")
            self.fill((0, 0, 0))
            self.move()
            self.draw()
            try:
                self.check_snake()
            except Exception:
                self.over = True
                print('over...')
            self.dt = 0
        elif self.over:
            self.gameOver()


background = Background(screen.get_size()).convert_alpha()
board = ScoreBoard()
snake = Snake(screen.get_size())
apples = Apple(screen.get_size(), snake, board)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    dt = clock.tick()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    snake.update(dt, keys)
    apples.update()
    screen.blit(board, (0, 0))
    screen.blit(apples, (0, MENU_HEIGHT))
    screen.blit(background, (0, MENU_HEIGHT))
    pygame.display.flip()