import pygame as pg

class SpriteClass(pg.sprite.Sprite):
    global spriteList
    spriteList = []

    def __init__(self, surface=type(pg.Surface), name=str(), img=pg.image, pos=tuple(), size=tuple() or None, state=str(), type=str()):
        pg.sprite.Sprite.__init__(self)

        self.typeList = ["Entity", "Object", "Tile", "Button", "Text"]
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

        if size == None:
            self.size = self.get_sprite_size()
        else:
            self.size = size

        spriteList.append(self)

    def get_sprite_size(self):
        return (self.rect[2], self.rect[3])

    def draw(self):
        if self.state == self.stateList[1]:
            self.surface.blit(self.image, self.rect)

    def update(self):
        self.posX, self.posY = self.pos[0], self.pos[1]
        self.rect.topleft = (self.posX, self.posY)

    def check_spriteState_changed(self):
        self.old_sprite_state = self.state
        if self.old_sprite_state != self.state:
            self.old_sprite_state = self.state
            return True
        else:
            return False

    def scaling_sprite(self, scale):
        self.scale_img = pg.transform.scale(self.image, scale)
        return self.scale_img

    def change_sprite_image(self, img):
        pass

    def event(self):
        pass
