import pygame as pg

class SpriteClass(pg.sprite.Sprite):
    global spriteList
    spriteList = []

    def __init__(self, surface=type(pg.Surface), name=str(), img=pg.image, pos=tuple(), size=tuple() or None, state=str(), type=str()):
        pg.sprite.Sprite.__init__(self)

        self.typeList = ["Entity", "Object", "Tile", "Button"]
        self.stateList = ["Hidden", "Showed"]
        self.surface = surface
        self.name = name
        self.collapse = True
        self.pos = pos

        self.posX, self.posY = self.pos[0], self.pos[1]

        if type in self.typeList:
            self.type = type
        else:
            print("This type seems to not exist")
            return

        if state in self.stateList:
            self.state = state
        else:
            print("This is not an existing state")

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posX, self.posY)

        spriteList.append(self)

    def draw(self):
        self.surface.blit(self.image, self.rect)

    def update(self):
        self.rect.topleft = (self.posX, self.posY)
