import pygame as pg
from src.Sprite.Button.ButtonClass import *
from src.Sprite.SpriteClass import *
from src.Utils.utils import *
from src.Menu.ListsongClass import *
from src.Utils.FileManager import *
import time


class MenuClass():

    def __init__(self, surface, game_size, game_state, layered_group):
        self.screen = surface
        self.layered_group = layered_group
        self.game_size = game_size
        self.game_state = game_state

        self.game_state_value = game_state.get_game_state()

        self.btnList = []
        self.textList = []

        self.game_center = (self.game_size[0] / 2, self.game_size[1] / 2)

        # Import the settings.yml file
        self.settings_file_content = get_yml_content('files/settings.yml')

        self.settingsState = {"Graphism": False, "Sound": False, "Keys": False}

        # The 3 Main Buttons (Play, Option, Exit)
        # Play Button heres
        self.play_button = self.create_btn("res/Buttons/Menu/play_btn.png", "PlayBtn", (self.game_center[0] - 128 / 2, (self.game_center[1] - 63 / 2) - 85), None, {"btn_pressed": None, "btn_not_pressed": None, "mouse_on_btn": None})
        #self.layered_group.add(self.play_button.spriteBtn)
        # Option Button here
        self.option_button = self.create_btn("res/Buttons/Menu/option_btn.png", "OptionBtn", (self.game_center[0] - 196 / 2, (self.game_center[1] - 86 / 2) - 30), None, {"btn_pressed": None, "btn_not_pressed": None, "mouse_on_btn": None})
        # Exit Button here
        self.exit_button = self.create_btn("res/Buttons/Menu/exit_btn.png", "ExitBtn",((self.game_center[0] - 136 / 2), (self.game_center[1] - 74 / 2) + 25), None, {"btn_pressed": None, "btn_not_pressed": None, "mouse_on_btn": None})

        self.menuBtnList = ["PlayBtn", "OptionBtn", "ExitBtn"]

        # All Settings Button here
        # Back Button here
        self.back_button = self.create_btn("res/Buttons/Menu/back_btn.png", "BackBtn", (self.game_center[0] - 164 / 2, self.game_center[1] - (82 / 2) + 80), None, {"btn_pressed": None, "btn_not_pressed": None, "mouse_on_btn": None})

        # Graphism Button here
        self.graphism_button = self.create_btn("res/Buttons/Menu/graphism_btn.png", "GraphismBtn", (self.game_center[0] - 253 / 2, self.game_center[1] - (84 / 2) - 30), None, {"btn_pressed": None, "btn_not_pressed": None, "mouse_on_btn": None})
        # Fullscreen Button here
        #self.fullscreen_img = import_image("res/Buttons/Menu/fullscreen_btn.png")
        #self.fullscreen_spr = SpriteClass(self.screen, "FullScreen_Txt", self.fullscreen_img, (self.game_center[0] - (109 / 2) - 120, self.game_center[1] - (59 / 2) - 100), None, "Showed", "Text")
        #self.textList.append(self.fullscreen_spr)
        # On/Off Button here
        #self.on_button = self.create_btn("res/Buttons/Menu/on_btn.png", "OnBtn", (self.game_center[0] - (50 / 2) + 50, self.game_center[1] - (30 /2) - 102), None, {"btn_pressed": None, "btn_not_pressed": None, "mouse_on_btn": None})
        #self.off_button = self.create_btn("res/Buttons/Menu/off_btn.png", "OffBtn", (self.game_center[0] - (50 / 2) + 50, self.game_center[1] - (30 /2) - 102), None, {"btn_pressed": None, "btn_not_pressed": None, "mouse_on_btn": None})

        self.settingsBtnList = ["BackBtn", "GraphismBtn"]

        # List of all text and btn in the Graphism Option
        self.graphismTextList = ["FullScreen_Txt"]
        self.graphismBtnList = ["BackBtn", "OnBtn", "OffBtn"]

    def draw(self):
        # Draw all btn
        for btn in self.btnList:

            if self.game_state_value == 1:
                if btn.name in self.menuBtnList:
                    btn.draw()

            if self.game_state_value == 2:
                if self.settingsState["Graphism"] == True:
                    if btn.name in self.graphismBtnList:
                        btn.draw()
                if btn.name in self.settingsBtnList and self.settingsState["Graphism"] == False:
                    btn.draw()

        # Draw all txt
        for txt in self.textList:

            if self.game_state_value == 2:
                if txt.name in self.graphismTextList:
                    if self.settingsState["Graphism"] == True:
                        txt.draw()


    def update(self):

        self.game_state_value = self.game_state.get_game_state()

        OptionBtn_state = None

        for btn in self.btnList:
            btn.update()

            # Update the file content of the settings.yml
            self.settings_file_content = get_yml_content('files/settings.yml')

            # -- MENU PART --

            # PlayBtn update here, will change the game_state to PlayList state when is pressed

            if btn.name == "PlayBtn" and btn.events.get("btn_pressed") == True:
                if self.game_state_value == 1:
                    self.change_btn_state("PlayBtn")
                    self.game_state.change_game_state(3)
                    btn.events["btn_pressed"] = False

            if btn.name == "PlayBtn" and btn.events.get("mouse_on_btn") == True:
                btn.spriteBtn.image = import_image("res/Buttons/Menu/play_btn_press.png")

            if btn.name == "PlayBtn" and btn.events.get("mouse_on_btn") == False:
                btn.spriteBtn.image = import_image("res/Buttons/Menu/play_btn.png")

            # OptionBtn update here, will change the game_state to Settings state when is pressed
            if btn.name == "OptionBtn" and btn.events.get("btn_pressed") == True:
                if self.game_state_value == 1:
                    self.change_btn_state("OptionBtn")
                    self.game_state.change_game_state(2)
                    btn.events["btn_pressed"] = False

            if btn.name == "OptionBtn" and btn.events.get("mouse_on_btn") == True:
                btn.spriteBtn.image = import_image("res/Buttons/Menu/option_btn_press.png")

            if btn.name == "OptionBtn" and btn.events.get("mouse_on_btn") == False:
                btn.spriteBtn.image = import_image("res/Buttons/Menu/option_btn.png")


            # ExitBtn update here, will change the game_state to Exit state when is pressed. Btn how closed the game
            if btn.name == "ExitBtn" and btn.events.get("btn_pressed") == True:
                if self.game_state_value == 1:
                    self.change_btn_state("ExitBtn")
                    self.game_state.change_game_state(0)
                    btn.events["btn_pressed"] = False

            if btn.name == "ExitBtn" and btn.events.get("mouse_on_btn") == True:
                btn.spriteBtn.image = import_image("res/Buttons/Menu/exit_btn_press.png")

            if btn.name == "ExitBtn" and btn.events.get("mouse_on_btn") == False:
                btn.spriteBtn.image = import_image("res/Buttons/Menu/exit_btn.png")



            # -- SETTING PART --

            # BackBtn update here, will change the game_state to Menu state when is pressed
            if btn.name == "BackBtn" and btn.events.get("btn_pressed") == True:
                if self.game_state_value == 2 and self.settingsState["Graphism"] == False:
                    self.change_btn_state("BackBtn")
                    self.game_state.change_game_state(1)
                    btn.events["btn_pressed"] = False

                if self.game_state_value == 2 and self.settingsState["Graphism"] == True:
                    self.change_btn_state("BackBtn")
                    self.settingsState["Graphism"] = False
                    btn.events["btn_pressed"] = False

            #GraphismBtn update here, will open the graphism option menu (change the settingsState)
            if btn.name == "GraphismBtn" and btn.events.get("btn_pressed") == True:
                if self.game_state_value == 2:
                    self.change_btn_state("GraphismBtn")
                    self.settingsState["Graphism"] = True
                    btn.events["btn_pressed"] = False


    def change_btn_state(self, btn_name):
        for btn in self.btnList:
            if btn.name != btn_name:
                btn.events["btn_pressed"] = False

    def create_btn(self, path, name, pos, size, event):
        self.btn_img = import_image(path)
        self.btn = ButtonClass(self.screen, name, self.btn_img, pos, size, event)
        self.btnList.append(self.btn)
        return self.btn

    def event(self):
        for btn in self.btnList:
            btn.event()
