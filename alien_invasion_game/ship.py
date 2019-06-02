import pygame

class Ship():
	
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its 'rectangle'.
        # every rectangle has his own width and height
        # example: the ship rectangle dimensions are 60x48
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        print('Rect: ', self.rect)
        self.screen_rect = self.screen.get_rect()
        print('screen_rect: ',self.screen_rect)

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        print('screen_rect_center: ',self.screen_rect.centerx)
        print('screen_rect_bottom: ',self.screen_rect.bottom)

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        print('rect_centerx: ', self.rect.centerx)

		# Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
            print("nave der: ", self.rect.right, "pantalla der: ",self.screen_rect.right)
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
            print("nave der: ", self.rect.right, "pantalla izq: ",self.screen_rect.left)
        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
