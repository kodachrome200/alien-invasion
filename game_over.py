import pygame.font

class GameOver():
	"""A class defining a banner that displays "GAME OVER" when no ships
	remain."""

	def __init__(self, ai_game):
		"""Initialize banner to be displayed on screen"""

		# Get screen parameters from ai_game
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# Set the dimensions and properties of the banner text
		self.width, self.height = 250, 250
		self.text_color = (255, 0, 0)
		self.font = pygame.font.SysFont('OCR A Extended', 150)

		# Build the banner's rect object and center it
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		self._prep_game_over()


	def _prep_game_over(self):
		"""Turn the banner into a rendered image and center it"""
		text = "GAME OVER"
		self.count_image = self.font.render(text, True, self.text_color)
		self.count_image_rect = self.count_image.get_rect()
		self.count_image_rect.center = self.rect.center


	def draw_game_over(self):
		"""Draw the count number image on the screen."""
		self.screen.blit(self.count_image, self.count_image_rect)

