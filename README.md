# SudokuSolver
Tiny python script to solve sudoku puzzles

Fooling around with backtracking/dfs to solve sudoku puzzles - currently brute forces

WIP, running will solve problem_grid hardcoded at the top

TODOs:
    
    # Considering a preprocess step and having a "candidate bank" for each blank space, where we hold all possible solutions, then upon hitting each square we can just pull from the candidate box
    # There would also need to be some way to update candidate boxes upon spaces being "confirmed"
    # This could be a way to improve performance
    
    # Some sort of UI -> text based or graphic
    
    # Let user choose to import grid from a file
    
    # Create a random puzzle grid if they want
    
    # UI that shows the puzzle, and graphically shows the puzzle being solved?
    # Allow the user to click squares to up/down the number they want there, letting them do puzzle
    # Button to auto solve at any time
