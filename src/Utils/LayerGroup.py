import pygame as pg

class LayerGroup:

    def __init__(self):
        self.layered_group = pg.sprite.LayeredUpdates()

    def add(self, sprite):
        self.layered_group.add(sprite)

    def get_layer_group(self):
        return self.layered_group
