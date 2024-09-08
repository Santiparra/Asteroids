import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  p_clock = pygame.time.Clock()
  

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)  
  AsteroidField.containers = (updatable)
  Shot.containers = (shots, updatable, drawable)

  asteroid_field = AsteroidField()

  player = Player(
    (SCREEN_WIDTH / 2), 
    (SCREEN_HEIGHT / 2)
  )

  dt = 0

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    for sprite in updatable:
      sprite.update(dt)


        
    for asteroid in asteroids:          
      if asteroid.check_for_collision(player):
        print("Game Over!")
        raise SystemExit()
      for shot in shots:
        if asteroid.check_for_collision(shot):
          shot.kill()
          asteroid.split()  

    screen.fill("black")

    for sprite in drawable:
      sprite.draw(screen)   

    pygame.display.flip()

    #FPS limiter
    dt = p_clock.tick(60) / 1000    

  print("Starting asteroids!")  
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()  