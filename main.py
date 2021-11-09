import pygame as pg
import time
from pygame.locals import *
from src.Menu.MenuClass import *
from src.Menu.ListsongClass import *
from src.Utils.StateManager import *

BACKGROUND = "#000000"

class OctoPy():

    def __init__(self):
        """Init method of the main class, settings all parameters like fullscreen, fps, version and more..."""
        pg.mixer.pre_init(44100, -16, 2, 2048)
        pg.mixer.init()
        pg.init()

        self.fullscreen = True
        self.name = "OctoPy RythmGame v"
        self.version = 0.1
        self.game_size = (1280, 720)
        self.fps = 240
        self.show_fps = False

        self.os_type = "Windows"

        self.previous_frame_time = 0
        self.dt = 0

        self.game_state = StateManager()

        self.screen = pg.display.set_mode(self.game_size, self.fullscreen)
        self.screen_size = self.screen.get_size()
        pg.display.set_caption(self.name + str(self.version))

        self.mainClock = pg.time.Clock()

    # Init all main method.
    def init_method(self):
        self.menu = MenuClass(self.screen, self.game_size, self.game_state)
        self.listsong = Listsong(self.screen, self.game_size, self.game_state)

    def calculate_deltatime(self):
        self.dt = time.time() - self.previous_frame_time
        dt *= self.fps
        self.previous_frame_time = time.time()

    # Event menu, all event of the game start here.
    def event(self):

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game_state.change_game_state(0)

            # Menu event.
            if self.game_state.get_game_state() == 1 or self.game_state.get_game_state() == 2:
                self.menu.event()

            # ListSong event.
            if self.game_state.get_game_state() == 3:
                self.listsong.event()

            # When the ESCAPE Key is press'd the game will end.
            if event.type == pg.KEYDOWN:
                if event.key == K_ESCAPE:
                    self.game_state.change_game_state(0)

    # Update method, update the display and the game function
    def update(self):
        print(self.game_state.get_game_state())
        pg.display.flip()

        if self.show_fps:
            print(int(self.mainClock.get_fps()))

        if self.game_state.get_game_state() == 1 or self.game_state.get_game_state() == 2:
            self.menu.update()

        if self.game_state.get_game_state() == 3:
            self.listsong.update()


    # Draw method, it will draw everything on screen and refresh it.
    def draw(self):

        self.screen.fill(BACKGROUND)

        if self.game_state.get_game_state() == 1 or self.game_state.get_game_state() == 2:
            self.menu.draw()

        if self.game_state.get_game_state() == 3:
            self.listsong.draw()

    # Main loop of the game, everything here is VERY important because all method is call'd here.
    def main_loop(self):
        while self.game_state.get_game_state() != 0:
            self.event()
            self.update()
            self.draw()
            self.mainClock.tick(self.fps)

        pg.quit()

MainClass = OctoPy()
MainClass.init_method()
MainClass.main_loop()
