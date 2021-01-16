import pygame.font

class Button:

	def __init__(self, ai_game, msg):
		"""Initialize button attributes."""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# Set the dimensions and properties of the button
		self.width, self.height = 200, 75
		self.button_color = (255, 255, 0)
		self.border_color = (0, 0, 0)
		self.text_color = (0, 0, 0)
		self.font = pygame.font.SysFont('OCR A Extended', 48)

		# Build the button's rect object and center it
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.x = (self.screen_rect.width - self.width) // 2
		self.rect.y = 2 * self.screen_rect.height // 3

		# Build a border for the button and center it
		self.border_rect = pygame.Rect(0, 0, self.width + 6, self.height + 6)
		self.border_rect.x = self.rect.x - 3
		self.border_rect.y = self.rect.y - 3

		# The button message needs to be prepped only once
		self._prep_msg(msg)


	def _prep_msg(self, msg):
		""" Turn msg into a rendered image and center text on the button."""
		self.msg_image = self.font.render(msg, True, self.text_color,
				self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center


	def draw_button(self):
		"""Draw blank button and border,  and then draw message."""
		self.screen.fill(self.border_color, self.border_rect)
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)