import pygame as pg
from src.Sprite.Entity.EntityClass import *

class TileClass:

    def __init__(self, surface, img, name, pos):

        self.screen = surface
        self.img = img
        self.name = name
        self.pos = pos

        self.tileSprite = EntityClass(self.screen, self.name, self.img, self.pos, "KeyNote", None)
