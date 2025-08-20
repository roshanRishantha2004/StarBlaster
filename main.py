import os 
import pygame
from loading_screen import lod_screen
from home_screen import home
from game_screen import game

# planet_names = ["1.png", "2.png", "3.png"]
def main():
    
    pygame.init()
    pygame.font.init()
    next_screen = lod_screen()

    if next_screen:
        # Loop between home and game: home() returns a selection string
        while True:
            selection = home()
            if selection == "play":
                game()
                # when game() finishes, loop back to home()
            else:
                # any other selection or quit -> exit loop / end program
                break

if __name__ == "__main__":
    main()