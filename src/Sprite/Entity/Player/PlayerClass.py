import pygame as pg
from src.Sprite.Entity.EntityClass import *
from src.Utils.utils import *

class PlayerClass:

    def __init__(self, surface):

        self.screen = surface
        self.keyBaseList = []
        self.playerX, self.playerY = (0, 0)
        self.createPlayer()

    def update(self):
        pass

    def event(self):
        pass

    def draw(self):
        for keyBase in self.keyBaseList:
            keyBase.draw()

    def createPlayer(self):
        keyBasePosList = [(285, 500), (438, 342), (436, 146), (285, 63), (94, 62), (13, 148), (12, 342), (94, 500)]
        for keyBase in range(0, 8):
            self.createKeyBase("res/Player/player_base" + str(keyBase) + ".png", "player_base" + str(keyBase), keyBasePosList[keyBase])

    def createKeyBase(self, path, name, pos):

        key_img = import_image(path)
        keyBase = EntityClass(self.screen, name, key_img, pos, "KeyBase")

        self.scalingSize = 60
        keyBase.entitySprite.image_grande = pg.transform.smoothscale(keyBase.entitySprite.image_grande, (int(keyBase.entitySprite.size[0] / 1.55), int(keyBase.entitySprite.size[1] / 1.5)))
        keyBase.entitySprite.image = keyBase.entitySprite.image_grande
        self.keyBaseList.append(keyBase)

    def keyPressed(self, keyName):
        c = 0
        for keys in self.keyBaseList:
            if keys.name == keyName:
                self.keyBaseList[c].entitySprite.image = pg.transform.smoothscale(import_image("res/Player/" + keys.name + "_pressed.png"), (int(keys.entitySprite.size[0] / 1.55), int(keys.entitySprite.size[1] / 1.5)))
            c += 1

    def keyNotPressed(self, keyName):
        c = 0
        for keys in self.keyBaseList:
            if keys.name == keyName:
                self.keyBaseList[c].entitySprite.image = self.keyBaseList[c].entitySprite.image_grande
            c += 1
