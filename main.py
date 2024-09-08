import pygame
from constants import *
from player import Player

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  p_clock = pygame.time.Clock()
  

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
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