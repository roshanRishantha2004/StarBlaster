import os
from pygame import mixer

# Base assets directory
assert_dir = os.path.join(os.path.dirname(__file__), "assets", "images")

# Image paths
ICON_PATH = os.path.join(assert_dir, "icon.png")
BACKGROUND_IMG_PATH = os.path.join(assert_dir, "background.jpg")
LOADING_BACKGROUND_PATH = os.path.join(assert_dir, "intro.jpg")
PLAYER_IMG_PATH = os.path.join(assert_dir, "player.png")
ENEMY_IMG_PATH = os.path.join(assert_dir, "enemy.png")
TITLE = "StarBlaster"

def play_sound(audio_name):
     assert_dir = os.path.join(os.path.dirname(__file__), "assets", "sounds")
     audio_path = os.path.join(assert_dir, audio_name)
     mixer.music.load(audio_path)
     mixer.music.play(-1)
     

