import pygame.font
from time import sleep 

class Countdown:

	def __init__(self, ai_game, start):
		"""Initialize the text for the game start countdown."""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# Set the dimensions and properties of the countdown text
		self.width, self.height = 100, 100
		self.text_color = (255, 0, 0)
		self.font = pygame.font.SysFont("OCR A Extended", 72)


	def countdown(self, start):
		"""Counts down from start and calls current count to be rendered."""
		count = start
		while count > 0:
			self._prep_count(count)
			self._draw_count()
			sleep(1)


	def _prep_count(self, count):
		"""Turn the countdown number into a rendered image and center it"""
		self.count_image = self.font.render(count, True, self.text_color)
		self.count_image_rect = self.count_image.get_rect()
		self.count_image_rect.center = self.rect.center


	def _draw_count(self):
		"""Draw the count number image on the screen."""
		self.screen.blit(self.count_image, self.count_image_rect)

