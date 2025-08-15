import pygame
from screen import Screen


def main():

    icon = "assets\space-ship.png"
    window = Screen()
    window.create_screen(800, 600, "Game", icon)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()