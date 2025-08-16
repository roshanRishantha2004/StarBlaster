import os
import random
import pygame
from player import Player
# from planet import Planet


assert_dir = os.path.join(os.path.dirname(__file__), "assets", "images")

icon_path = os.path.join(assert_dir, "icon.png")
background_img_path = os.path.join(assert_dir, "background.jpg")
loading_background_path = os.path.join(assert_dir, "intro.jpg")
player_img_path = os.path.join(assert_dir, "player.png")

# planet_names = ["1.png", "2.png", "3.png"]

def loading_screen():

    screen = pygame.display.set_mode((800, 533))
    pygame.display.set_caption("StarBlaster")
    icon = pygame.image.load(icon_path)
    pygame.display.set_icon(icon)

    background = pygame.image.load(loading_background_path)

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

        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        if elapsed_time > 10:
            running = False
            return True
        
        # for planet in planets:
        #     planet.draw(screen)
        #     planet.update()


        pygame.display.update()
        clock.tick(10)
        

def menu_screen():
    pass



def game_screen():

    screen = pygame.display.set_mode((800, 533))
    pygame.display.set_caption("StarBlaster")

    icon = pygame.image.load(icon_path)
    background = pygame.image.load(background_img_path)
    player = Player(player_img_path, 400, 450)

    pygame.display.set_icon(icon)

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
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


def main():
    
    pygame.init()
    pygame.font.init()
    next_screen = loading_screen()

    if next_screen:
        game_screen()

  

if __name__ == "__main__":
    main()