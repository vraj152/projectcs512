'''
This file creates a cell object that contains some properties required
to implement our algorithms.

'''

from graphics import *


class Cell:
    rect = Rectangle(Point(1000, 1000), Point(1001, 1001))
    blocked = 0
    hVal = 0
    gVal = 0
    parent = None
    index = -1

    def __init__(self, ind, b, h, g, p):
        # print(po1.getX(), po2.getX())
        # self.rect = Rectangle(po1, po2)
        # self.p1 = po1
        # self.p2 = po2
        self.blocked = b
        self.hVal = h
        self.gVal = g
        self.parent = p
        self.index = ind

    def getFValue(self):
        return self.hVal + self.gVal
