# Conway's Game of Life takes place on an infinite two-dimensional board of square cells.
# Each cell is either dead or alive, and at each tick, the following rules apply:

# Any live cell with less than two live neighbours dies.
# Any live cell with two or three live neighbours remains living.
# Any live cell with more than three live neighbours dies.
# Any dead cell with exactly three live neighbours becomes a live cell.
# A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

# Implement Conway's Game of Life. It should be able to be initialized with a starting
# list of live cell coordinates and the number of steps it should run for.
# Once initialized, it should print out the board state at each step.
# Since it's an infinite board, print out only the relevant coordinates, i.e.
# from the top-leftmost live cell to bottom-rightmost live cell.

# You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).


import numpy as np


class Cell(object):
    def __init__(self, val, coords):
        self.val = val
        self.coords = coords
        self.neighbours = 0

    def check_neighbors(self, state, m, n):
        # Check neighoring cells and update
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                other_x = self.coords[0] + dx
                other_y = self.coords[1] + dy
                if dx == 0 and dy == 0:
                    continue
                else:
                    if other_x >= 0 and other_x < m and other_y >= 0 and other_y < n:
                        if state[other_x][other_y].val == '*':
                            self.neighbours += 1


def print_state(state, m, n):
    # Print the game's current state
    for i in range(n):
        for j in range(m):
            if state[i][j].val == '*':
                print(state[i][j].val, end =" ")
            else:
                print('.', end =" ")
        print('\n', end ="")
    print('\n')


def find_size(initial_state):
    # Find the needed m,n size of the game's state based on the initial condition
    x_min = min(initial_state, key=lambda item:item[0])[0]
    x_max = max(initial_state, key=lambda item:item[0])[0]
    y_min = min(initial_state, key=lambda item:item[1])[1]
    y_max = max(initial_state, key=lambda item:item[1])[1]
    return (np.subtract(x_max, x_min)+1, np.subtract(y_max, y_min)+1)


def game_policy(state, m ,n):
    # Run one iteration of Conway's game of life
    for i in range(n):
        for j in range(m):
            if state[i][j].val == '*':
                if state[i][j].neighbours < 2:
                    state[i][j].val = '.'
                elif state[i][j].neighbours == 2 or state[i][j].neighbours == 3:
                    pass
                elif state[i][j].neighbours > 3:
                    state[i][j].val = '.'
            else:
                if state[i][j].neighbours == 3:
                    state[i][j].val = '*'
            state[i][j].check_neighbors(state, m, n)
        

def game_of_life(initial_state, steps):
    m,n = find_size(initial_state)
    state = [['.' for i in range(m)] for j in range(n)]

    # Add live cells
    for coords in initial_state:
        state[coords[0]][coords[1]] = '*'

    # Add dead cells
    for i in range(n):
        for j in range(m):
            if state[i][j] == '.':
                state[i][j] = Cell('.', [i,j])
            else:
                state[i][j] = Cell('*', [i,j])

    # Find neighbors
    for i in range(n):
        for j in range(m):
            state[i][j].check_neighbors(state, m, n)

    # Run game
    while steps > 0:
        game_policy(state, m, n)
        print_state(state, m, n)
        steps -= 1


# Driver code
initial_state = [[0,0],[1,0],[1,1],[3,0],[4,4]]
steps = 100
game_of_life(initial_state, steps)