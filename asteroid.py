import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self)
        CircleShape.__init__(self, x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)

    def split(self):
        print(f"Splitting asteroid with radius {self.radius}")  # Debug print
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Calculate new smaller radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Generate a random angle between 20 and 50 degrees
        angle = random.uniform(20, 50)

        # Rotate the velocity vector to split into two directions
        velocity1 = self.velocity.rotate(angle) * 1.2
        velocity2 = self.velocity.rotate(-angle) * 1.2

        # Spawn the two smaller asteroids with updated velocity
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2