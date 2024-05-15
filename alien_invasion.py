import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		pygame.init()
		self.settings = Settings()

		# Option: play in smaller screen
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		# Option: play in full screen
		#self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")
		self.ship = Ship(self)

		# Set background color
		self.bg_color = (230, 230, 230)

	def run_game(self):
		"""Start main loop"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_screen()


	def _check_events(self):
		# Watch for keyboard and mouse events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _update_screen(self):
		# Redraw the screen dring each pass through the loop
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()


		#Make the most recently drawn screen visible.
		pygame.display.flip()



if __name__ == '__main__':
	# Make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()

