# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    dt = 0
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    

    while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
              return

        screen.fill("black")
        for thing in updatable:
            thing.update(dt)

        for thing in asteroids:
            if thing.checkCollision(player) == True:
                print("Game over!")
                return
            for bullet in shots:
                if bullet.checkCollision(thing) == True:
                    bullet.kill()
                    thing.split()


        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = timer.tick(60) / 1000


if __name__ == "__main__":
    main()