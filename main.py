import sys
import pygame

from snake import Snake, UP, DOWN, LEFT, RIGHT

# --- Configuración general ---
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 10

BG_COLOR = (30, 30, 30)

KEY_TO_DIRECTION = {
    pygame.K_UP: UP,
    pygame.K_DOWN: DOWN,
    pygame.K_LEFT: LEFT,
    pygame.K_RIGHT: RIGHT,
}


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    start_pos = (WIDTH // 2 // CELL_SIZE * CELL_SIZE, HEIGHT // 2 // CELL_SIZE * CELL_SIZE)
    snake = Snake(start_pos, CELL_SIZE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key in KEY_TO_DIRECTION:
                snake.change_direction(KEY_TO_DIRECTION[event.key])

        snake.move()

        screen.fill(BG_COLOR)
        snake.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
