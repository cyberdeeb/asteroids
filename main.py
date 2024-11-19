import constants
import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot


def main():

    # Initialize and set up pygame
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    score_font = pygame.font.Font("font/PressStart2P.ttf", 18)
    game_over_font = pygame.font.Font("font/PressStart2P.ttf", 45)
    restart_font = pygame.font.Font("font/PressStart2P.ttf", 14)
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    asteroidfield = AsteroidField()
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)


    game_over = False
    

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Restart the game
                    main()
                    return  # Exit the current game loop to restart
                elif event.key == pygame.K_ESCAPE:  # Quit the game
                    pygame.quit()
                    sys.exit()
        
        if not game_over:
        
            screen.fill('black')

            # Render the score text
            score_text = score_font.render(f"Score: {player.score}", True, (57, 255, 20))

            # Blit the text onto the screen
            screen.blit(score_text, (20, 20))

            for obj in updatable:
                obj.update(dt)

            for asteroid in asteroids:
                if player.collision_check(asteroid):
                    # Set game over to True
                    game_over = True

                    # Freeze the screen and display "Game Over"
                    screen.fill('black')

                    # Render "Game Over" and final score
                    game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
                    score_text = score_font.render(f"Final Score: {player.score}", True, (57, 255, 20))
                    restart_text = restart_font.render("Press ENTER to Restart or ESC to Quit", True, (255, 255, 255))

                    # Center the text on the screen
                    game_over_rect = game_over_text.get_rect(center=(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 50))
                    score_rect = score_text.get_rect(center=(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 + 20))
                    restart_rect = restart_text.get_rect(center=(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 + 80))

                    # Blit the text onto the screen
                    screen.blit(game_over_text, game_over_rect)
                    screen.blit(score_text, score_rect)
                    screen.blit(restart_text, restart_rect)



            for obj in drawable:
                obj.draw(screen)

            for asteroid in asteroids:
                for shot in shots:
                    if shot.collision_check(asteroid):
                        asteroid.split()
                        shot.kill()
                        player.score += 1
            

        pygame.display.flip()

            
            
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()