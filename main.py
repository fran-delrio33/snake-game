import sys
import pygame

from snake import Snake, UP, DOWN, LEFT, RIGHT
from food import Food

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

    food = Food(CELL_SIZE, WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE)
    food.randomize_position(occupied=snake.body)

    running = True
    game_over = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key in KEY_TO_DIRECTION:
                snake.change_direction(KEY_TO_DIRECTION[event.key])

        if not game_over:
            will_eat = snake.peek_next_head() == food.position
            snake.move(grow=will_eat)

            if will_eat:
                food.randomize_position(occupied=snake.body)

            if snake.hit_wall(WIDTH, HEIGHT) or snake.hit_self():
                game_over = True

        screen.fill(BG_COLOR)
        snake.draw(screen)
        food.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
