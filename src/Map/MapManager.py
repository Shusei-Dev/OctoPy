import pygame as pg
from pygame.locals import *
import os
from src.Sprite.Entity.Player.PlayerClass import *
from src.Sprite.Entity.Tiles.TileClass import *
from src.Utils.FileManager import *
from src.Utils.StateManager import *
from src.Utils.utils import *
from src.Utils.FontClass import *

class MapManager:

    def __init__(self, surface, game_size, game_state):
        self.screen = surface
        self.game_state = game_state
        self.settings_file = get_yml_content("files/settings.yml")
        self.startedMap = [False, None]
        self.gameSize = game_size
        self.gameover = False
        self.keyBind = {"base0": False, "base1": False, "base2": False, "base3": False, "base4": False, "base5": False, "base6": False, "base7": False}
        self.noteImgList = [import_image("res/Key_Tiles/key_tile0.png"), import_image("res/Key_Tiles/key_tile1.png"), import_image("res/Key_Tiles/key_tile2.png"), import_image("res/Key_Tiles/key_tile3.png"), import_image("res/Key_Tiles/key_tile4.png"), import_image("res/Key_Tiles/key_tile5.png"), import_image("res/Key_Tiles/key_tile6.png"), import_image("res/Key_Tiles/key_tile7.png")]
        self.noteReduce = None



    def event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                if get_yml_content("files/settings.yml").get("volume") > 0:
                    change_yml_content("files/settings.yml", "volume", get_yml_content("files/settings.yml").get("volume") - 5)
            if event.key == pg.K_UP:
                if get_yml_content("files/settings.yml").get("volume") < 100:
                    change_yml_content("files/settings.yml", "volume", get_yml_content("files/settings.yml").get("volume") + 5)

            for bases in range(0, 8):
                if pg.key.name(event.key) == get_yml_content("files/settings.yml").get("controls").get("base" + str(bases)):
                    self.keyBind["base" + str(bases)] = True

        if event.type == pg.KEYUP:
            for bases in range(0, 8):
                if pg.key.name(event.key) == get_yml_content("files/settings.yml").get("controls").get("base" + str(bases)):
                    self.keyBind["base" + str(bases)] = False


    def update(self, clockTick):
        self.settings_file = get_yml_content("files/settings.yml")
        self.setVolume(get_yml_content("files/settings.yml").get("volume"))

        self.delta_time = clockTick / 1000
        self.time_passed += self.delta_time
        self.current_beat = int(self.BPM / get_yml_content("files/settings.yml").get("fps") * self.time_passed)

        for keysbind in range(0, 8):
            if self.keyBind["base" + str(keysbind)] == True:
                self.player.keyPressed("player_base" + str(keysbind))
            if self.keyBind["base" + str(keysbind)] == False:
                self.player.keyNotPressed("player_base" + str(keysbind))
        if self.startedMap[0]:

            self.player.update()
            self.updateMap(self.startedMap[1])


    def draw(self):
        if self.startedMap[0]:
            self.player.draw()
            for tiles in self.tileList:
                if tiles.state == "Showed" and tiles.showTime + 3 >= float("%.2f" % self.timer) and tiles.showTime <= float("%.2f" % self.timer):
                    tiles.draw()
            self.pts_counter.print_text_font(str(self.total_pts))
            self.combo_counter.print_text_font(str())


    def loadMap(self, mapName):
        loadingFile = get_yml_content("src/Map/maps/" + mapName + ".yml")

        self.mapData = {"Map_Info": {}, "Map_Content": []}

        for elements in loadingFile["map_info"].items():
            mapDataInfo = self.mapData.get("Map_Info")
            mapDataInfo[elements[0]] = elements[1]

        for elements in loadingFile["content"]:
            mapDataContent = self.mapData.get("Map_Content")
            mapDataContent.append(elements)

        return self.mapData

    def getMapInfo(self, mapObj, t_var):
        return mapObj.get("Map_Info").get(t_var)

    def setVolume(self, volume):
        self.musicMap.set_volume((volume/1000))

    def initMap(self, mapObj):
        self.player = PlayerClass(self.screen, self.gameSize)
        self.notePosX, self.notePosY = ((self.gameSize[0] / 2) - 90, (self.gameSize[1] / 2) - 100)
        self.notePosList = [(104 + self.notePosX, 159 + self.notePosY), (160 + self.notePosX, 102 + self.notePosY), (160 + self.notePosX , 32 + self.notePosY), (104 + self.notePosX, 0 + self.notePosY), (32 + self.notePosX, 0 + self.notePosY), (0 + self.notePosX, 32 + self.notePosY), (0 + self.notePosX, 102 + self.notePosY), (32 + self.notePosX, 158 + self.notePosY)]

        self.clock = pg.time.Clock()
        self.timer = 0
        self.dt = 0

        self.pts_counter = Font(self.screen, "res/fonts/BACKTO1982.TTF", (self.gameSize[0] - 60, self.gameSize[1] - 55), 20, (255, 255, 255))

        self.combo_counter = Font(self.screen, "res/fonts/BACKTO1982.TTF", (60, self.gameSize[1] - 55), 20, (255, 255, 255))

        self.scalingTile = 4.5
        self.velocity = 1

        self.musicMap = pg.mixer.Sound(self.getMapInfo(mapObj, "music_path"))
        self.setVolume(get_yml_content("files/settings.yml").get("volume"))

        self.time_passed = 0
        self.current_beat = 0
        self.BPM = self.getMapInfo(mapObj, "bpm")

        self.total_pts = 0
        self.combo = 0

        self.tileList = []

        for elements in self.mapData.get("Map_Content"):
            if elements[2] == "note":
                self.createNote("note" + str(len(self.tileList) + 1), elements[0], elements[1])

        self.startMap(mapObj)


    def startMap(self, mapObj):

        self.musicMap.play()
        self.startedMap[0] = True
        self.startedMap[1] = mapObj

    def updateMap(self, mapObj):
        self.timer += self.dt
        self.dt = self.clock.tick(get_yml_content("files/settings.yml").get("fps")) / 1000
        #self.player.loose_hp(1)
        if self.check_hp() == 0:
            self.gameover = True
            self.stopMap()
            self.game_state.change_game_state(3)


        for tiles in self.tileList:
            if tiles.state == "Showed" and tiles.showTime + 3 >= float("%.2f" % self.timer) and tiles.showTime <= float("%.2f" % self.timer):
                if tiles.tilePlace == 0:
                    if float("%.2f" % tiles.toScale) < 0.9:
                        tiles.toScale += 0.006
                        tiles.pos = (tiles.pos[0] + 0.02, tiles.pos[1] + self.velocity)
                        self.scalingNote(tiles, tiles.toScale, False)

                    else:
                    # La note est sorti du cadran donc le combo est cassé
                        tiles.state = "Hidden"
                        print("FAUTE")

                    if self.keyBind["base0"] and tiles.tileSprite.entitySprite.rect[0] > self.player.keyBaseList[0].entitySprite.rect[0] and tiles.tileSprite.entitySprite.rect[1] > (self.player.keyBaseList[0].entitySprite.rect[1] - 20):
                        tiles.state = "Hidden"
                        self.total_pts += 100
                        self.combo += 1


                if tiles.tilePlace == 1:
                    if float("%.2f" % tiles.toScale) < 0.9:
                        tiles.toScale += 0.006
                        tiles.pos = (tiles.pos[0] + 0.5, tiles.pos[1] + self.velocity - 1)
                        self.scalingNote(tiles, tiles.toScale, False)



            tiles.update()

        print(self.total_pts)

    def createNote(self, name, pos, showTime):

        tile = TileClass(self.screen, self.noteImgList[pos], name, self.notePosList[pos], "note", showTime, pos, self.scalingTile)
        self.scalingNote(tile, self.scalingTile, True)
        self.tileList.append(tile)

    def scalingNote(self, tile, scaling, decrase):
        if decrase:
            tile.tileSprite.entitySprite.image_grande = pg.transform.smoothscale(tile.tileSprite.entitySprite.image_petite, (int(tile.tileSprite.entitySprite.size[0] / scaling), int(tile.tileSprite.entitySprite.size[1] / scaling)))
            tile.update()
        else:
            tile.tileSprite.entitySprite.image_grande = pg.transform.smoothscale(tile.tileSprite.entitySprite.image_petite, (int(tile.tileSprite.entitySprite.size[0] * scaling), int(tile.tileSprite.entitySprite.size[1] * scaling)))
            tile.update()

        tile.tileSprite.entitySprite.image = tile.tileSprite.entitySprite.image_grande


    def check_hp(self):
        return self.player.hp


    def stopMap(self):
        if self.startedMap[1] != None:
            self.startedMap[0] = False
            self.startedMap[1] = None
            self.clockTick = 0
            self.musicMap.stop()
