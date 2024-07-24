pip install pygame

import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
GRID_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
WINDOW_WIDTH = GRID_WIDTH * GRID_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * GRID_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Directions (x, y)
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class SnakeGame:
    def __init__(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        # Snake initial position and direction
        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.direction = RIGHT

        # Generate initial food position
        self.food = self.generate_food_position()

        # Game variables
        self.score = 0
        self.game_over = False

    def generate_food_position(self):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in self.snake:
                return (x, y)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != DOWN:
                    self.direction = UP
                elif event.key == pygame.K_DOWN and self.direction != UP:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                    self.direction = RIGHT

    def move_snake(self):
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])

        # Check if snake hits boundaries or itself
        if (new_head in self.snake or
            new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
            self.game_over = True
            return

        # Check if snake eats food
        if new_head == self.food:
            self.snake.insert(0, new_head)
            self.score += 1
            self.food = self.generate_food_position()
        else:
            self.snake.insert(0, new_head)
            self.snake.pop()

    def draw(self):
        self.window.fill(BLACK)
        # Draw snake
        for segment in self.snake:
            pygame.draw.rect(self.window, GREEN, (segment[0]*GRID_SIZE, segment[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))
        # Draw food
        pygame.draw.rect(self.window, RED, (self.food[0]*GRID_SIZE, self.food[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))
        # Draw score
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {self.score}', True, WHITE)
        self.window.blit(text, (10, 10))

        pygame.display.flip()

    def run(self):
        while not self.game_over:
            self.handle_events()
            self.move_snake()
            self.draw()
            self.clock.tick(FPS)

        self.show_game_over_screen()

    def show_game_over_screen(self):
        font = pygame.font.Font(None, 72)
        text = font.render('Game Over', True, WHITE)
        text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.window.fill(BLACK)
        self.window.blit(text, text_rect)
        pygame.display.flip()

        pygame.time.wait(2000)

        self.reset()
        self.run()

if __name__ == '__main__':
    game = SnakeGame()
    game.run()