import sys
import pygame

from snake import Snake, UP, DOWN, LEFT, RIGHT
from food import Food

# --- Configuración general ---
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 10

BG_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)

KEY_TO_DIRECTION = {
    pygame.K_UP: UP,
    pygame.K_DOWN: DOWN,
    pygame.K_LEFT: LEFT,
    pygame.K_RIGHT: RIGHT,
}


def create_entities():
    start_pos = (WIDTH // 2 // CELL_SIZE * CELL_SIZE, HEIGHT // 2 // CELL_SIZE * CELL_SIZE)
    snake = Snake(start_pos, CELL_SIZE)

    food = Food(CELL_SIZE, WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE)
    food.randomize_position(occupied=snake.body)

    return snake, food


def draw_centered_text(surface, font, text, color, y):
    rendered = font.render(text, True, color)
    rect = rendered.get_rect(center=(WIDTH // 2, y))
    surface.blit(rendered, rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)
    title_font = pygame.font.SysFont(None, 48)

    snake, food = create_entities()
    score = 0
    state = "start"  # "start", "playing" o "game_over"

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if state == "start":
                    if event.key == pygame.K_SPACE:
                        state = "playing"
                elif state == "playing":
                    if event.key in KEY_TO_DIRECTION:
                        snake.change_direction(KEY_TO_DIRECTION[event.key])
                elif state == "game_over":
                    if event.key == pygame.K_SPACE:
                        snake, food = create_entities()
                        score = 0
                        state = "playing"

        if state == "playing":
            will_eat = snake.peek_next_head() == food.position
            snake.move(grow=will_eat)

            if will_eat:
                score += 1
                food.randomize_position(occupied=snake.body)

            if snake.hit_wall(WIDTH, HEIGHT) or snake.hit_self():
                state = "game_over"

        screen.fill(BG_COLOR)

        if state == "start":
            draw_centered_text(screen, title_font, "SNAKE", TEXT_COLOR, HEIGHT // 2 - 30)
            draw_centered_text(screen, font, "Presiona ESPACIO para empezar", TEXT_COLOR, HEIGHT // 2 + 20)
        else:
            snake.draw(screen)
            food.draw(screen)

            score_surface = font.render(f"Puntaje: {score}", True, TEXT_COLOR)
            screen.blit(score_surface, (10, 10))

            if state == "game_over":
                draw_centered_text(screen, title_font, "GAME OVER", TEXT_COLOR, HEIGHT // 2 - 30)
                draw_centered_text(screen, font, "Presiona ESPACIO para reiniciar", TEXT_COLOR, HEIGHT // 2 + 20)

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
