import pygame
import random

from assets import tetrominos, shapes, colors


class Tetromino:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.type = random.choice(tetrominos)
        self.shape = shapes[self.type]
        self.color = colors[self.type]
        self.rotation = 0

    def image(self) -> [[int]]:
        return self.shape[self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)
