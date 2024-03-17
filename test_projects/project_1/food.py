from random import randint
from dataclasses import dataclass
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

@dataclass
class Food:
    position: Segment

    def __init__(self):
        self.respawn()

    def respawn(self):
        self.position = Segment(randint(0, (SCREEN_WIDTH - 10) // 10) * 10,
                                randint(0, (SCREEN_HEIGHT - 10) // 10) * 10)