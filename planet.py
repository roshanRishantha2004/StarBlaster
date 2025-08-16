import os
import pygame

class Planet:
    
    def __init__(self, img_name, planet_x, planet_y):

        assert_dir = os.path.join(os.path.dirname(__file__), "assets", "images", "planets")
        img_path = os.path.join(assert_dir, img_name)

        try:
            self.image = pygame.image.load(img_path)
        
        except pygame.error as e:
            print(f"Could not load image: {e}")
            self.image = None
        
        self.x = planet_x
        self.y = planet_y
        self.planet_x_change = 5
        self.planet_y_change = 5

    def draw(self, surface):

        if self.image:
            surface.blit(self.image, (self.x, self.y))
    
    def update(self):
        self.x += self.planet_x_change
        self.y += self.planet_y_change

        if self.x < 0 or 736:
            self.planet_x_change *= -5

        if self.y < 0 or self.y > 469:
            self.planet_y_change *= -1
    