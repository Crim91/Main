import pygame
from pygame.locals import *
import sys
import player

key_name = pygame.key.name
curr_keys = []

def end_game(window):
    window.exit_debug_info(window)
    sys.exit()

def event_handler(ms, kb, window):
    all_events = pygame.event.get()
    for event in all_events:
        # Key is pressed
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == 'escape':
                end_game(window)
            key = key_name(event.key)
            curr_keys.append(key)
            print(curr_keys)

        # Key is let go
        elif event.type == pygame.KEYUP:
            key = key_name(event.key)
            curr_keys.remove(key)
            print(curr_keys)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.button, event.pos)

        elif event.type == pygame.MOUSEBUTTONUP:
            print(event.button, event.pos)


        # end game if close button is clicked
        if event.type == pygame.QUIT:
            end_game(window)

    for plyr in player.Player.all_players:
        if len(curr_keys) > 0:
            plyr.event_handler(curr_keys, ms.current_pos())

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