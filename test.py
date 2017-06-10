import pygame
from pygame.locals import *
import sys
import window
import input
import debug
import player


ms = input.Mouse()
main_player = player.Player(window)


def game():
    debug.mouse_pos_draw(window, ms)
    main_player.draw(window)
    window.update()

while True:
    ms.update()
    input.event_handler(ms, window)
    game()
    window.frame_handler()
    debug.legend_handler(window)
