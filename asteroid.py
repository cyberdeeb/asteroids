from circleshape import CircleShape
import constants
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)
            first_velocity = self.velocity.rotate(rand_angle)
            second__velocity = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            split_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid_1.velocity = first_velocity
            split_asteroid_2.velocity = second__velocity

    