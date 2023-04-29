import pygame
import sys
from player import Player
from enemy import Enemy
from healthbar import HealthBar
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

pygame.init()

pygame.display.set_caption('CatGame')

screen_width = 800
screen_height = 600
screen_size = (screen_width, screen_height)

screen = pygame.display.set_mode((screen_width, screen_height))

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 100)

player = Player(screen_size)
player_health = HealthBar(screen_size, player.health)

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

clock = pygame.time.Clock()

running = True
game_over = False

font_big = pygame.font.SysFont('arialblack', 48)
font_small = pygame.font.SysFont('arialblack', 24)
img_gv = font_big.render('GAME OVER', True, (255, 255, 255))
img_rg = font_small.render('Press escape to close the Game', True,
                           (255, 255, 255))
img_gv_rect = img_gv.get_rect(center=(screen_size[0] / 2,
                                      screen_size[1] / 2 - 50))
img_rg_rect = img_rg.get_rect(center=(screen_size[0] / 2,
                                      screen_size[1] / 2 + 50))

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY and not game_over:
            new_enemy = Enemy(screen_size)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    player_health.update()

    enemies.update()

    screen.fill((0, 0, 0))

    if not game_over:
        screen.blit(player_health.surf, player_health.rect)
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        if pygame.sprite.spritecollideany(player, enemies):
            for enemy in enemies:
                if enemy.rect.colliderect(player.rect):
                    enemy.kill()
                    player_health.damage()
                    game_over = player.hit()

    if game_over:
        screen.blit(img_gv, img_gv_rect)
        screen.blit(img_rg, img_rg_rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
