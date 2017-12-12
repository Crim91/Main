import sys
import pygame
import vector
import math



class Player():
    all_players = []
    init_rad = 10
    interaction_dict = {'w': 'force up',
                        'a': 'force left',
                        's': 'force down',
                        'd': 'force right',}
    def_background = (0, 0, 0)
    def_color = (0, 0, 255)

    def __init__(self, window):
        Player.all_players.append(self)
        self.rad = Player.init_rad
        screen_center = (window.main_surf.get_size()[0] / 2, window.main_surf.get_size()[1] / 2)
        self.pos = screen_center
        self.size = [self.rad*2,self.rad*2]
        self.mass = (self.rad**2)*math.pi
        self.color = Player.def_color
        self.surface = pygame.Surface(self.size)
        self.surface.set_colorkey(Player.def_background)
        self.refresh_surf()
        self.force = [0, 0]
        self.acc = [0, 0]
        self.vel = [0, 0]
        self.keys = []

    def integrate(self, dt):
        self.acc = [0, 0]
        self.acc = vector.scale(self.force, 1/self.mass)
        self.vel = vector.add_scaled(self.vel, self.acc, dt)
        self.pos = vector.add_scaled(self.pos, self.vel, dt)
        self.force = [0, 0]

    def refresh_surf(self):
        self.surface.fill(Player.def_background)
        pygame.draw.circle(self.surface,self.color,[self.rad,self.rad],self.rad,1)

    def draw(self,win):
        vis_pos = win.screen_pos(self.pos)
        win.main_surf.blit(self.surface, vis_pos)

    def apply_force(self, force):
        self.force = [self.force[0]+force[0], self.force[1]+force[1]]

    def event_handler(self, key_list, mouse_info):
        for key in key_list:
            if key in self.interaction_dict.keys():
                if self.interaction_dict[key] == 'force up':
                    self.apply_force([0, .01])
                elif self.interaction_dict[key] == 'force left':
                    self.apply_force([-.01, 0])
                elif self.interaction_dict[key] == 'force down':
                    self.apply_force([0, -.01])
                elif self.interaction_dict[key] == 'force right':
                    self.apply_force([.01, 0])

