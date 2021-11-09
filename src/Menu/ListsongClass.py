import pygame as pg
from src.Sprite.Button.ButtonClass import *
from src.Utils.utils import *

class Listsong:

    def __init__(self, surface, game_size, game_state):
        self.screen = surface
        self.game_size = game_size
        self.game_state = game_state
        self.game_state_value = game_state.get_game_state()
        self.btnList = []
        self.game_center = (self.game_size[0] / 2, self.game_size[1] / 2)

        # Import the back Btn
        self.btn_back_img = import_image("res/Buttons/Menu/back_btn.png")
        self.back_button = ButtonClass(self.screen, "BackBtn", self.btn_back_img, (0, 0), None, {"btn_pressed": None, "btn_not_pressed": None})
        self.btnList.append(self.back_button)

        # Import the model of the song button
        self.btn_modeleson_img = import_image("res/Buttons/ListSong/modeleson.png")
        y = 100
        for i in range(3):
            self.modeleson_button = ButtonClass(self.screen, "ModelesonBtn" + str(i), self.btn_modeleson_img, (0,y), None, {"btn_pressed": None, "btn_not_pressed": None, "mouse_on_btn": None})
            self.btnList.append(self.modeleson_button)
            y += 90

    def event(self):
        for btn in self.btnList:
            btn.event()

    def update(self):

        self.game_state_value = self.game_state.get_game_state()

        for btn in self.btnList:
            btn.update()

            if btn.name == "BackBtn" and btn.events.get("btn_pressed") == True:
                if self.game_state_value == 3:
                    self.change_btn_state("BackBtn")
                    self.game_state.change_game_state(1)
                    btn.events["btn_pressed"] = False

            if btn.name.__contains__("ModelesonBtn") and btn.events.get("mouse_on_btn"):
                btn.spriteBtn.image = btn.spriteBtn.scaling_sprite((600, 150))


    def change_btn_state(self, btn_name):
        for btn in self.btnList:
            if btn.name != btn_name:
                btn.events["btn_pressed"] = False

    def draw(self):
        for btn in self.btnList:
            btn.draw()
