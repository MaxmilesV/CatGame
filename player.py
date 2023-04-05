import pygame
from pygame.locals import (K_w, K_s, K_a, K_d)


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.scr_sz = screen_size
        self.health = 5

    def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_a]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.scr_sz[0]:
            self.rect.right = self.scr_sz[0]
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.scr_sz[1]:
            self.rect.bottom = self.scr_sz[1]

        if self.health <= 0:
            self.kill()

