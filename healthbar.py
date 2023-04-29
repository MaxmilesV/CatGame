import pygame


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, screen_size, health):
        super(HealthBar, self).__init__()
        self.surf = pygame.Surface((200, 30))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(screen_size[0] / 2, screen_size[1] * 0.9))
        self.scr_sz = screen_size
        self.health = health
        self.font = pygame.font.SysFont('arialblack', 18)

    def damage(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.remove()
            self.kill()

    def update(self):
        self.surf.fill((255, 255, 255))
        pygame.draw.rect(self.surf, (255, 0, 0), (0, 0, 200, 30))
        pygame.draw.rect(self.surf, (0, 128, 0),
                         (0, 0, 200 - (40 * (5 - self.health)), 30))
        text_hp = self.font.render(f'{self.health} / 5', True, (0, 0, 0))
        text_hp_rect = text_hp.get_rect(center=(100, 15))
        self.surf.blit(text_hp, text_hp_rect)
