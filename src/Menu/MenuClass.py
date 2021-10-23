import pygame as pg
from src.SpriteClass import *
from src.Utils.utils import *

class MenuClass():

    def __init__(self, screen):
        self.screen = screen

        self.btn_img = import_image("res/mickey.jpg")
        self.button = SpriteClass(screen, "Mickey", self.btn_img, (100,100), None, "Showed", "Button")

    def draw(self):
        self.button.draw()
