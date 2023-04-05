import pygame
import sys
from player import Player
from enemy import Enemy
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

pygame.init()

screen_width = 800
screen_height = 600
screen_size = (screen_width, screen_height)

screen = pygame.display.set_mode((screen_width, screen_height))

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 100)

player = Player(screen_size)

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

clock = pygame.time.Clock()
clock.tick(60)

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy(screen_size)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    enemies.update()

    screen.fill((0, 0, 0))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        for enemy in enemies:
            if enemy.rect.colliderect(player.rect):
                enemy.kill()
                player.health -= 1
                if player.health <= 0:
                    running = False

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
