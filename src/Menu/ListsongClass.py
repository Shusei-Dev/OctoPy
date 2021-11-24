import pygame as pg
from src.Sprite.Button.ButtonClass import *
from src.Utils.utils import *


class Listsong:

    def __init__(self, surface, game_size, game_state, map_manager):
        self.screen = surface
        self.game_size = game_size
        self.game_state = game_state
        self.game_state_value = game_state.get_game_state()
        self.btnList = []
        self.game_center = (self.game_size[0] / 2, self.game_size[1] / 2)
        self.mapManager = map_manager
        self.gameover_menu = False
        self.btnGameoverList = []
        self.textList = []

        # Import the back Btn
        self.btn_back_img = import_image("res/Buttons/Menu/back_btn.png")
        self.back_button = ButtonClass(self.screen, "BackBtn", self.btn_back_img, (0, 0), None, {"btn_pressed": None,"mouse_on_btn": None, "btn_not_pressed": None})
        self.btnList.append(self.back_button)
        self.btnGameoverList.append(self.back_button)
        # Import gameover buttons
        self.btn_retry_img = import_image("res/Buttons/ListSong/retry_btn.png")
        self.retry_button = ButtonClass(self.screen, "RetryBtn", self.btn_retry_img, (self.game_center[0] - 85, self.game_center[1] + 65), None, {"btn_pressed": None,"mouse_on_btn": None, "btn_not_pressed": None})
        self.btnGameoverList.append(self.retry_button)
        # Game over text
        self.gameover_img = import_image("res/Buttons/ListSong/game_over_txt.png")
        self.gameover_spr = SpriteClass(self.screen, "GameoverTxt", self.gameover_img, (self.game_center[0] - (109 / 2) - 60, self.game_center[1] - (59 / 2) - 88), None, "Showed", "Text")
        self.textList.append(self.gameover_spr)

        # Import the model of the song button
        self.btn_modeleson_img = import_image("res/Buttons/ListSong/song1.png")
        y = 100
        for i in range(1):
            self.modeleson_button = ButtonClass(self.screen, "ModelesonBtn" + str(i), self.btn_modeleson_img, (0,y), None, {"btn_pressed": None, "btn_not_pressed": None, "mouse_on_btn": None})
            scalingSize = 1.2
            self.modeleson_button.spriteBtn.image_grande = self.modeleson_button.spriteBtn.scaling_sprite((int(self.modeleson_button.spriteBtn.size[0] * scalingSize), int(self.modeleson_button.spriteBtn.size[1] * scalingSize)))
            self.btnList.append(self.modeleson_button)
            y += 90

    def event(self):
        for btn in self.btnList:
            btn.event()

        for btn in self.btnGameoverList:
            btn.event()

    def update(self):

        self.game_state_value = self.game_state.get_game_state()

        for btn in self.btnList:
            btn.update()

            if btn.name == "BackBtn" and btn.events.get("btn_pressed") == True and self.gameover_menu == False:
                if self.game_state_value == 3:
                    self.change_btn_state("BackBtn")
                    self.game_state.change_game_state(1)
                    btn.events["btn_pressed"] = False

            if btn.name == "BackBtn" and self.gameover_menu == False:
                btn.pos = (0,0)

            if btn.name == "BackBtn" and btn.events.get("mouse_on_btn") == True and self.gameover_menu == False:
                btn.spriteBtn.image = import_image("res/Buttons/Menu/back_btn_press.png")

            if btn.name == "BackBtn" and btn.events.get("mouse_on_btn") == False and self.gameover_menu == False:
                btn.spriteBtn.image = import_image("res/Buttons/Menu/back_btn.png")

            # Change the modeleson boutton size when the mouse is on it
            if btn.name.__contains__("ModelesonBtn") and btn.events.get("mouse_on_btn") and self.gameover_menu == False:
                btn.spriteBtn.image = btn.spriteBtn.image_grande

            if btn.name.__contains__("ModelesonBtn") and not btn.events.get("mouse_on_btn") and self.gameover_menu == False:
                btn.spriteBtn.image = btn.spriteBtn.image_petite

            if btn.name == "ModelesonBtn0" and btn.events.get("btn_pressed") and self.gameover_menu == False:
                if self.game_state_value == 3:
                    self.change_btn_state("ModelesonBtn0")
                    self.testMap = self.mapManager.loadMap("test_map")
                    self.mapManager.initMap(self.testMap)
                    self.target_map = self.testMap
                    self.game_state.change_game_state(4)
                    btn.events["btn_pressed"] = False

        for btn in self.btnGameoverList:
            btn.update()
            if btn.name == "RetryBtn" and btn.events.get("btn_pressed") == True and self.gameover_menu == True:

                if self.game_state_value == 3:
                    self.change_btn_state("RetryBtn")
                    self.mapManager.initMap(self.target_map)
                    self.gameover_menu = False
                    self.game_state.change_game_state(4)
                    btn.events["btn_pressed"] = False

            if btn.name == "RetryBtn" and btn.events.get("mouse_on_btn") == True and self.gameover_menu == True:
                btn.spriteBtn.image = import_image("res/Buttons/ListSong/retry_btn_press.png")

            if btn.name == "RetryBtn" and btn.events.get("mouse_on_btn") == False and self.gameover_menu == True:
                btn.spriteBtn.image = import_image("res/Buttons/ListSong/retry_btn.png")

            if btn.name == "BackBtn" and btn.events.get("btn_pressed") == True and self.gameover_menu == True:
                if self.game_state_value == 3:
                    self.change_btn_state("BackBtn")
                    self.gameover_menu = False
                    btn.events["btn_pressed"] = False

            if btn.name == "BackBtn" and self.gameover_menu == True:
                btn.pos = (self.game_center[0] - 85, self.game_center[1] - 15)

            if btn.name == "BackBtn" and btn.events.get("mouse_on_btn") == True and self.gameover_menu == True:
                btn.spriteBtn.image = import_image("res/Buttons/Menu/back_btn_press.png")

            if btn.name == "BackBtn" and btn.events.get("mouse_on_btn") == False and self.gameover_menu == True:
                btn.spriteBtn.image = import_image("res/Buttons/Menu/back_btn.png")
            btn.update()

        if self.mapManager.gameover:
            print("gameover")
            self.gameover_menu = True
            self.mapManager.gameover = False

    def change_btn_state(self, btn_name):
        for btn in self.btnList:
            if btn.name != btn_name:
                btn.events["btn_pressed"] = False

    def draw(self):
        for btn in self.btnList:
            if self.gameover_menu == False:
                btn.draw()

        for btn in self.btnGameoverList:
            if self.gameover_menu == True:
                btn.draw()

        for txt in self.textList:
            if self.gameover_menu == True:
                txt.draw()
