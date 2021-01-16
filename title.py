import pygame.font

class Banner():
	"""A banner to show the game title and any other desired information
	at the start of the game."""

	def __init__(self, ai_game, title):
		"""Initialize the banner's settings."""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# Set the banner dimensions and properties
		self.width, self.height = 800, 100
		self.banner_color = (0, 255, 0)
		self.border_color = (0, 0, 0)
		self.text_color = (0, 0, 0)
		self.font = pygame.font.SysFont('OCR A Extended', 64)

		# Build the banner's rect object and position it
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.x = (self.screen_rect.width - self.width) // 2
		self.rect.y = self.screen_rect.height // 3

		# Build the banner's border object and position it
		# Build a border for the button and center it
		self.border_rect = pygame.Rect(0, 0, self.width + 6, self.height + 6)
		self.border_rect.x = self.rect.x - 3
		self.border_rect.y = self.rect.y - 3

		self._prep_message(title)


	def _prep_message(self, title):
		"""Turn the title into a rendered image and determine its position."""
		self.title_image = self.font.render(title, True, self.text_color)
		self.title_image_rect = self.title_image.get_rect()
		self.title_image_rect.center = self.rect.center

	def draw_banner(self):
		"""Draw a blank button and border and then draw the message."""
		self.screen.fill(self.border_color, self.border_rect)
		self.screen.fill(self.banner_color, self.rect)
		self.screen.blit(self.title_image, self.title_image_rect)