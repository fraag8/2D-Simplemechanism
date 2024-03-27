import pygame
from Bullets import Bullet


class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=5):
        super().__init__()
        self.image = pygame.Surface((20, 20))  # Create a placeholder image for the snake
        self.image.fill((0, 255, 0))  # Green color for the snake
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed
        self.dx = 0  # Horizontal velocity
        self.dy = 0  # Vertical velocity
        self.special_attack_available = False
        self.bullets = pygame.sprite.Group()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.dx = 0
            self.dy = -self.speed
        elif keys[pygame.K_s]:
            self.dx = 0
            self.dy = self.speed
        elif keys[pygame.K_a]:
            self.dx = -self.speed
            self.dy = 0
        elif keys[pygame.K_d]:
            self.dx = self.speed
            self.dy = 0

        # Update the snake's position
        self.rect.x += self.dx
        self.rect.y += self.dy

    def shoot_bullet(self, mouse_pos, special_attack=False):
        if not special_attack:   # Placeholder for creating a regular bullet at the snake's position
            bullet = Bullet(self.rect.centerx, self.rect.centery, 0, -5)  # Example: Bullet moving upwards
            self.bullets.add(bullet)  # Add the bullet to the bullets group
            print("Shooting regular bullet towards position:", mouse_pos)
        else:
            if self.special_attack_available:
                print("Performing special attack at position:", mouse_pos)
                # Add special attack logic here
                self.special_attack_available = False
            else:
                print("Special attack not available")

    def collect_special_item(self):
        self.special_attack_available = True
        print("Special item collected")

    def activate_special_attack(self):
        if self.special_attack_available:
            self.shoot_bullet(self.rect.center, special_attack=True)
            print("Special attack activated")
        else:
            print("Special attack not available")
