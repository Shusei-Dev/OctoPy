import pygame as pg
from pygame.locals import *

class OctoPy():

    def __init__(self):
        pg.init()
        self.fullscreen = False
        self.game_size = (1280, 720)
        screen = pg.display.set_mode(self.game_size, self.fullscreen)
        self.screen_size = screen.get_size()


MainClass = OctoPy( )
