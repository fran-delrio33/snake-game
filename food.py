import random
import pygame


class Food:
    def __init__(self, cell_size, grid_width, grid_height, color=(200, 0, 0)):
        self.cell_size = cell_size
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.color = color
        self.position = (0, 0)

    def randomize_position(self, occupied=()):
        while True:
            x = random.randrange(self.grid_width) * self.cell_size
            y = random.randrange(self.grid_height) * self.cell_size
            self.position = (x, y)
            if self.position not in occupied:
                break

    def draw(self, surface):
        rect = pygame.Rect(self.position[0], self.position[1], self.cell_size, self.cell_size)
        pygame.draw.rect(surface, self.color, rect)
