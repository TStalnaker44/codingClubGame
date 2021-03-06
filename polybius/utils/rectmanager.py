"""
Author: Trevor Stalnaker
File: rectmanager.py

Manages more complicated collide rectangles for sprites
"""

import copy, pygame

def getRects(image):
    """This fucntion gets the rects for an image."""

    print("come on man")
    pxa = pygame.PixelArray(image)
    print(type(image))
    print("but not this")
    print(type(pxa))
    print(pxa.shape)
    transparent = (0,0,0)#pxa[0,0]
    print("1")
    rects = []
    print("2")
    scale = 1
    print("3")
    rects, flag, count = [], False, 0
    print("4")

    print("whats happening")
    for h in range(pxa.shape[1]):
        leftBound = 0
        inRect = False
        for w in range(pxa.shape[0]):
            if pxa[w, h] == transparent:
                if inRect:
                    inRect = False
                    width = w-leftBound
                    rect = pygame.Rect(leftBound, h, width, 1)
                    rects.append(rect)
                    leftBound += 1
            else:
                if not inRect:
                    inRect = True
                    leftBound = w
                if w == pxa.shape[0]-1: #End of row
                    width = w - (leftBound-1)
                    rect = pygame.Rect(leftBound, h, width, 1)
                    rects.append(rect)
    return rects

def moveRects(rects, pos):
    """This function moves the rects to a certain position."""
    return [rect.move(pos[0],pos[1]) for rect in rects]

def visualizeRects(rects):
    y = 0
    x = 0
    retString = ""
    for r in rects:
        if r.y == y:
            retString += (" " * (r.x - x)) + ("0" * r.width)
            x = r.x+r.width
        elif r.y > y:
            retString += "\n"
            x = 0
            y = r.y
            retString += (" " * (r.x - x)) + ("0" * r.width)
            x = r.x+r.width        
    print(retString)
                    
