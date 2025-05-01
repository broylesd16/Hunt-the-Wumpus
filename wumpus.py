import random
#import pygame
#import sys

#python is evil for not having constants
rows = 10
columns = 10

def printGrid(grid):
    for row in grid:
        for i in row:
            print(i, end=' ')
        print()
    #print()

def makeCave(grid):
    x = random.randint(0, rows-1)
    y = random.randint(0, columns-1)
    grid[x][y] = "#"

    counter = 0
    while counter != 60:
        ran = random.randint(0,1)

        if ran == 0:
            newX = x + random.randint(-1, 1)
            if newX < 0 or newX >= rows:
                continue
            else:
                x = newX
            print(f'X: {x}')
            print(f'Y: {y}')

        if ran == 1:
            newY = y + random.randint(-1, 1)
            if newY < 0 or newY >= columns:
                continue
            else:
                y = newY
            print(f'X: {x}')
            print(f'Y: {y}')

        grid[x][y] = "#"
        counter +=1

    return grid


def main():
    grid = []
    for i in range(rows):
        grid.append(["-"] * columns)

    grid = makeCave(grid)



    printGrid(grid)

main()