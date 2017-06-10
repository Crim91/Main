import pygame
from pygame.locals import *
import sys


pygame.init()
font = pygame.font.SysFont("calibri", 15)
main_surf = pygame.display.set_mode((700,400))
frame = 0
time = 0
frame_time = 0
fps = 0
frame_hist = []
game_clock = pygame.time.Clock()


def update():
    pygame.display.update()
    main_surf.fill((0, 0, 0))


def frame_handler():
    global frame
    global time
    global frame_time
    global frame_hist
    global game_clock
    global fps
    frame_time = game_clock.tick()
    time += frame_time
    fps = game_clock.get_fps()
    frame_hist.append([frame,frame_time, fps, time])
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

def clear():
    pass
