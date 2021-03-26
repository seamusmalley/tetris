from tetromino import Tetromino

class Tetris:
    x, y = 100, 60
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.field = [[0 for _ in range(width)] for _ in range(height)]
        self.level = 0
        self.score = 0
        self.state = 1
        self.tetromino = None

    def new_tetromino(self):
        self.tetromino = Tetromino(3, 0)