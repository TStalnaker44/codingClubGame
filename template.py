
import pygame
from polybius.abstractGame import AbstractGame
from polybius.managers import FRAMES
from polybius.graphics import Drawable 

class ClubGame(AbstractGame):

    def __init__(self):
        AbstractGame.__init__(self, (1000,600), "Game Title")
        FRAMES.prepareImage("image.png", colorKey=True)
        self._sprite = Drawable("image.png",(100,100))

    def draw(self, screen):
        self._sprite.draw(screen)
        
    def handleEvent(self, event):
        pass

    def update(self, ticks):
        pass

g = ClubGame()
g.run()
