import pygame
import os
from assets import ICON_PATH, LOADING_BACKGROUND_PATH, TITLE, play_sound

def lod_screen():

    screen = pygame.display.set_mode((800, 533))
    pygame.display.set_caption(TITLE)
    icon = pygame.image.load(ICON_PATH)
    pygame.display.set_icon(icon)

    play_sound("background.wav")
    background = pygame.image.load(LOADING_BACKGROUND_PATH)

    font = pygame.font.Font(None, 100)
    clock = pygame.time.Clock()

    # planets = []
    # for name in planet_names:
    #     planet_x = random.randint(0, 1200)
    #     planet_y = random.randint(0, 800)
    #     planets.append(Planet(name, planet_x, planet_y))

    running = True
    start_time = pygame.time.get_ticks()

    while running:

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        text_surface = font.render("StarBlaster", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(400, 266))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        if elapsed_time > 10:
            running = False
            pygame.quit()
            return True
        
        # for planet in planets:
        #     planet.draw(screen)
        #     planet.update()


        pygame.display.update()
        clock.tick(10)