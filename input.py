import pygame
from pygame.locals import *
import sys


def event_handler(ms, window):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window.exit_debug_info(window)
            print(window.time, len(window.frame_hist), sys.getsizeof(window.frame_hist))
            sys.exit()


class Mouse():
    def __init__(self):
        pygame.mouse.set_visible(False)
        pygame.mouse.set_pos(150,150)
        self.update()

    def current_pos(self):
        return pygame.mouse.get_pos()

    def update(self):
        self.pos = self.current_pos()