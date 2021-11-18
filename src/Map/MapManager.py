import pygame as pg
from src.Entity.Player.PlayerClass import *
from src.Utils.FileManager import *

class MapManager:

    def __init__(self, surface):

        self.screen = surface
        self.player = PlayerClass(self.screen)

    def event(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def loadMap(self, mapName):
        loadingFile = get_yml_content("src/Map/maps/" + mapName + ".yml")

        self.mapData = {"Map_Info": {}, "Map_Content": []}

        for elements in loadingFile["map_info"].items():
            print(elements)


    def startMap(self, mapObj):
        pass
