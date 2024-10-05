import pygame
from circle import CircleShape
from constants import *

class Asteroid(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = pygame.Rect(x, y, radius * 2, radius * 2)
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius, 2)

    def update(self, dt): 
        displacement = self.velocity * dt
        self.x += displacement.x
        self.y += displacement.y