
import pygame
from polybius.abstractGame import AbstractGame
from polybius.managers import FRAMES
from polybius.graphics import Drawable
from polybius.utils.draggable import Draggable
from board import Board

# https://stackoverflow.com/questions/13218362/fatal-python-error-pygame-parachute-segmentation-fault-when-changing-window
# Fatal Python: error: (pygame parachute) Segmentation Fault
# Python runtime state: intialized

class ClubGame(AbstractGame):

    def __init__(self):

        tileDims = (21,21)
        tiles = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                 [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                 [3, 3, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 3, 3],
                 [3, 3, 2, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 2, 3, 3],
                 [3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3],
                 [3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3],
                 [3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3],
                 [3, 3, 2, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 2, 3, 3],
                 [3, 3, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 3, 3],
                 [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                 [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]
        
        
        AbstractGame.__init__(self,
                              (len(tiles[0])*tileDims[0], len(tiles)*tileDims[1]),
                              "Game Title")

        

        FRAMES.prepareImage("image.png", colorKey=True)
        self._sprite = Sprite((100,100))
        self._sprite.scale(1.5)
        
        FRAMES.prepareImage("grassTile.png")
        FRAMES.prepareImage("stoneTile.png")
        FRAMES.prepareImage("brickTile.png")
        FRAMES.prepareImage("waterTile.png")
        
        tileMap = {0:FRAMES.getFrame("grassTile.png"),
                   1:FRAMES.getFrame("stoneTile.png"),
                   2:FRAMES.getFrame("brickTile.png"),
                   3:FRAMES.getFrame("waterTile.png"),
                  -1:None}
        
        self._board = Board((0,0), tiles, tileMap=tileMap, tileDims=tileDims)

    def draw(self, screen):
        self._board.draw(screen)
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
        pass
        Draggable.handleDraggingEvent(self, event)

g = ClubGame()
g.run()
