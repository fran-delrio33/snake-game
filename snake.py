import pygame

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    def __init__(self, start_pos, cell_size, color=(0, 200, 0)):
        self.cell_size = cell_size
        self.color = color
        self.body = [start_pos]
        self.direction = RIGHT

    def change_direction(self, new_direction):
        opposite = (-self.direction[0], -self.direction[1])
        if new_direction != opposite:
            self.direction = new_direction

    def peek_next_head(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        return (head_x + dx * self.cell_size, head_y + dy * self.cell_size)

    def move(self, grow=False):
        new_head = self.peek_next_head()
        self.body.insert(0, new_head)
        if not grow:
            self.body.pop()

    def hit_wall(self, width, height):
        x, y = self.body[0]
        return x < 0 or x >= width or y < 0 or y >= height

    def hit_self(self):
        return self.body[0] in self.body[1:]

    def draw(self, surface):
        for segment in self.body:
            rect = pygame.Rect(segment[0], segment[1], self.cell_size, self.cell_size)
            pygame.draw.rect(surface, self.color, rect)
