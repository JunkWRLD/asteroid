import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidField = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)   

        for rock in asteroids:
            if rock.collision_check(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collision_check(rock):
                    shot.kill()
                    rock.split()

        screen.fill("black")

        for drawing in drawable:
            drawing.draw(screen) 

        pygame.display.flip()

        dt = clock.tick(60) / 1000

#    print("Starting Asteroids!")
#    print(f"Screen width: {SCREEN_WIDTH}")
#    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
