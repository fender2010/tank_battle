import pygame

class Good_Tank():
	
	def __init__(self, tb_settings, screen):
		"""Initialize the good tank and set its starting position."""
		self.screen = screen
		# load the tank image and get its rect.
		self.image = pygame.image.load('images/good_tank.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.tb_settings = tb_settings
		
		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		# Store a decimal value for the tank's center.
		self.center = float(self.rect.centerx)
		
		# Movement flags
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		"""Update the tank's position based on the movement flags."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.tb_settings.tank_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.tb_settings.tank_speed_factor
		
		# Update rect object from self.center
		self.rect.centerx = self.center
		
	def blitme(self):
		"""Draw the tank at its current location."""
		self.screen.blit(self.image, self.rect)
