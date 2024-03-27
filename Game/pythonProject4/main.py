import pygame
from Snake import Snake



pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Set up the game objects
snake = Snake(screen_width // 2, screen_height // 2)


# Variables for tracking time
last_spawn_time = pygame.time.get_ticks()
spawn_interval = 5000  # Milliseconds between spawns

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left click
                snake.shoot_bullet(pygame.mouse.get_pos(), special_attack=False)
            elif event.button == 3:  # right click
                snake.activate_special_attack()

    # Update
    snake.update()
    snake.bullets.update()  # Update bullet positions

    # Check if it's time to spawn a new special item
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time >= spawn_interval:

        last_spawn_time = current_time

    # Draw
    screen.fill((0, 0, 0))  # Fill the screen with black color
    screen.blit(snake.image, snake.rect)  # Draw the snake

    snake.bullets.draw(screen)  # Draw bullets
    pygame.display.flip()

    clock.tick(60)  # Cap the frame rate to 60 FPS

pygame.quit()
