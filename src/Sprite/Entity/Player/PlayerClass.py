import pygame as pg
from src.Sprite.Entity.EntityClass import *
from src.Sprite.SpriteClass import *
from src.Utils.utils import *

class PlayerClass:

    def __init__(self, surface, game_size):

        self.screen = surface
        self.keyBaseList = []
        self.playerX, self.playerY = ((game_size[0] / 4) + 40, (game_size[1] / 4) - 180 )
        self.gameSize = game_size
        self.hp = 100
        self.hpBarList = []
        self.hpBar = SpriteClass(self.screen, "HpBar", import_image("res/Player/hp_bar.png"), (15, 15), None, "Showed", "Tile")
        self.createPlayer()
        self.create_hp_bar()

    def update(self):
        self.hpBar.update()

        for keyBase in self.keyBaseList:
            keyBase.update()

        for hpBars in self.hpBarList:
            print(hpBars.name)
            if self.hp <= 130:
                hpBars.entitySprite.state = "Showed"
            else:
                if hpBars.name == "hpBar12" and self.hp <= 120:
                    hpBars.entitySprite.state = "Hidden"





    def event(self):
        pass

    def draw(self):
        self.hpBar.draw()

        for keyBase in self.keyBaseList:
            keyBase.draw()

        for hpBars in self.hpBarList:
            hpBars.draw()

    def createPlayer(self):
        keyBasePosList = [(295 + self.playerX, 560 + self.playerY), (491 + self.playerX, 360 + self.playerY), (487 + self.playerX, 115 + self.playerY), (290 + self.playerX, 14 + self.playerY), (44 + self.playerX, 12 + self.playerY), (-60 + self.playerX, 120 + self.playerY), (-61 + self.playerX, 362 + self.playerY), (46 + self.playerX, 560 + self.playerY)]
        for keyBase in range(0, 8):
            self.createKeyBase("res/Player/player_base" + str(keyBase) + ".png", "player_base" + str(keyBase), keyBasePosList[keyBase])

    def createKeyBase(self, path, name, pos):
        key_img = import_image(path)
        keyBase = EntityClass(self.screen, name, key_img, pos, "KeyBase")

        self.scalingSize = 1.2
        keyBase.entitySprite.image_grande = pg.transform.smoothscale(keyBase.entitySprite.image_grande, (int(keyBase.entitySprite.size[0] / self.scalingSize), int(keyBase.entitySprite.size[1] / self.scalingSize)))
        keyBase.entitySprite.image = keyBase.entitySprite.image_grande
        self.keyBaseList.append(keyBase)

    def keyPressed(self, keyName):
        for keys in self.keyBaseList:
            if keys.name == keyName:
                keys.entitySprite.image = pg.transform.smoothscale(import_image("res/Player/" + keys.name + "_pressed.png"), (int(keys.entitySprite.size[0] / self.scalingSize), int(keys.entitySprite.size[1] / self.scalingSize)))


    def keyNotPressed(self, keyName):
        for keys in self.keyBaseList:
            if keys.name == keyName:
                keys.entitySprite.image = keys.entitySprite.image_grande


    def loose_hp(self, nmb):
        if self.hp > 0:
            self.hp -= nmb

    def create_hp_bar(self):
        fiveHpBar = import_image("res/Player/5_hp.png")
        tenHpBar = import_image("res/Player/10_hp.png")
        x = 0
        for i in range(0, 13):

            hpBar = EntityClass(self.screen, "hpBar" + str(i), tenHpBar, (24 + x, 21), "HpBar")
            x += 32
            self.hpBarList.append(hpBar)
