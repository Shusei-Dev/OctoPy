import pygame as pg
from src.Sprite.Entity.EntityClass import *
from src.Utils.utils import *

class PlayerClass:

    def __init__(self, surface, game_size):

        self.screen = surface
        self.keyBaseList = []
        self.playerX, self.playerY = ((game_size[0] / 4) + 40, (game_size[1] / 4) - 180 )
        self.gameSize = game_size
        self.createPlayer()

    def update(self):
        for keyBase in self.keyBaseList:
            keyBase.update()

    def event(self):
        pass

    def draw(self):
        for keyBase in self.keyBaseList:
            keyBase.draw()

    def createPlayer(self):
        keyBasePosList = [(285 + self.playerX, 500 + self.playerY), (438 + self.playerX, 342 + self.playerY), (436 + self.playerX, 146 + self.playerY), (285 + self.playerX, 63 + self.playerY), (94 + self.playerX, 62 + self.playerY), (13 + self.playerX, 148 + self.playerY), (12 + self.playerX, 342 + self.playerY), (94 + self.playerX, 500 + self.playerY)]
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
