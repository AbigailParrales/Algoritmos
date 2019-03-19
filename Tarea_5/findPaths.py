# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 00:39:16 2019

@author: DavidGS
"""

class Celda:
    
    isAvailable = True
    
    def __init__(self,isAvailable):
        self.isAvailable = True
        
    def youCanBeHere(self,canBe):
        self.isAvailable = canBe
    
class Maze:
    
    celdaArray = []
    x = 0
    y = 0
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.celdaArray = []
        for i in range(0,self.y):
            newRow = []
            for j in range(0,self.x):
                newCell = Celda(True)
                newRow.append(newCell)
            self.celdaArray.append(newRow)
    
    def closeCell(self,coorX,coorY):
        self.celdaArray[coorY][coorX].youCanBeHere(False)


        
def checkPath(maze,xSize,ySize,index,indey):
    if (maze.celdaArray[indey][index].isAvailable):
        if ((index == xSize-1) and (indey == ySize-1)):
            ## Reached the end of Array
            return 1
        elif (index == xSize-1):
            ## Reached right border
            return checkPath(maze,xSize,ySize,index,indey+1)
        elif (indey == ySize-1):
            ## Reached down border
            return checkPath(maze,xSize,ySize,index+1,indey)
        else:
            return checkPath(maze,xSize,ySize,index,indey+1)+checkPath(maze,xSize,ySize,index+1,indey)
    else:
        return 0

        
if __name__ == '__main__':
    
    maze1 = Maze(7,6)
    maze1.closeCell(1,2)
    maze1.closeCell(2,3)
    maze1.closeCell(3,2)
    maze1.closeCell(5,0)
    maze1.closeCell(5,4)
    print("Checking for 44 possible paths in 'maze1'"+": "+str(checkPath(maze1,maze1.x,maze1.y,0,0)==44))
    
    maze2 = Maze(3,3)
    maze2.closeCell(1,1)
    print("Checking for 2 possible paths in 'maze2'"+": "+str(checkPath(maze2,maze2.x,maze2.y,0,0)==2))
    
    maze3 = Maze(4,4)
    maze3.closeCell(0,2)
    maze3.closeCell(3,0)
    print("Checking for 15 possible paths in 'maze3'"+": "+str(checkPath(maze3,maze3.x,maze3.y,0,0)==15))
    