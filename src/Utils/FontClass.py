import pygame as pg


class Font(pg.sprite.Sprite):

    def __init__(self, screen, font_path, pos, size, color):
        pg.sprite.Sprite.__init__(self)
        self.screen = screen
        self.font_color = color
        self.pos = pos
        self.font = pg.font.Font(font_path, size)

    def print_text_font(self, text):
        self.font_render = self.font.render(text, True, self.font_color)
        self.screen.blit(self.font_render, self.pos)
