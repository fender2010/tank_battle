import sys
import pygame

from bullet import Bullet

def check_keydown_events(event, tb_settings, screen, good, bullets):
	if event.key == pygame.K_RIGHT:
		good.moving_right = True
	elif event.key == pygame.K_LEFT:
		good.moving_left = True
	elif event.key == pygame.K_SPACE:
		# Create a new bullet and add it to the group.
		new_bullet = Bullet(tb_settings, screen, good)
		bullets.add(new_bullet)
			
def check_keydup_events(event, good):	
	if event.key == pygame.K_RIGHT:
		good.moving_right = False
	elif event.key == pygame.K_LEFT:
		good.moving_left = False

def check_events(tb_settings, screen, good, bullets):
	"""Respond to keypresses and mouse movements."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, tb_settings, screen, good, bullets)
		elif event.type == pygame.KEYUP:
			check_keydup_events(event, good)
			
def update_screen(tb_settings, screen, good, bullets):
	"""Update images on the screen and flip to the new screen."""
	#Redraw the screen during each pass through the loop.
	screen.fill(tb_settings.bg_color)
	
	# Redraw all bullets behind tanks.
	for bullet in bullets.sprites():
		bullet.draw_bullet()	
		
	good.blitme()

	#Make the most recently drawn screen visible
	pygame.display.flip()
