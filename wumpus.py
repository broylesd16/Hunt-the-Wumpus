import random
#import pygame
#import sys


def main():
    rows = 20
    columns = 20

    grid = []
    for i in range(rows):
        grid.append(["-"] * columns)

    for i in range(0, rows):
        for j in range(0, columns):
            ran = random.randint(0, 1)
            if ran == 0:
                grid[i][j] = "-"
            elif ran == 1:
                grid[i][j] = "#"