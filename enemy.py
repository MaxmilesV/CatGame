import random
import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((255, 255, 255))
        self.scr_sz = screen_size
        self.rect = self.surf.get_rect(
            center=(
                random.randint(self.scr_sz[0] + 20, self.scr_sz[0] + 100),
                random.randint(0, self.scr_sz[1])
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
