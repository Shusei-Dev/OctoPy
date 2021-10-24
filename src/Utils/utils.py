import pygame as pg

def import_image(img_path):
    img = pg.image.load(img_path).convert_alpha()
    return img
