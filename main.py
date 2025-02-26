# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_tick = pygame.time.Clock()
    dt = 0

    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        
        updatable.update(dt)

        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            if asteroid.collision_check(player) == True:
                print("Game Over!")
                return
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision_check(shot) == True:
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        dt = clock_tick.tick(60) / 1000


if __name__ == "__main__":
    main()