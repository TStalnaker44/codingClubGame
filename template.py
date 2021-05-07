
import pygame
from polybius.abstractGame import AbstractGame
from polybius.managers import FRAMES
from polybius.graphics import Drawable
from polybius.utils.draggable import Draggable
from board import Board

class ClubGame(AbstractGame):

    def __init__(self):
        AbstractGame.__init__(self, (1000,600), "Game Title")
        FRAMES.prepareImage("image.png", colorKey=True)
        FRAMES.prepareImage("grassTile.png")
        FRAMES.prepareImage("stoneTile.png")
        self._sprite = Sprite((100,100))
        tiles = [[-1,1,-1,0],
                 [1,0,1,0],
                 [0,1,0,0],
                 [0,0,0,0],
                 [0,0,0,0]]
        red = pygame.Surface((32,32))
        red.fill((255,0,0))
        tileMap = {0:FRAMES.getFrame("grassTile.png"),
                    1:FRAMES.getFrame("stoneTile.png"),
                    -1:None}
        self._board = Board((100,100), tiles, tileMap=tileMap, tileDims=(21,21))

    def draw(self, screen):
        self._sprite.draw(screen)
        self._board.draw(screen)
        
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
