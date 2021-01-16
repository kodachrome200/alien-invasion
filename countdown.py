import pygame.font

class Countdown():
	"""A class for a countdown number to be rendered on-screen when the
	game is started or when the ship is hit."""

	def __init__(self, ai_game):
		"""Create a countdown object to be displayed on screen"""
		# Initialize data

		# Get screen parameters from ai_game
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# Set the dimensions and properties of the countdown text
		self.width, self.height = 250, 250
		self.text_color = (255, 0, 0)
		self.font = pygame.font.SysFont('OCR A Extended', 150)

		# Build the countdown's rect object and center it
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center


	def _prep_count(self, count):
		"""Turn the countdown number into a rendered image and center it"""
		count_str = str(count)
		self.count_image = self.font.render(count_str, True, self.text_color)
		self.count_image_rect = self.count_image.get_rect()
		self.count_image_rect.center = self.rect.center


	def draw_count(self, count):
		"""Draw the count number image on the screen."""
		self._prep_count(count)
		self.screen.blit(self.count_image, self.count_image_rect)

