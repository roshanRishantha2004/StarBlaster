import pygame
from player import Player

def main():

    player_img = "assets\images\player.png"
    player = Player(player_img, 370, 480)

    pygame.init()

    # Create Main Screen $ Set Titile
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("StarBlaster")

    # Set game icon
    icon = pygame.image.load("assets\images\icon.png")
    pygame.display.set_icon(icon)

    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_left()
                if event.key == pygame.K_RIGHT:
                    player.move_right()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.stop()

        player.draw(screen)
        player.update()
        pygame.display.update()

if __name__ == "__main__":
    main()