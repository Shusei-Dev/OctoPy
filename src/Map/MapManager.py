import pygame as pg
import os
from src.Entity.Player.PlayerClass import *
from src.Utils.FileManager import *

class MapManager:

    def __init__(self, surface):

        self.screen = surface
        self.player = PlayerClass(self.screen)
        self.settings_file = get_yml_content("files/settings.yml")

    def event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                if get_yml_content("files/settings.yml").get("volume") > 0:
                    change_yml_content("files/settings.yml", "volume", get_yml_content("files/settings.yml").get("volume") - 5)
            if event.key == pg.K_UP:
                if get_yml_content("files/settings.yml").get("volume") < 100:
                    change_yml_content("files/settings.yml", "volume", get_yml_content("files/settings.yml").get("volume") + 5)

    def update(self, clockTick):
        self.settings_file = get_yml_content("files/settings.yml")
        self.setVolume(get_yml_content("files/settings.yml").get("volume"))



        self.delta_time = clockTick / 1000
        self.time_passed += self.delta_time
        self.current_beat = int(self.BPM / get_yml_content("files/settings.yml").get("fps") * self.time_passed)

        print(self.current_beat)

    def draw(self):
        pass

    def loadMap(self, mapName):
        loadingFile = get_yml_content("src/Map/maps/" + mapName + ".yml")

        self.mapData = {"Map_Info": {}, "Map_Content": []}

        for elements in loadingFile["map_info"].items():
            mapDataInfo = self.mapData.get("Map_Info")
            mapDataInfo[elements[0]] = elements[1]

        return self.mapData

    def getMapInfo(self, mapObj, t_var):
        return mapObj.get("Map_Info").get(t_var)

    def setVolume(self, volume):
        pg.mixer.music.set_volume((volume/100)-0.05)

    def startMap(self, mapObj):
        pg.mixer.music.load(self.getMapInfo(mapObj, "music_path"))
        self.setVolume(get_yml_content("files/settings.yml").get("volume"))

        self.time_passed = 0
        self.current_beat = 0
        self.BPM = self.getMapInfo(mapObj, "bpm")

        pg.mixer.music.play()
