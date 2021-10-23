import pygame as pg
from src.Sprite.SpriteClass import *
from src.Utils.utils import *

class MenuClass():

    def __init__(self, screen):
        self.screen = screen

        self.btn_img = import_image("res/play_btn.png")
        self.button = SpriteClass(self.screen, "Mickey", self.btn_img, (0,0), None, "Showed", "Button")

    def draw(self):
        self.button.draw()

    def update(self):
        pass

    def event(self):
        pass
