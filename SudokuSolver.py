## Zachary Hicks
## This program uses backtracking and brute force to solve Sudoku Puzzles

import time

## The GRID is a 2D array of ints, 9x9. 0 represents a blank space
problem_grid = [[1,0,0, 2,0,0, 0,0,7],
                [0,0,0, 0,0,0, 6,9,0],
                [7,0,0, 3,0,0, 8,0,0],
               
                [5,6,0, 9,0,8, 0,0,0],
                [0,2,0, 7,0,0, 0,0,1],
                [0,0,0, 0,0,0, 0,0,0],
               
                [0,0,4, 0,7,0, 0,0,5],
                [2,5,0, 8,0,0, 9,0,0],
                [0,0,0, 0,4,0, 0,0,0]]

blank_grid = [[0,0,0, 0,0,0, 0,0,0],
              [0,0,0, 0,0,0, 0,0,0],
              [0,0,0, 0,0,0, 0,0,0],
               
              [0,0,0, 0,0,0, 0,0,0],
              [0,0,0, 0,0,0, 0,0,0],
              [0,0,0, 0,0,0, 0,0,0],
               
              [0,0,0, 0,0,0, 0,0,0],
              [0,0,0, 0,0,0, 0,0,0],
              [0,0,0, 0,0,0, 0,0,0]]

# The Solution Grid
grid = problem_grid

# Takes the grid 2d array, and prints it as a square
def printGrid(grid):
    for row in grid:
        print(row)

# From the current position, check candidate against this row
def checkRow(row, guess):
    # check this row for guess
    if guess in grid[row]:
        return False
    return True 

# From the current position, check candidate against this column
def checkCol(col, guess):
    # check this col for guess
    for row in grid:
        if guess is row[col]:
            return False
    return True

# From the current position, check candidate against this box
def checkBox(row, col, guess):
    # from row,col determine what BOX this cell belongs to - top left cell index
    boxRow = int(row/3)*3
    boxCol = int(col/3)*3
    
    # with the top left corner index, we check the 3x3 box for guess
    for i in range(boxRow, boxRow+3):
        for j in range(boxCol, boxCol+3):
            if guess is grid[i][j]:
                return False
    return True

# Wrapper for checks, if any check fails, return false
def checkValid(row, col, guess):
    if not checkRow(row, guess):
        return False
    if not checkCol(col, guess):
        return False
    if not checkBox(row, col, guess):
        return False
    return True
  
# Recursive solve call
# returns False on incomplete, True on complete
def solve(cRow, cCol):
    # If the cell is 0, try to set it
    if grid[cRow][cCol] == 0:
        # for all options 1 to 10
        for guess in range(1,10):
            #print("Row " + str(cRow) + " and Col " + str(cCol) + " with guess " + str(guess))
            # if it can be placed here
            if checkValid(cRow, cCol, guess):
                # place it here
                grid[cRow][cCol] = guess
                
                # check if this is the last spot we have successfully set = finished
                if cRow == 8 and cCol == 8:
                    return True
                
                # done is True when we reach our end case
                done = False
                
                # determine which cell to go to next
                if cCol != 8:
                    done = solve(cRow, cCol + 1 % 9)
                else:
                    done = solve(cRow + 1 % 9, 0)
                
                # if an above solve returned True, we are done
                if done:
                    return True
        # end for
        # If we try all 9 numbers and can not validate, we reset the cell to 0, and go back up one, returning false
        #print("Row " + str(cRow) + " and Col " + str(cCol) + " out of options, set 0, return false")
        grid[cRow][cCol] = 0
        return False
    else: # if the cell already has a value, skip it
        # check if this is the last spot we have successfully set = finished
        if cRow == 8 and cCol == 8:
            return True
        
        # done is True when we reach out end case
        done = False
        
        # determine which cell to go to next
        if cCol != 8:
            done = solve(cRow, cCol + 1 % 9)
        else:
            done = solve(cRow + 1 % 9, 0)
        
        # if an above solve returns True, we are done
        if done:
            return True

# Top Level for solve, takes no arguments and starts stack (you cant overload methods in python curse you Java)
def start_solve():
    return solve(0,0)

### Main Method call. Solves Sudoku grid in global "problem_grid" and completes puzzle in "grid"
def main():
    # generic greeting, and printing the problem puzzle
    print("Hello Solver! Here is the current problem grid to solve:\n")
    printGrid(problem_grid)
    
    # TODOs:
    
    # Something to consider is to preprocess and have a "candidate bank" for each blank space, where we hold all possible solutions, then upon hitting each square we can just pull from the candidate box
    # There would also need to be some way to update candidate boxes upon spaces being "confirmed"
    # This could be a way to improve performance
    
    # Some sort of UI -> text based or graphic
    
    # Let user choose to import grid from a file
    
    # Create a random puzzle grid if they want
    
    # UI that shows the puzzle, and graphically shows the puzzle being solved?
    # Allow the user to click squares to up/down the number they want there, letting them do puzzle
    # Button to auto solve at any time
    
    start_time = time.time()
    
    # solve the grid
    done = start_solve()
    
    end_time = time.time()
    
    if done:
        # the grid is complete, print the solved puzzle
        print("\nSolved in %.2f seconds" % (end_time-start_time)) 
        print("\nHere is the solved grid:\n")
        printGrid(grid)
    else:
        print("Something went wrong: could not solve the grid:\n")
        printGrid(grid)

if __name__ == "__main__":
    main()

