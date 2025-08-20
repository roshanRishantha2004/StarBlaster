import os
import pygame
from assets import ICON_PATH, BACKGROUND_IMG_PATH, TITLE

txt = ["Play", "Mute", "Settings"]

def home():

    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((800, 533))
    icon = pygame.image.load(ICON_PATH)
    pygame.display.set_icon(icon)
    pygame.display.set_caption(TITLE)

    background = pygame.image.load(BACKGROUND_IMG_PATH)

    font = pygame.font.Font(None, 50)

    running = True
    while running:
        
        screen.fill((0, 0, 0))
        screen.blit(background, ((0, 0)))

        start_y = 200   # starting vertical position
        spacing = 60    # space between items

        for i, text in enumerate(txt):
            text_surface = font.render(text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(400, start_y + i * spacing))
            screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return "quit"
            if event.type == pygame.KEYDOWN:
                # Press 'p' to Play -> return selection to main
                if event.key == pygame.K_p:
                    return "play"
                # optional: press ESC to quit
                if event.key == pygame.K_ESCAPE:
                    return "quit"
        
        pygame.display.update()
    return "quit"

