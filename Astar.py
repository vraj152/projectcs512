'''
This file gets the 5th maze from 50 mazes generated in 'FiftyMazes.py' and
runs Forward A* algorithm on it.

The first line of output shows start point and target point.
After that the index and the color of each cell from the path are printed.
If there is a blocked cell, a star is called again and the color of path changes.
At the end you can see the length of path and the size of nodes expanded

I removed the code I used for testing this algorithm on all 50 mazes because
I had to remove the graphical part to do so. This is the exact code I will
be using for demo.

'''

from Maze import *

from graphics import *
from MinHeap import *
import pickle

expanded = []


def manHat(index1, index2):
    x1 = index1 // 20
    y1 = index1 % 20
    x2 = index2 // 20
    y2 = index2 % 20
    dist = abs(x2 - x1) + abs(y2 - y1)
    return dist


def getNeighbors(index, maze):
    neigh = []
    if index > 19:
        neigh.append(maze.cells[index - 20])
    if index % 20 != 0:
        neigh.append(maze.cells[index - 1])
        # neigh.append(index - 1)
    if index < 400:
        if (index + 1) % 20 != 0:
            neigh.append(maze.cells[index + 1])
        # neigh.append(index + 1)
    if index < 380:
        neigh.append(maze.cells[index + 20])
        # neigh.append(index + 101)
    return neigh


def computePath(maze, start, target):
    mh = MinHeap()
    closedList = []

    mh.push(maze.cells[start])

    while not mh.isEmpty():
        current = mh.pop()
        closedList.append(current)
        expanded.append(current)

        if current.index == target:
            path = []
            while current:
                # print(current.index, start)
                path.append(current)
                current = current.parent
            return path[::-1]
        neighbors = getNeighbors(current.index, maze)
        # print (neighbors[1].index)
        for n in neighbors:
            if n in closedList:
                continue
            if n.blocked:
                continue
            n.rect.setFill(color_rgb(0, 206, 209))
            n.gVal = current.gVal + 1
            n.hVal = manHat(n.index, target)

            if n in mh.minList and n.gVal > current.gVal:
                continue
            n.parent = current
            mh.push(n)

    print("Sorry! No path found")
    return []


def resetParents(list):
    for l in list:
        l.parent = None


def main():
    win = GraphWin("Window", 700, 700)

    # print(len(m.cells))99

    start = 380
    target = 19
    m = Maze(start, target, [])

    m.cells[start].rect.setFill(color_rgb(255, 0, 0))
    m.cells[target].rect.setFill(color_rgb(0, 255, 0))

    for j in m.obstacles:
        j.rect.setFill(color_rgb(0, 0, 0))

    for j in m.cells:
        j.rect.draw(win)

    print("start = ", start, "target = ", target)

    pathColor = [color_rgb(255, 200, 255), color_rgb(100, 100, 255), color_rgb(0, 206, 209), color_rgb(255, 140, 0),
                 color_rgb(0, 0, 205), color_rgb(200, 200, 0)]
    star = computePath(m, start, target)
    if not star:
        quit()
    cIndex = 0

    sPointer = start
    path = []
    # print(len(pathColor))
    while not sPointer == target and star:
        for s in star:
            if not s in m.obstacles:
                print(s.index, cIndex)
                s.rect.setFill(pathColor[cIndex])
                m.cells[start].rect.setFill(color_rgb(255, 0, 0))
                m.cells[target].rect.setFill(color_rgb(0, 255, 0))
                time.sleep(0.5)
                sPointer = s.index
                path.append(sPointer)
                # print(ind1)
        # star = computePath(m, sPointer, target)

    print("Nodes Expanded: ", len(expanded), "\nPath length: ", len(path))

    win.getMouse()
    win.close()


main()
