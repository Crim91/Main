import sys
import pygame


class Player():
    init_rad = 10
    interaction_dict = {}
    def_background = (0, 0, 0)
    def_color = (0, 0, 255)


    def __init__(self, window):
        self.rad = Player.init_rad
        screen_center = (window.main_surf.get_size()[0] / 2, window.main_surf.get_size()[1] / 2)
        self.pos = screen_center
        self.size = [self.rad*2,self.rad*2]
        self.color = Player.def_color
        self.surface = pygame.Surface(self.size)
        self.surface.set_colorkey(Player.def_background)
        self.refresh_surf()

    def refresh_surf(self):
        self.surface.fill(Player.def_background)
        pygame.draw.circle(self.surface,self.color,[self.rad,self.rad],self.rad,1)

    def draw(self,win):
        win.main_surf.blit(self.surface, self.pos)