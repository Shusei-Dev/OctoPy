import pygame as pg

def import_image(img_path):
    img = pygame.image.load(img_path).convert()
    return img
