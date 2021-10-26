import pygame as pg
from src.Sprite.Button.ButtonClass import *
from src.Utils.utils import *

class MenuClass():

    def __init__(self, surface, game_size, game_state):
        self.screen = surface
        self.game_size = game_size
        self.game_state = game_state
        self.btnList = []
        self.game_center = (self.game_size[0] / 2, self.game_size[1] / 2)

        self.settingsState = {"Graphism": False, "Sound": False, "Keys": False}

        # The 3 Main Buttons (Play, Option, Exit)
        # Play Button here
        self.btn_play_img = import_image("res/buttons/play_btn.png")
        self.play_button = ButtonClass(self.screen, "PlayBtn", self.btn_play_img, (self.game_center[0] - 128 / 2, (self.game_center[1] - 63 / 2) - 85), None, {"btn_pressed": None, "btn_not_pressed": None})
        self.btnList.append(self.play_button)
        # Option Button here
        self.btn_option_img = import_image("res/buttons/option_btn.png")
        self.option_button = ButtonClass(self.screen, "OptionBtn", self.btn_option_img, (self.game_center[0] - 196 / 2, (self.game_center[1] - 86 / 2) - 30), None, {"btn_pressed": None, "btn_not_pressed": None})
        self.btnList.append(self.option_button)
        # Exit Button here
        self.btn_exit_img = import_image("res/buttons/exit_btn.png")
        self.exit_button = ButtonClass(self.screen, "ExitBtn", self.btn_exit_img, ((self.game_center[0] - 136 / 2), (self.game_center[1] - 74 / 2) + 25), None, {"btn_pressed": None, "btn_not_pressed": None})
        self.btnList.append(self.exit_button)

        self.menuBtnList = ["PlayBtn", "OptionBtn", "ExitBtn"]

        # All Settings Button here
        # Back Button here
        self.btn_back_img = import_image("res/buttons/back_btn.png")
        self.back_button = ButtonClass(self.screen, "BackBtn", self.btn_back_img, (self.game_center[0] - 164 / 2, self.game_center[1] - (82 / 2) + 80), None, {"btn_pressed": None, "btn_not_pressed": None})
        self.btnList.append(self.back_button)

        # Graphism Button here
        self.btn_graphism_img = import_image("res/buttons/graphism_btn.png")
        self.graphism_button = ButtonClass(self.screen, "GraphismBtn", self.btn_graphism_img, (self.game_center[0] - 253 / 2, self.game_center[1] - (84 / 2) - 30), None, {"btn_pressed": None, "btn_not_pressed": None})
        self.btnList.append(self.graphism_button)

        self.settingsBtnList = ["BackBtn", "GraphismBtn"]

    def draw(self):
        for btn in self.btnList:

            if self.game_state == 1:
                if btn.name in self.menuBtnList:
                    btn.draw()

            if self.game_state == 2:
                if btn.name in self.settingsBtnList:
                    if btn.name == "GraphismBtn" and self.settingsState["Graphism"] == True:
                        pass
                    btn.draw()


    def update(self):
        OptionBtn_state = None
        for btn in self.btnList:
            btn.update()

            # -- MENU PART --

            # PlayBtn update here, will change the game_state to PlayList state when is pressed
            if btn.name == "PlayBtn" and btn.events.get("btn_pressed") == True:
                if self.game_state == 1:
                    self.game_state = 3
                    btn.events["btn_pressed"] = False

            # OptionBtn update here, will change the game_state to Settings state when is pressed
            if btn.name == "OptionBtn" and btn.events.get("btn_pressed") == True:
                if self.game_state == 1:
                    self.game_state = 2
                    btn.events["btn_pressed"] = False

            # ExitBtn update here, will change the game_state to Exit state when is pressed. Btn how closed the game
            if btn.name == "ExitBtn" and btn.events.get("btn_pressed") == True:
                if self.game_state == 1:
                    btn.events["btn_pressed"] = False
                    self.game_state = 0


            # -- SETTING PART --

            # BackBtn update here, will change the game_state to Menu state when is pressed
            if btn.name == "BackBtn" and btn.events.get("btn_pressed") == True:
                if self.game_state == 2:
                    self.game_state = 1
                    self.settingsState["Graphism"] = False
                    btn.events["btn_pressed"] = False

            if btn.name == "GraphismBtn" and btn.events.get("btn_pressed") == True:
                if self.game_state == 2:
                    print("Test")
                    self.settingsState["Graphism"] = True
                    btn.events["btn_pressed"] = False



            #print(btn.spriteBtn.state)

        #print(self.game_state)

    def event(self):
        for btn in self.btnList:
            btn.event()
