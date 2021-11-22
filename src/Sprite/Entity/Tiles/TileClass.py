import pygame as pg
from src.Sprite.Entity.EntityClass import *

class TileClass:

    def __init__(self, surface, img, name, pos, type):

        self.screen = surface
        self.img = img
        self.name = name
        self.pos = pos
        self.tileType = ["note", "slider"]
        if type in self.tileType:
            self.type = type


        self.tileSprite = EntityClass(self.screen, self.name, self.img, self.pos, "KeyNote", None)
