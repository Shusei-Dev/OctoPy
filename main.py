import pygame as pg
import time
from pygame.locals import *

# 0 = Menu, 1 = PlayList, 2 = Play, 3 = Quit
game_state = 0

class OctoPy():

    def __init__(self):
        """Init method of the main class, settings all parameters like fullscreen, fps, version and more..."""
        pg.init()

        self.fullscreen = False
        self.name = "OctoPy RythmGame v"
        self.version = 0.1
        self.game_size = (1280, 720)
        self.fps = 60

        self.previous_frame_time = 0
        self.dt = 0

        screen = pg.display.set_mode(self.game_size, self.fullscreen)
        self.screen_size = screen.get_size()
        pg.display.set_caption(self.name + self.version)

        mainClock = pg.time.Clock()

    def calculate_deltatime(self):
        self.dt = time.time() - self.previous_frame_time
        dt *= self.fps
        self.previous_frame_time = time.time()


MainClass = OctoPy( )
