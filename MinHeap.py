'''
I implemented my own MinHeap that compares the f values of all
the nodes in it. The node with smallest f value is always at the
root.
'''
from Cell import *

class MinHeap:

    def __init__(self):
        c = Cell(-1, -1, -1, -1, None)
        self.minList = [c]
        self.size = 0


    def moveUp(self, index):
        while index//2 > 0:
            fParent = self.minList[index//2].getFValue()
            fCur = self.minList[index].getFValue()
            #if self.minList[index] < self.minList[index//2]:
            if fCur < fParent:
                temp = self.minList[index//2]
                self.minList[index//2] = self.minList[index]
                self.minList[index] = temp
            elif fCur == fParent:
                if self.minList[index].gVal >self.minList[index//2].gVal:
                    temp = self.minList[index // 2]
                    self.minList[index // 2] = self.minList[index]
                    self.minList[index] = temp
            index //= 2
    def push(self, cell):
        self.minList.append(cell)
        self.size += 1
        self.moveUp(self.size)

    def getSuccessor(self, index):
        if index*2 + 1 > self.size:
            return index*2
        else:
            if self.minList[index*2].getFValue() < self.minList[index*2 + 1].getFValue():
                return index*2
            else:
                return index*2 + 1
    def moveDown(self, index):
        while index*2 <= self.size:
            sIndex = self.getSuccessor(index)
            if self.minList[index].getFValue() > self.minList[sIndex].getFValue():
                temp = self.minList[index]
                self.minList[index] = self.minList[sIndex]
                self.minList[sIndex] = temp
            index = sIndex

    def pop(self):
        if self.size == 0:
            return
        min = self.minList[1]
        self.minList[1] = self.minList[self.size]
        self.size -= 1
        self.minList.pop()
        self.moveDown(1)
        return min

    def isEmpty(self):
        return self.size == 0