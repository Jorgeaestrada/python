import pygame
# Module import
import game_functions as gf
# Class import
from settings import Settings
from ship import Ship

def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Make a ship.
    ship = Ship(ai_settings, screen)
    # start the main loop for the game
    while True:
        # watch for keyboard and mouse events
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
run_game()

# Chapter 12, 256p.
