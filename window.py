import pygame
from pygame.locals import *
import sys


pygame.init()
font = pygame.font.SysFont("calibri", 15)
screen_size = (1920, 1200)
main_surf = pygame.display.set_mode(screen_size,FULLSCREEN|HWSURFACE)
frame = 0
time = 0
dt = 0
fps = 0
frame_hist = []
game_clock = pygame.time.Clock()


def update():
    pygame.display.update()
    main_surf.fill((0, 0, 0))


def frame_handler():
    global frame
    global time
    global dt
    global frame_hist
    global game_clock
    global fps
    dt = game_clock.tick()
    time += dt
    fps = game_clock.get_fps()
    frame_hist.append([frame, dt, fps, time])
    frame += 1

# Prints frame info when the main proess exits
def exit_debug_info(game_win):
    sum = 0
    len_framehist = len(game_win.frame_hist)
    for i in range(len_framehist):
        sum += game_win.frame_hist[i][2]
    print("AVG FPS: ", sum / len_framehist)
    print("Total time (s): ", time / 1000)
    print("Frames: ", len(frame_hist))
    print("Memory used for frame hist (bytes): ", sys.getsizeof(frame_hist))

def screen_pos(object_pos):
    return [object_pos[0], screen_size[1]-object_pos[1]]

def clear():
    pass
