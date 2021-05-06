
import pygame
from polybius.abstractGame import AbstractGame

class ClubGame(AbstractGame):

    def __init__(self):
        AbstractGame.__init__(self, (1000,600), "Game Title")

    def draw(self, screen):
        pass
        
    def handleEvent(self, event):
        pass

    def update(self, ticks):
        pass

g = ClubGame()
g.run()
