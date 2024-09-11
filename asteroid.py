import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		self.velocity =  0
	def draw(self, screen):
		white = (255, 255, 255)
		pygame.draw.circle(screen, white, self.position, self.radius, 2)

	def update(self, dt):
		self.position += dt *  self.velocity

	def split(self):
		self.kill()
		if self.radius < ASTEROID_MIN_RADIUS:
			return
		angle = random.uniform(20, 50)
		v1 = self.velocity.rotate(angle) * 1.2
		v2 = self.velocity.rotate(-angle) * 1.2
		new_rad = self.radius - ASTEROID_MIN_RADIUS
		asteroid1 = Asteroid(self.position.x, self.position.y, new_rad)
		asteroid2 = Asteroid(self.position.x, self.position.y, new_rad)
		asteroid1.velocity = v1
		asteroid2.velocity = v2
