
import pygame
from polybius.abstractGame import AbstractGame
from polybius.managers import FRAMES
from polybius.graphics import Drawable
from polybius.utils.draggable import Draggable

class ClubGame(AbstractGame):

    def __init__(self):
        AbstractGame.__init__(self, (1000,600), "Game Title")
        FRAMES.prepareImage("image.png", colorKey=True)
        self._sprite = Sprite((100,100))

    def draw(self, screen):
        self._sprite.draw(screen)
        
    def handleEvent(self, event):
        self._sprite.handleEvent(event)

    def update(self, ticks):
        pass

class Sprite(Drawable, Draggable):

    def __init__(self, position):
        Drawable.__init__(self, "image.png", position)
        Draggable.__init__(self)

    def handleEvent(self, event):
        Draggable.handleDraggingEvent(self, event)

g = ClubGame()
g.run()
