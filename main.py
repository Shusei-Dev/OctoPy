import pygame as pg
import time
from pygame.locals import *
from src.Menu.MenuClass import *
from src.Menu.ListsongClass import *
from src.Utils.StateManager import *
from src.Utils.FileManager import *
from src.Utils.FontClass import *
from src.Utils.LayerGroup import *
from src.Map.MapManager import *

BACKGROUND = "#000000"

class OctoPy():

    def __init__(self):
        """Init method of the main class, settings all parameters like fullscreen, fps, version and more..."""
        pg.mixer.pre_init(22050, -16, 2, 1024)
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

        self.background = import_image("res/Background/fondetoile.png")

        # Init the fps_counter font
        self.fps_counter = Font(self.screen, "res/fonts/BACKTO1982.TTF", (self.game_size[0] - 60, 20), 20, (0, 255, 255))

        # Create the layer group for all sprite
        self.layered_group = LayerGroup()


    # Init all main method.
    def init_method(self):
        self.menu = MenuClass(self.screen, self.game_size, self.game_state, self.layered_group.get_layer_group())
        self.mapManager = MapManager(self.screen, self.game_size, self.game_state)
        self.listsong = Listsong(self.screen, self.game_size, self.game_state, self.mapManager)

    def calculate_deltatime(self):
        self.dt = time.time() - self.previous_frame_time
        self.dt *= self.fps
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

            # MapManager event.
            if self.game_state.get_game_state() == 4:
                self.mapManager.event(event)

            # When the ESCAPE Key is press'd the game will end.
            if event.type == pg.KEYDOWN:
                if event.key == K_ESCAPE:
                    if self.game_state.get_game_state() == 4:
                        self.game_state.change_game_state(3)
                        self.mapManager.stopMap()
                    else:
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

        if self.game_state.get_game_state() == 4:
            self.mapManager.update(self.clockTick)

        # Update the screen size
        if self.settings_file_content.get("fullscreen") == True:
            self.game_size = self.screen_size
            self.fullscreen = pg.FULLSCREEN
        else:
            self.fullscreen = False
            self.game_size = (1280, 720)


    # Draw method, it will draw everything on screen and refresh it.
    def draw(self):

        self.screen.fill(BACKGROUND)

        self.screen.blit(self.background, self.background.get_rect())

        #self.layered_group.get_layer_group().draw(self.screen)

        # Draw the fps_counter if the permision of it is on
        if self.show_fps:
            self.fps_counter.print_text_font(str(round(self.mainClock.get_fps())))

        if self.game_state.get_game_state() == 1 or self.game_state.get_game_state() == 2:
            self.menu.draw()

        if self.game_state.get_game_state() == 3:
            self.listsong.draw()

        if self.game_state.get_game_state() == 4:
            self.mapManager.draw()

    # Main loop of the game, everything here is VERY important because all method is call'd here.
    def main_loop(self):
        while self.game_state.get_game_state() != 0:
            self.event()
            self.update()
            self.draw()
            self.clockTick = self.mainClock.tick(self.fps)

        pg.quit()

MainClass = OctoPy()
MainClass.init_method()
MainClass.main_loop()
