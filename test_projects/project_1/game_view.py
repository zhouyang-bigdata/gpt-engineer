import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_COLOR, FOOD_COLOR

class GameView:
    def __init__(self, model):
        self.model = model
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game')

    def render(self):
        self.screen.fill((0, 0, 0))  # Fill the screen with black
        for segment in self.model.snake.segments:
            pygame.draw.rect(self.screen, SNAKE_COLOR, pygame.Rect(segment.x, segment.y, 10, 10))
        pygame.draw.rect(self.screen, FOOD_COLOR, pygame.Rect(self.model.food.position.x, self.model.food.position.y, 10, 10))
        pygame.display.flip()