import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage bullets fired from the ship"""
	
	def __init__(self, tb_settings, screen, good):
		"""Create a bullet object at the tank's current postion"""
		super(Bullet, self).__init__()
		self.screen = screen
		
		# Create a bullet at (0, 0) and then set the correct position.
		self.rect = pygame.Rect(0, 0, tb_settings.bullet_width, 
			tb_settings.bullet_height)
		self.rect.centerx = good.rect.centerx
		self.rect.top = good.rect.top
		
		# Store the bullet's position as a decimal value.
		self.y = float(self.rect.y)
		
		self.color = tb_settings.bullet_color
		self.speed_factor = tb_settings.bullet_speed_factor
		
	def update(self):
		"""Move the bullet up the screen."""
		# Update the position of the bullet.
		self.y -= self.speed_factor
		# Update rect position.
		self.rect.y = self.y
		
	def draw_bellet(self):
		"""Draw the bullet on the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)
