import pygame
from pygame.locals import *
import sys
import input

legend_surf = pygame.Surface((200, 150))
legend_refresh_interval = 1000
legend_background_color = (0,0,0)
legend_font_color = (0, 255, 0)

def mouse_pos_draw(window,ms):
    pygame.draw.circle(window.main_surf, (255,255,255), (ms.pos), 2, 1)


def legend_draw(window):
    frame_time = window.font.render(f"frame time: {window.dt}ms", 1, legend_font_color)
    fps = window.font.render(f"fps: {window.fps:8.0f}", 1, legend_font_color)
    legend_surf.blit(frame_time, (0, 0))
    legend_surf.blit(fps, (0, 13))

def legend_handler(window):
    refresh_legend(window)
    window.main_surf.blit(legend_surf, (0,0))

def refresh_legend(window):
    if window.frame % legend_refresh_interval == 0:
        legend_surf.fill(legend_background_color)
        legend_draw(window)