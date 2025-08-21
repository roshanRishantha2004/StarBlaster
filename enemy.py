import pygame
import os

class Enemy:
    def __init__(self, img_name, enemy_x, enemy_y):
        assert_dir = os.path.join(os.path.dirname(__file__), "assets", "images")
        img_path = os.path.join(assert_dir, img_name)

        try:
            self.image = pygame.image.load(img_path)

        except pygame.error as e:
            print(f"Could not load image: {e}")
            self.image - None
        
        self.x = enemy_x
        self.y = enemy_y
        self.enemy_x_change = 0.3
        self.enemy_y_change = 0.5

    def draw(self, surface):

        if self.image:
            surface.blit(self.image, (self.x, self.y))

    def update(self):

        self.x += self.enemy_x_change

        if self.x < 0:
            self.x = 0
            self.enemy_x_change = 0.3
        elif self.x > 736:
            self.x = 736
            self.enemy_x_change = -0.3
        
