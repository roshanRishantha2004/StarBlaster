import pygame
import random
from assets import ICON_PATH, BACKGROUND_IMG_PATH, TITLE, PLAYER_IMG_PATH, ENEMY_IMG_PATH
from player import Player
from enemy import Enemy


def game():

    pygame.init()

    screen = pygame.display.set_mode((800, 533))
    pygame.display.set_caption(TITLE)

    icon = pygame.image.load(ICON_PATH)
    background = pygame.image.load(BACKGROUND_IMG_PATH)
    player = Player(PLAYER_IMG_PATH, 400, 450)
    enemy = Enemy(ENEMY_IMG_PATH, random.randint(0, 800), random.randint(50, 200))

    pygame.display.set_icon(icon)

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_left()
                    player.sound("laser.wav")
                if event.key == pygame.K_RIGHT:
                    player.move_right()
                    player.sound("laser.wav")

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.stop()

        player.draw(screen)
        enemy.draw(screen)
        player.update()
        enemy.update()


        pygame.display.update()