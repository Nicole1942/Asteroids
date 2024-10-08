import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  score = 0 

  pygame.init
  pygame.font.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  font = pygame.font.Font(None, 36)

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
  player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
  asteroid_field = AsteroidField()

  while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return

    screen.fill((0,0,0))
    player.draw(screen)
    for update in updatable:
       update.update(dt)
    for object in drawable:
      object.draw(screen)
    for asteroid in asteroids:
      if asteroid.check_collision(player):
        print("Game over!")
        return
      for shot in shots:
         if asteroid.check_collision(shot):
            asteroid.split()
            score += 10
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

    dt = clock.tick(60) / 1000


if __name__ == "__main__":
  main()