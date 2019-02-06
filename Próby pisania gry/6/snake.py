import pygame
import sys
import random
import time

# Define Constants
BOARD_SIZE = 30  # Size of the board, in block
BLOCK_SIZE = 20  # Size of 1 block, in pixel
HEAD_COLOR = (0, 100, 0)  # Dark Green
BODY_COLOR = (0, 200, 0)  # Light Green
FOOD_COLOR = (200, 0, 0)  # Dark Red
GAME_SPEED = 10  # Game speed (Normal = 10), The bigger, the faster


class Snake():
    def __init__(self):
        self.head = [int(BOARD_SIZE / 4), int(BOARD_SIZE / 4)]
        self.body = [[self.head[0], self.head[1]],
                     [self.head[0] - 1, self.head[1]],
                     [self.head[0] - 2, self.head[1]]
                     ]
        self.direction = "RIGHT"

    def change_direction_to(self, dir):
        if dir == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        if dir == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        if dir == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        if dir == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    def move(self, food_pos):
        ''' Move the snake to the desired direction by adding the head to that direction
            and remove the tail if the snake does not eat food
        '''
        if self.direction == "RIGHT":
            self.head[0] += 1
        if self.direction == "LEFT":
            self.head[0] -= 1
        if self.direction == "UP":
            self.head[1] -= 1
        if self.direction == "DOWN":
            self.head[1] += 1

        self.body.insert(0, list(self.head))
        if self.head == food_pos:
            return 1
        else:
            self.body.pop()
            return 0

    def check_collision(self):
        # Check if the head collides with the edges of the board
        if self.head[0] >= BOARD_SIZE or self.head[0] < 0:
            return 1
        elif self.head[1] > BOARD_SIZE or self.head[1] < 0:
            return 1
        # Check if the head collides with the body
        for body in self.body[1:]:
            if self.head == body:
                return 1
        return 0

    def get_body(self):
        return self.body


class FoodSpawner():
    def __init__(self):
        self.head = [random.randrange(1, BOARD_SIZE), random.randrange(1, BOARD_SIZE)]
        self.is_food_on_screen = True

    def spawn_food(self):
        if self.is_food_on_screen == False:
            self.head = [random.randrange(1, BOARD_SIZE), random.randrange(1, BOARD_SIZE)]
            self.is_food_on_screen = True
        return self.head

    def set_food_on_screen(self, bool_value):
        self.is_food_on_screen = bool_value


# Game Initialization
window = pygame.display.set_mode((BOARD_SIZE * BLOCK_SIZE, BOARD_SIZE * BLOCK_SIZE))
pygame.display.set_caption("SNAKE GAME")
fps = pygame.time.Clock()

score = 0

# Initialize snake and food
snake = Snake()
food_spawner = FoodSpawner()


def game_start():
    for i in range(3):
        pygame.display.set_caption("SNAKE GAME  |  Game starts in " + str(3 - i) + " second(s) ...")
        pygame.time.wait(1000)


def game_over():
    pygame.display.set_caption("SNAKE GAME  |  Score: " + str(score) + "  |  GAME OVER. Press any key to quit ...")
    while True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            break
    pygame.quit()
    sys.exit()


game_start()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.change_direction_to("RIGHT")
            if event.key == pygame.K_UP:
                snake.change_direction_to("UP")
            if event.key == pygame.K_DOWN:
                snake.change_direction_to("DOWN")
            if event.key == pygame.K_LEFT:
                snake.change_direction_to("LEFT")
    food_pos = food_spawner.spawn_food()
    if snake.move(food_pos) == 1:
        score += 1
        food_spawner.set_food_on_screen(False)

    window.fill(pygame.Color(225, 225, 225))
    # Draw snake
    head = 1
    for pos in snake.get_body():
        if head == 1:
            pygame.draw.rect(window, HEAD_COLOR,
                             pygame.Rect(pos[0] * BLOCK_SIZE, pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            head = 0
        else:
            pygame.draw.rect(window, BODY_COLOR,
                             pygame.Rect(pos[0] * BLOCK_SIZE, pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # Draw food
    pygame.draw.rect(window, FOOD_COLOR,
                     pygame.Rect(food_pos[0] * BLOCK_SIZE, food_pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    if snake.check_collision() == 1:
        game_over()

    pygame.display.set_caption("SNAKE GAME  |  Speed: " + GAME_SPEED + "  |  Score: " + str(score))
    pygame.display.flip()
    fps.tick(GAME_SPEED)﻿