import pygame
from tetris import Tetris

pygame.init()

screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption('tetris')

playing = True
clock = pygame.time.Clock()
fps = 25
game = Tetris(20, 10)
counter = 0
zoom = 20

while playing:
    if game.tetromino == None:
        game.new_tetromino()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.tetromino.rotate()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                # TODO move left
                pass
            if event.key == pygame.K_RIGHT:
                # TODO move right
                pass
            if event.key == pygame.K_SPACE:
                # TODO drop
                pass
            if event.key == pygame.K_ESCAPE:
                game.__init__(20, 10)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False

    screen.fill((255, 255, 255))

    if game.tetromino is not None:
        for i in range(4):
            for j in range(4):
                if game.tetromino.image()[i][j]:
                    pygame.draw.rect(screen, game.tetromino.color, [game.x + zoom * (j + game.tetromino.x) + 1,
                                      game.y + zoom * (i + game.tetromino.y) + 1,
                                      zoom - 2, zoom - 2])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()