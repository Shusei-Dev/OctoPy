import pygame as pg
import time
from pygame.locals import *
from src.Menu import *

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
        pg.display.set_caption(self.name + str(self.version))

        mainClock = pg.time.Clock()

    def init_method(self):
        self.menu = MenuClass()

    def calculate_deltatime(self):
        self.dt = time.time() - self.previous_frame_time
        dt *= self.fps
        self.previous_frame_time = time.time()

    # Interface(event, update, draw method)
    def event(self):
        global game_state
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_state = 3

    def update(self):
        pg.display.flip()

    def draw(self):
        menu.draw()

    def main_loop(self):
        global game_state
        while game_state != 3:

            self.event()
            self.update()
            if game_state == 0:
                pass

        pg.quit()

MainClass = OctoPy()
MainClass.init_method()
MainClass.main_loop()
