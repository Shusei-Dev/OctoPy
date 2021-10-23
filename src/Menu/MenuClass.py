import pygame as pg
from src.Sprite.Button.ButtonClass import *
from src.Utils.utils import *

class MenuClass():

    def __init__(self, surface, game_size):
        self.screen = surface
        self.game_size = game_size
        self.btnList = []

        self.btn_play_img = import_image("res/play_btn.png")
        self.play_button = ButtonClass(self.screen, "PlayBtn", self.btn_play_img, (100, 100), None, {"btn_pressed": "test"})
        self.btnList.append(self.play_button)

    def draw(self):
        for btn in self.btnList:
            btn.draw()

    def update(self):
        for btn in self.btnList:
            btn.update()

    def event(self):
        for btn in self.btnList:
            btn.event()
