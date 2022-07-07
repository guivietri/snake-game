import pygame
from level import *

class Main():
    def __init__(self):
        pygame.init()

        apple = Apple()
        snake = Snake()

        screen = pygame.display.set_mode(DISPLAY)
        SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(SCREEN_UPDATE , 150)

        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == SCREEN_UPDATE:
                    snake.move_snake()
                    # collision snake apple
                    if apple.pos in snake.body:
                        snake.body.append(snake.direction)
                        apple = Apple()
                    # collision snake to snake
                    if snake.body[0] in snake.body[1:]:
                        clock.tick(1)
                        Main()
                    if snake.body[0].x < 0 or snake.body[0].x > CELL_NUMBER - 1:
                        clock.tick(1)
                        Main()
                    if snake.body[0].y < 0 or snake.body[0].y > CELL_NUMBER - 1:
                        clock.tick(1)
                        Main()
                if event.type == pygame.KEYDOWN:
                    snake.snake_keys(event)

            screen.fill((BACK_COLOR))
            apple.draw_apple()
            snake.draw_snake()
            pygame.display.update()
            clock.tick(FPS)

if __name__ == '__main__':
    Main()