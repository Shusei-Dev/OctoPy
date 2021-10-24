import pygame as pg
import time
from pygame.locals import *
from src.Menu.MenuClass import *

# 0 = Quit, 1 = Menu, 2 = Settings, 3 = PlayList, 4 = Play
game_state = 1
BACKGROUND = "#000000"

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

        self.screen = pg.display.set_mode(self.game_size, self.fullscreen)
        self.screen_size = self.screen.get_size()
        pg.display.set_caption(self.name + str(self.version))

        self.mainClock = pg.time.Clock()

    # Init all main method.
    def init_method(self):
        self.menu = MenuClass(self.screen, self.game_size, game_state)

    def calculate_deltatime(self):
        self.dt = time.time() - self.previous_frame_time
        dt *= self.fps
        self.previous_frame_time = time.time()

    # Event menu, all event of the game start here.
    def event(self):
        global game_state
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_state = 0

            # Menu event.
            if game_state == 1 or game_state == 2:
                self.menu.event()

            # When the ESCAPE Key is press'd the game will end.
            if event.type == pg.KEYDOWN:
                if event.key == K_ESCAPE:
                    game_state = 0

    # Update method, update the display and the game function
    def update(self):
        global game_state
        pg.display.flip()

        if game_state == 1 or game_state == 2:
            self.menu.update()
            game_state = self.menu.game_state
            self.menu.game_state = game_state


    # Draw method, it will draw everything on screen and refresh it.
    def draw(self):
        self.screen.fill(BACKGROUND)
        global game_state
        if game_state == 1 or game_state == 2:
            self.menu.draw()

    # Main loop of the game, everything here is VERY important because all method is call'd here.
    def main_loop(self):
        global game_state
        while game_state != 0:
            self.event()
            self.update()
            self.draw()
            self.mainClock.tick(self.fps)

        pg.quit()

MainClass = OctoPy()
MainClass.init_method()
MainClass.main_loop()
