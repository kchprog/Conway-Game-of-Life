import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class cell:
    state = 0

    def __init__(self, state):
        self.state = state
    
    def getState(self):
        return self.state
    
    def display_cell(self) -> str:
        if self.state == 0:
            return "."
        elif self.state == 1:
            return "□"


def display_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j].display_cell(), end="")
        print()


def clear():
    # clear the console
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def spawn_glider(grid) -> None:
    # spawn a glider
    grid[2][1].state = 1
    grid[3][2].state = 1
    grid[3][3].state = 1
    grid[2][3].state = 1
    grid[1][3].state = 1
    return grid


def main():
    print("Welcome to Conway's Game of Life!")
    # create a one hundred by one hundred grid of cells
    grid: list = []
    for i in range(20):
        new = []
        for j in range(20):
            new.append(cell(0))
        grid.append(new)
    
    # allow the user to input the initial state of the grid
    spawn_glider(grid)

    complete = True
    while complete == False:

        print("Enter a x coordinate: ", end="")
        x = int(input())
        while x < 0 or x >= len(grid):
            print("Invalid x coordinate. Enter a x coordinate: ", end="")
            x = int(input())
        
        print("Enter a y coordinate: ", end="")
        y = int(input())
        while y < 0 or y >= len(grid[0]):
            print("Invalid y coordinate. Enter a y coordinate: ", end="")
            y = int(input())

        # if the cell's state is zero, flip it to one. If it is one, flip it to zero.
        if grid[x][y].getState() == 0:
            grid[x][y].state = 1
        else:
            grid[x][y].state = 0

        print("Current State: ")
        display_grid(grid)
        print("Enter another coordinate? N to stop")
        response = input()
        if response == "N":
            complete = True

    print("Current State: ")
    display_grid(grid)
 
    # # of frames?
    # set output file
 
    plt.show()

    # run the game
    import time

    plt.plot()
    # plt.show()

    for i in range(100):
        clear()
        grid = update_grid(grid)
        print("\n----------------------------\n")
        display_grid(grid)
        # update the plot
        plt.show()
        time.sleep(0.1)


def update_grid(grid) -> None:
    # update the grid
    new_grid: list = []
    for i in range(len(grid)):
        new_grid.append([])
        for j in range(len(grid[0])):
            new_grid[i].append(cell(0))
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # count the number of neighbors
            neighbors = 0
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if x == i and y == j:
                        continue
                    if x < 0 or x >= len(grid):
                        continue
                    if y < 0 or y >= len(grid[0]):
                        continue
                    neighbors += grid[x][y].getState()
            # apply the rules of the game
            if grid[i][j].getState() == 0:
                if neighbors == 3:
                    new_grid[i][j].state = 1
            else:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i][j].state = 0
                else:
                    new_grid[i][j].state = 1
    return new_grid

if __name__ == "__main__":
    main()

def isEven(num: int) -> bool:
    last_digit = num % 10

    even_endings = [0, 2, 4, 6, 8]
    if last_digit in even_endings:
        return True
    return False