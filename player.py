import os
import pygame
from pygame import mixer


class Player:
    
    def __init__(self, img_name, player_x, player_y):

        assert_dir = os.path.join(os.path.dirname(__file__), "assets", "images")
        img_path = os.path.join(assert_dir, img_name)

        try:
            self.image = pygame.image.load(img_path)
        
        except pygame.error as e:
            print(f"Could not load image: {e}")
            self.image = None
        
        self.x = player_x
        self.y = player_y
        self.player_x_change = 0

    
    def draw(self, surface):

        if self.image:
            surface.blit(self.image, (self.x, self.y))
    
    def update(self):
        self.x += self.player_x_change
        if self.x < 0:
            self.x = 0
        elif self.x > 736:
            self.x = 736
    
    def move_right(self):
        self.player_x_change = 0.3

    def move_left(self):
        self.player_x_change = -0.3

    def stop(self):
        self.player_x_change = 0

    def sound(self, audio_name):
        assert_dir = os.path.join(os.path.dirname(__file__), "assets", "sounds")
        audio_path = os.path.join(assert_dir, audio_name)
        audio = mixer.Sound(audio_path)
        audio.play()