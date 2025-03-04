import pygame
from constants import * 
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x,y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.shot_timer = 0
        self.image = pygame.transform.scale(pygame.image.load("shipbird2.webp"), (75, 75))
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        screen.blit(self.image, pygame.Rect(self.position.x -35, self.position.y-35, 10, 10))
        
        

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        self.shot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def shoot(self):
        if self.shot_timer > 0:
            return
        else:
            velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            _ = Shot(self.position.x, self.position.y, SHOT_RADUIS, velocity)
            self.shot_timer = PLAYER_SHOOT_COOLDOWN