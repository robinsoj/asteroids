import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, SHOT_RADIUS)
		self.velocity = 0

	def draw(self, screen):
		white = (255, 255, 255)
		pygame.draw.circle(screen, white, self.position, self.radius, 2)

	def update(self, dt):
		self.position += dt * self.velocity
