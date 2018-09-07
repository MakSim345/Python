import os
import sys
"""

"""

def get_row_d(grid, col):
    new_grid = []
    sum = 0
    _grid = []

    for i in grid:
        new_grid.append(str(i))    
        _grid.append(i)

    if (col == 0):
        sum = _grid[0] + _grid[1]
    elif (col == len(_grid) - 1): 
        sum = _grid[-2] + _grid[-1]
    else:
        sum = _grid[col-1] + _grid[col] + _grid[col+1]
    # print "sum = ", sum
    new_grid.append("=" + str(sum))
    return new_grid

def get_current_row_d(grid, col):
    # print "row:", row
    sum = 0
    new_grid = []
    _grid = []
    for i in grid:
        new_grid.append(str(i))
        _grid.append(i)
    
    new_grid[col] = '*'

    if (col == 0):
        sum = _grid[1]
    elif (col == len(_grid) - 1): 
        sum = _grid[-2]
    else:
        sum = _grid[col-1] + _grid[col+1]
    # print "sum = ", sum
    new_grid.append("=" + str(sum))
    return new_grid


def get_row(grid, col):
    sum = 0
    _grid = []

    for i in grid:
        _grid.append(i)

    if (col == 0):
        sum = _grid[0] + _grid[1]
    elif (col == len(_grid) - 1): 
        sum = _grid[-2] + _grid[-1]
    else:
        sum = _grid[col-1] + _grid[col] + _grid[col+1]       
    return sum

def get_current_row(grid, col):
    sum = 0
    _grid = []
    for i in grid:
        _grid.append(i)
    
    if (col == 0):
        sum = _grid[1]
    elif (col == len(_grid) - 1): 
        sum = _grid[-2]
    else:
        sum = _grid[col-1] + _grid[col+1]
    return sum

def count_neighbours(grid, row, col):
    #print  "\nlen(grid):", len(grid)
    #print "row:", row
    #print "col:", col
    _retVal = 0

    if (row > 0):
        #print "top row:    ", # grid [col-1]
        #print get_row(grid[row-1], col)
        _retVal = get_row(grid[row-1], col)
    
    # print "current row:", # grid [col]
    # print get_current_row(grid[row], col)
    _retVal = _retVal + get_current_row(grid[row], col)
    
    if (row < (len(grid)-1)):        
        #print "bottom row: ", # grid [col+1]
        #print get_row(grid[row+1], col)
        _retVal = _retVal + get_row(grid[row+1], col)
    
    return _retVal

# main entrance point:
if __name__ == '__main__' or __name__ == sys.argv[0]:
    print "Main program start."
    print ""
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"

    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
    
    print "Main program end."




