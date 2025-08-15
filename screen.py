import pygame

class Screen:
    def __init__(self):
        pygame.init()

    def create_screen(self, WIDTH, HEIGHT, CAPTION, ICON_PATH):
        
        surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(CAPTION)

        if ICON_PATH:
            
            try:
                icon = pygame.image.load(ICON_PATH)
                pygame.display.set_icon(icon)

            except pygame.error as e:
                print(f"Could not icon: {e}")

        return surface

    