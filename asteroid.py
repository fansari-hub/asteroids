import pygame
import random
from constants import * 
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x,y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.image = pygame.transform.scale(pygame.image.load("spacefish.webp"), (radius*2, radius*2))

    def draw(self, screen):
        screen.blit(self.image, pygame.Rect(self.position.x -self.radius, self.position.y-self.radius, 10, 10))
        pygame.draw.circle(screen, (40,25,34), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vec1 = self.velocity.rotate(random_angle)
            vec2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vec1 * 1.5
            asteroid2.velocity = vec2 * 1.5
