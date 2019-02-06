import pygame
import sys
import time
import random
import collections
import itertools
import os
def main():
    """Snake v 1.59"""
    score = 0  # Initial score
    speed = pygame.time.Clock()
    direction = "R"  # Initial direction
    snake_position = collections.deque([100, 50])  # Initial snake position
    snake_body = collections.deque([[100, 50], [90, 50], [100, 50]])  # Initial snake body
    # It places the food randomly, excluding the border
    food_position = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    food_spawn = True
    # Will define the colors
    white = pygame.Color("white")
    red = pygame.Color("red")
    green = pygame.Color("green")
    black = pygame.Color("black")
    orange = pygame.Color("orange")
    grey = pygame.Color("light grey")
    # Game surface
    player_screen = pygame.display.set_mode((720, 460))  # Set screen size
    pygame.display.set_caption("Snake v.1.38")  # Set screen title and version

    def initializer():
        """ Checks the mistakes, and closes the program if it does while
        printing on the console how many bugs it has, also initializes
        the mixers, and game """
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.mixer.init()
        bugs = pygame.init()
        if bugs[1] > 0:
            print("There are", bugs[1], "bugs! quiting.....")
            time.sleep(3)
            sys.exit("Closing program")
        else:
            print("The game was initialized")

    def game_sound(s):
        """ Include the game sfx and music"""
        if s == 0:
            directory = os.path.dirname(os.path.realpath(sys.argv[0]))
            full_path = os.path.join(directory, "background.ogg")
            pygame.mixer.music.load(full_path)
            pygame.mixer.music.play(-1)
        elif s == 1:
            directory = os.path.dirname(os.path.realpath(sys.argv[0]))
            full_path = os.path.join(directory, "eating.wav")
            pygame.mixer.Sound(full_path).play()
        elif s == 2:
            directory = os.path.dirname(os.path.realpath(sys.argv[0]))
            full_path = os.path.join(directory, "game-over.wav")
            pygame.mixer.Sound(full_path).play()

    def you_lose():
        """ When the players loses, it will show a red message in times new
         roman font with 44 px size in a rectangle box"""
        font_game_over = pygame.font.SysFont("times new roman", 44)
        game_over_surface = font_game_over.render("Game over :(", True, red)
        game_over_position = game_over_surface.get_rect()
        game_over_position.midtop = (360, 15)
        player_screen.blit(game_over_surface, game_over_position)
        game_sound(2)
        scoring()
        pygame.display.flip()  # Updates the screen, so it doesnt freeze
        quiting()

    def pause_menu():
        """It displays the pause menu"""
        player_screen.fill(white)
        pause_font = pygame.font.SysFont("times new roman", 44)
        pause_surface = pause_font.render("Paused", True, black)
        pause_position = pause_surface.get_rect()
        pause_position.midtop = (360, 15)
        player_screen.blit(pause_surface, pause_position)
        pygame.display.flip()

    def quiting():
        """ When this function is called, it will wait 4 seconds and exit"""
        time.sleep(4)
        pygame.quit()
        sys.exit()

    def scoring():
        """ It will shows the score after the game over in times new
        roman font with 16px size and black color in a rectangle box"""
        score_font = pygame.font.SysFont("times new roman", 16)
        score_surface = score_font.render("Score : {}".format(score), True, black)
        score_position = score_surface.get_rect()
        score_position.midtop = (360, 80)
        player_screen.blit(score_surface, score_position)

    initializer()
    game_sound(0)
    paused = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quiting()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Pausing/ unpausing
                    paused = not paused
                    if paused:
                        pygame.mixer.music.pause()
                        pause_menu()
                    else:
                        pygame.mixer.music.unpause()
                # Choose direction by user input, block opposite directions
                key_right = event.key in (pygame.K_RIGHT, pygame.K_d)
                key_left = event.key in (pygame.K_LEFT, pygame.K_a)
                key_down = event.key in (pygame.K_DOWN, pygame.K_s)
                key_up = event.key in (pygame.K_UP, pygame.K_w)
                if key_right and direction != "L":
                    direction = "R"
                elif key_left and direction != "R":
                    direction = "L"
                elif key_down and direction != "U":
                    direction = "D"
                elif key_up and direction != "D":
                    direction = "U"
                elif event.key == pygame.K_ESCAPE:
                    quiting()  # It will quit when esc is pressed

        # Simulates the snake movement(together with snake_body_pop)
        if not paused:
            if direction == "R":
                snake_position[0] += 10
            elif direction == "L":
                snake_position[0] -= 10
            elif direction == "D":
                snake_position[1] += 10
            elif direction == "U":
                snake_position[1] -= 10
            # Body mechanics
            snake_body.appendleft(list(snake_position))
            if snake_position == collections.deque(food_position):
                score += 1  # Every food taken will raise the score by 1
                game_sound(1)
                food_spawn = False  # It removes the food from the board
            else:
                # If the food is taken it will not remove the last body piece(raising snakes size)
                snake_body.pop()
            if food_spawn is False:  # When a food is taken it will respawn randomly
                food_position = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
            food_spawn = True  # It will set the food to True again, to keep the cycle
            # Drawing
            player_screen.fill(grey)  # Set the background to grey
            for position in snake_body:  # Snake representation on the screen
                pygame.draw.rect(player_screen, green, pygame.Rect(position[0], position[1], 10, 10))
            # Food representation on the screen
            pygame.draw.rect(player_screen, orange, pygame.Rect(food_position[0], food_position[1], 10, 10))
            if snake_position[0] not in range(0, 711) or snake_position[1] not in range(0, 451):
                you_lose()  # Game over when the Snake hit a wall
            for block in itertools.islice(snake_body, 1, None):
                if snake_position == collections.deque(block):
                    you_lose()  # Game over when the Snake hits itself
            pygame.display.flip()  # It constantly updates the screen
            speed.tick(26)  # It sets the speed to a playable value


if __name__ == "__main__":
    main()