'''
This file creates the maze object.

Since, there are no multiple constructors, I had to put an if else
statement. If you want to create a randomm maze call the constructor
with an empty list for obs. If you want to create a maze by feeding
it the obstacles, you can pass in the list containing indices of all the
obstacle cells.
'''

from Cell import *
from graphics import *
import random


class Maze:
    # cells = [] # list of all the cells
    obstacles = []

    def __init__(self, st, ta, obs):
        self.cells = []
        if not obs:
            self.st = st
            self.ta = ta
            x = self.cells
            white = color_rgb(255, 255, 255)
            black = color_rgb(0, 0, 0)
            x1 = 0
            y1 = 0

            # self.st = random.randint(0, 101 * 101)
            # self.ta = random.randint(0, 101 * 101)

            for i in range(20 * 20):
                p1 = Point(x1, y1)
                p2 = Point(x1 + 20, y1 + 20)
                x1 += 20
                if x1 == 400:
                    x1 = 0
                    y1 += 20
                c = Cell(i, 0, 0, 0, None)
                c.rect = Rectangle(p1, p2)
                rand = random.randint(0, 5)
                if rand == 0 and i != self.st and i != self.ta:
                    c.rect.setFill(black)
                    self.obstacles.append(c)
                    c.blocked = 1
                else:
                    c.rect.setFill(white)
                x.append(c)
        else:
            self.st = st
            self.ta = ta
            x = self.cells
            white = color_rgb(255, 255, 255)
            black = color_rgb(0, 0, 0)
            x1 = 0
            y1 = 0

            # self.st = random.randint(0, 101 * 101)
            # self.ta = random.randint(0, 101 * 101)

            for i in range(20 * 20):
                p1 = Point(x1, y1)
                p2 = Point(x1 + 20, y1 + 20)
                x1 += 20
                if x1 == 400:
                    x1 = 0
                    y1 += 20
                c = Cell(i, 0, 0, 0, None)
                c.rect = Rectangle(p1, p2)
                if i in obs:
                    c.rect.setFill(black)
                    self.obstacles.append(c)
                else:
                    c.rect.setFill(white)
                x.append(c)
