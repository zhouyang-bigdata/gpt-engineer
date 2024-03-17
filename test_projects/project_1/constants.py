from enum import Enum

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4