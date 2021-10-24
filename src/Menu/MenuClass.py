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

    def draw(self):
        for btn in self.btnList:
            btn.draw()

    def update(self):
        for btn in self.btnList:
            btn.update()

            # PlayBtn update here, will change the game_state to PlayList state when is pressed
            if btn.name == "PlayBtn" and btn.events.get("btn_pressed") == True:
                self.game_state = 3

            # OptionBtn update here, will change the game_state to Settings state when is pressed
            if btn.name == "OptionBtn" and btn.events.get("btn_pressed") == True:
                self.game_state = 2

            # ExitBtn update here, will change the game_state to Exit state when is pressed. Btn how closed the game
            if btn.name == "ExitBtn" and btn.events.get("btn_pressed") == True:
                self.game_state = 0

            # Will show all btn that is not pressed
            if btn.events.get("btn_not_pressed") == True:
                btn.spriteBtn.state = "Showed"

        print(self.game_state)

    def event(self):
        for btn in self.btnList:
            btn.event()
