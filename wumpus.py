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
    for i in range(20):
        ran = random.randint(0,1)
        if ran == 0:
            x = x + random.randint(-1, 1)
            if x < 0 or x > rows:
                break
            print(f'X: {x}')
            print(f'Y: {y}')
        if ran == 1:
            y = y + random.randint(-1, 1)
            if y < 0 or y > rows:
                break
            print(f'X: {x}')
            print(f'Y: {y}')
        grid[x][y] = "#"

    return grid


def main():
    grid = []
    for i in range(rows):
        grid.append(["-"] * columns)

    grid = makeCave(grid)



    printGrid(grid)

main()