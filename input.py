import pygame
from pygame.locals import *
import sys


def end_game(window):
    window.exit_debug_info(window)
    sys.exit()

def event_handler(ms, kb, window):
    all_events = pygame.event.get()
    for event in all_events:
        # Key is pressed or let go
        if event.type in [pygame.KEYDOWN, pygame.KEYUP]:
            print(pygame.key.name(event.key))

        # end game if close button is clicked
        elif event.type == pygame.QUIT:
            end_game(window)
            
        # end game if escape key is pressed
        elif event.type == pygame.KEYDOWN and pygame.key.name(event.key) == 'escape':
            end_game(window)
class Keyboard():
    def __init__(self):
        pass

    def display_keypress(self):
        if pygame.key.get_focused():
            for entry in pygame.key.get_pressed():
                if entry != 0:
                    print(entry)

class Mouse():
    def __init__(self):
        pygame.mouse.set_visible(False)
        pygame.mouse.set_pos(150,150)
        self.update()

    def current_pos(self):
        return pygame.mouse.get_pos()

    def update(self):
        self.pos = self.current_pos()