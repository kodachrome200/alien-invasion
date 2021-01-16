import pygame
from pygame.sprite import Sprite

class ShipCounter(Sprite):
	"""A class to display a ship sprite for remaining ships"""

	def __init__(self, ai_game):
		"""Initialize the counter and set its starting position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship_counter.bmp')
		self.rect = self.image.get_rect()