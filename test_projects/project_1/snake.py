from collections import deque
from dataclasses import dataclass
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

@dataclass
class Segment:
    x: int
    y: int

class Snake:
    def __init__(self):
        self.segments = deque([Segment(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)])
        self.growing = False

    def move(self, direction):
        head = self.segments[0]
        if direction == Direction.UP:
            new_head = Segment(head.x, head.y - 10)
        elif direction == Direction.DOWN:
            new_head = Segment(head.x, head.y + 10)
        elif direction == Direction.LEFT:
            new_head = Segment(head.x - 10, head.y)
        elif direction == Direction.RIGHT:
            new_head = Segment(head.x + 10, head.y)
        self.segments.appendleft(new_head)
        if not self.growing:
            self.segments.pop()
        else:
            self.growing = False

    def grow(self):
        self.growing = True

    def head_position(self):
        return self.segments[0]