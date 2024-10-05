import pygame
from constants import *
from player import * 
from asteroid import * 
from asteroidfield import * 

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    AsteroidField.containers = (updatable,)
    

    asteroid_field = AsteroidField()
    updatable.add(asteroid_field)



    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for sprite in updatable:
            sprite.update(dt)

        screen.fill((0, 0, 0))  # clear the screen before drawing

        for sprite in drawable: 
            sprite.draw(screen)
        
        dt = clock.tick(60) / 1000
        pygame.display.flip()

        

if __name__ == "__main__":
        main()  



