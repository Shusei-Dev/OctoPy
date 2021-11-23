import pygame as pg
from src.Sprite.SpriteClass import *

class EntityClass(pg.sprite.Sprite):

    def __init__(self, surface, name, img, pos, type, size=None):
        pg.sprite.Sprite.__init__(self)

        self.screen = surface
        self.name = name
        self.img = img
        self.pos = pos
        self.size = size

        self.entityTypeList = ["KeyBase", "KeyNote"]
        if type in self.entityTypeList:
            self.type = type

        self.entitySprite = SpriteClass(self.screen, self.name, self.img, self.pos, self.size, "Showed", "Entity")
        self.state = self.entitySprite.state

    def draw(self):
        self.entitySprite.draw()

    def update(self):
        self.entitySprite.update()
        self.entitySprite.pos = self.pos
        self.state = self.entitySprite.state
