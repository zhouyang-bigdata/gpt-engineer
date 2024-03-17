from snake import Snake
from food import Food
from constants import Direction

class GameModel:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.direction = Direction.RIGHT
        self.score = 0

    def update(self):
        self.snake.move(self.direction)
        if self.snake.head_position() == self.food.position:
            self.snake.grow()
            self.food.respawn()
            self.score += 1

    def change_direction(self, new_direction):
        if (self.direction, new_direction) not in [(Direction.UP, Direction.DOWN), (Direction.DOWN, Direction.UP),
                                                   (Direction.LEFT, Direction.RIGHT), (Direction.RIGHT, Direction.LEFT)]:
            self.direction = new_direction