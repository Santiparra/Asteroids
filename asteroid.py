import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):


  def draw(self, screen):  
    pygame.draw.circle(screen, "white", [self.x, self.y] ,self.radius, 2)

  def update(self, dt):
      self.y += ASTEROID_SPEED * dt