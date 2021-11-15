import pygame as pg
import time
from pygame.locals import *
from src.Menu.MenuClass import *
from src.Menu.ListsongClass import *
from src.Utils.StateManager import *
from src.Utils.FileManager import *
from src.Utils.FontClass import *
from src.Utils.LayerGroup import *

BACKGROUND = "#000000"

class OctoPy():

    def __init__(self):
        """Init method of the main class, settings all parameters like fullscreen, fps, version and more..."""
        pg.mixer.pre_init(44100, -16, 2, 2048)
        pg.mixer.init()
        pg.init()

        # VERY IMPORTANT, get the file content of the settings.yml where all option are implemented
        self.settings_file_content = get_yml_content('files/settings.yml')

        self.screen_size = (pg.display.Info().current_w, pg.display.Info().current_h)
        # The basics game_size
        self.game_size = (1280, 720)

        # Check if the fullscreen is On on Off in the settings.yml file
        if self.settings_file_content.get("fullscreen") == True:
            self.game_size = self.screen_size
            self.fullscreen = pg.FULLSCREEN
        else:
            self.fullscreen = False
            self.game_size = (1280, 720)


        self.name = self.settings_file_content.get("name")
        self.version = self.settings_file_content.get("version")

        self.fps = self.settings_file_content.get("fps")
        self.show_fps = self.settings_file_content.get("show_fps")

        self.os_type = self.settings_file_content.get("os_type")

        self.previous_frame_time = 0
        self.dt = 0

        self.game_state = StateManager()

        self.screen = pg.display.set_mode(self.game_size, self.fullscreen)
        pg.display.set_caption(self.name + str(self.version))

        self.mainClock = pg.time.Clock()

        # Init the fps_counter font
        self.fps_counter = Font(self.screen, "res/fonts/BACKTO1982.TTF", (20, 20), 20, (0, 255, 255))

        # Create the layer group for all sprite
        self.layered_group = LayerGroup()



    # Init all main method.
    def init_method(self):
        self.menu = MenuClass(self.screen, self.game_size, self.game_state, self.layered_group.get_layer_group())
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
        pg.display.flip()

        # Update the settings var content of the settings.yml file
        self.settings_file_content = get_yml_content('files/settings.yml')

        if self.game_state.get_game_state() == 1 or self.game_state.get_game_state() == 2:
            self.menu.update()

        if self.game_state.get_game_state() == 3:
            self.listsong.update()


    # Draw method, it will draw everything on screen and refresh it.
    def draw(self):

        self.screen.fill(BACKGROUND)

        #self.layered_group.get_layer_group().draw(self.screen)

        # Draw the fps_counter if the permision of it is on
        if self.show_fps:
            self.fps_counter.print_text_font(str(round(self.mainClock.get_fps())))

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
