import pygame as pg
from src.Sprite.Entity.EntityClass import *

class TileClass:

    def __init__(self, surface, img, name, pos, type, showTime, tilePlace, scaling):

        self.screen = surface
        self.img = img
        self.name = name
        self.pos = pos
        self.state = "Showed"
        self.showTime = showTime
        self.tilePlace = tilePlace
        self.scaling = scaling
        self.toScale = 0
        self.scaleCenter = (0, 0)

        self.tileType = ["note", "slider"]
        if type in self.tileType:
            self.type = type

        self.tileSprite = EntityClass(self.screen, self.name, self.img, self.pos, "KeyNote", None)

    def draw(self):
        self.tileSprite.draw()

    def update(self):
        self.tileSprite.pos = self.pos
        self.tileSprite.state = self.state
        self.tileSprite.update()
