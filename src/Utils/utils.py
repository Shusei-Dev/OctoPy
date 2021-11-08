import pygame as pg

os_type = "Linux" # Linux or Windows


def import_image(img_path):

    img = pg.image.load(img_path).convert_alpha()
    return img
