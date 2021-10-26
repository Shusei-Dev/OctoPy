import pygame as pg
from src.Sprite.SpriteClass import *


class ButtonClass(pg.sprite.Sprite):

    def __init__(self, surface=type(pg.Surface), name=str(), img=pg.image, pos=tuple(), size=tuple() or None, events=dict()):
        self.screen = surface
        self.name = name
        self.img = img
        self.pos = pos

        self.eventList = ["btn_pressed", "mouse_on_btn", "btn_not_pressed", "not_mouse_on_btn"]

        for i in events:
            if not i in self.eventList:
                print("ERROR")
                pass

        self.events = events

        # Create the sprite for the btn
        self.spriteBtn = SpriteClass(self.screen, self.name, self.img, self.pos, size, "Showed", "Button")

        # Get the sprite size for the btn_size
        self.size = self.spriteBtn.size


    def event(self):

        # Do what event is on the events Dict

        # Check if the events Dict have an btn_pressed event
        for i in self.events:
            mouse_pos = pg.mouse.get_pos()

            # Btn_pressed event is here
            if i == self.eventList[0]:
                # Check if the btn is showed
                if self.spriteBtn.state == "Showed":
                    # Check if the mouse is pressed
                    if pg.mouse.get_pressed()[0] == True:
                        # Check if the mouse is on the button
                        if mouse_pos[0] > self.pos[0] and mouse_pos[0] < self.pos[0] + self.size[0] and mouse_pos[1] > self.pos[1] and mouse_pos[1] < self.pos[1] + self.size[1]:
                            # TODO method here
                            self.events[i] = True
                            
                    else:
                        self.events[i] = False


            # Mouse_on_btn event is here
            if i == self.eventList[1]:
                # Check if the btn is showed
                if self.spriteBtn.state == "Showed":
                    # Check if the mouse is on the button
                    if mouse_pos[0] > self.pos[0] and mouse_pos[0] < self.pos[0] + self.size[0] and mouse_pos[1] > self.pos[1] and mouse_pos[1] < self.pos[1] + self.size[1]:
                        # TODO method here
                        self.events[i] = True
                    else:
                        self.events[i] = False

            # Btn_not_pressed event is here
            if i == self.eventList[2]:
                # Check if the btn is showed
                if self.spriteBtn.state == "Showed" or self.spriteBtn.state == "Hidden":
                    # Check if the mouse is pressed
                    if pg.mouse.get_pressed()[0] == False:
                        # Check if the mouse is on the button
                        if mouse_pos[0] > self.pos[0] and mouse_pos[0] < self.pos[0] + self.size[0] and mouse_pos[1] > self.pos[1] and mouse_pos[1] < self.pos[1] + self.size[1]:
                                # TODO method here
                                self.events[i] = True
                    else:
                        self.events[i] = False

            # Not_mouse_on_btn event is here
            if i == self.eventList[3]:
                # Check if the btn is showed
                if self.spriteBtn.state == "Showed":
                    # Check if the mouse is on the button
                    if not mouse_pos[0] > self.pos[0] and not mouse_pos[0] < self.pos[0] + self.size[0] and not mouse_pos[1] > self.pos[1] and not mouse_pos[1] < self.pos[1] + self.size[1]:
                        # TODO method here
                        self.events[i] = True
                    else:
                        self.events[i] = False


    def draw(self):
        self.spriteBtn.draw()

    def update(self):

        pass
