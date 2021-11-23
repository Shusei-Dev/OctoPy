import pygame as pg
from pygame.locals import *
import os
from src.Sprite.Entity.Player.PlayerClass import *
from src.Sprite.Entity.Tiles.TileClass import *
from src.Utils.FileManager import *
from src.Utils.StateManager import *

class MapManager:

    def __init__(self, surface, game_size):
        self.screen = surface
        self.settings_file = get_yml_content("files/settings.yml")
        self.startedMap = [False, None]
        self.gameSize = game_size

        self.keyBind = {"base0": False, "base1": False, "base2": False, "base3": False, "base4": False, "base5": False, "base6": False, "base7": False}

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
        self.clockTick = clockTick
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

        self.musicMap = pg.mixer.Sound(self.getMapInfo(mapObj, "music_path"))
        self.setVolume(get_yml_content("files/settings.yml").get("volume"))

        self.time_passed = 0
        self.current_beat = 0
        self.BPM = self.getMapInfo(mapObj, "bpm")

        self.tileList = []

        for elements in self.mapData.get("Map_Content"):
            print(elements)

        self.startMap(mapObj)


    def startMap(self, mapObj):

        self.musicMap.play()
        self.startedMap[0] = True
        self.startedMap[1] = mapObj

    def updateMap(self, mapObj):
        self.seconde = int((pg.time.get_ticks() - self.clockTick) / 1000)
        print(self.seconde)

    def stopMap(self):
        if self.startedMap[1] != None:
            self.startedMap[0] = False
            self.startedMap[1] = None
            self.musicMap.stop()
