from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        splitVector1 = self.velocity.rotate(angle)
        splitVector2 = self.velocity.rotate(360 - angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        newAsteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        newAsteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        newAsteroid1.velocity = splitVector1 * 1.2
        newAsteroid2.velocity = splitVector2 * 1.2
