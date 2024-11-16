import constants
import pygame
from player import Player

def main():

    # Initialize and set up pygame
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    dt = 0

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill('black')
        player.draw(screen)
        pygame.display.flip()

        
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()