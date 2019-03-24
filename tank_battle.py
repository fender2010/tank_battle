import pygame

from pygame.sprite import Group
from settings import Settings
from good_tank import Good_Tank

import game_functions as gf

def run_game():
	#Initialize game and create a screen object.
	pygame.init()
	tb_settings = Settings()
	screen = pygame.display.set_mode(
		(tb_settings.screen_width, tb_settings.screen_height))
	pygame.display.set_caption("Tank Battle!")
	
	# Make a good tank.
	good = Good_Tank(tb_settings, screen)
	
	# Make a group to store fired bullets.
	bullets = Group()
	
	#Start the main loop for the game.
	while True:
		gf.check_events(tb_settings, screen, good, bullets)
		good.update()
		bullets.update()
		gf.update_screen(tb_settings, screen, good, bullets)

run_game()
