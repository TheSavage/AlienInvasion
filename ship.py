import pygame

class Ship:
	"""A class to manage the ship"""

	def __init__(self, ai_game):
		"""Init ship and set starting position"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		#Load the ship image and get it's rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Start each new ship at bottom center of screen
		self.rect.midbottom = self.screen_rect.midbottom

		#Store decimal value for horizontal position
		self.x = float(self.rect.x)

		#Movement flags
		self.moving_right = False
		self.moving_left = False

	def update(self):
		# update ship position based on movement flags
		#update ships x value, not the rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
				self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
				self.x -= self.settings.ship_speed

		#Update rect object from self.x
		self.rect.x = self.x

	def blitme(self):
		"""Draw the ship at current location"""
		self.screen.blit(self.image, self.rect)


