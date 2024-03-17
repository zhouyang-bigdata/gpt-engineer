import pygame
from constants import Direction

class GameController:
    def __init__(self, model):
        self.model = model

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.model.change_direction(Direction.UP)
            elif event.key == pygame.K_DOWN:
                self.model.change_direction(Direction.DOWN)
            elif event.key == pygame.K_LEFT:
                self.model.change_direction(Direction.LEFT)
            elif event.key == pygame.K_RIGHT:
                self.model.change_direction(Direction.RIGHT)

    def update(self):
        self.model.update()