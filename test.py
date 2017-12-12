import pygame
from pygame.locals import *
import sys
import window
import input
import debug
import player


ms = input.Mouse()
kb = input.Keyboard()
main_player = player.Player(window)


def game():
    debug.mouse_pos_draw(window, ms)
    main_player.draw(window)
    main_player.integrate(window.dt)
    window.update()

while True:
    ms.update()
    input.event_handler(ms, kb,  window)
    game()
    window.frame_handler()
    debug.legend_handler(window)
