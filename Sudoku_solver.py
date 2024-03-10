def is_valid_move(grid, row, col, number):
    # Check if the number is not already present in the current row
    for x in range(9):
        if grid[row][x] == number:
            return False

    # Check if the number is not already present in the current column
    for x in range(9):
        if grid[x][col] == number:
            return False

    # Find the top-left corner of the current subgrid (3x3)
    corner_row = row - row % 3
    corner_col = col - col % 3

    # Check if the number is not already present in the current subgrid
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False

    # If the number is not present in the current row, column, or subgrid, it's a valid move
    return True


def solve(grid, row, col):
    # If we have reached the end of the grid, return True (base case)
    if col == 9:
        if row == 8:
            return True

        # Move to the next row and start from the first column
        row += 1
        col = 0

    # If the current cell is not empty, move to the next cell
    if grid[row][col] > 0:
        return solve(grid, row, col + 1)

    # Try numbers from 1 to 9 in the current cell
    for num in range(1, 10):
        # If the current number is a valid move, place it in the cell
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num

            # Recursively solve the Sudoku puzzle for the next cell
            if solve(grid, row, col + 1):
                return True

        # If placing the current number doesn't lead to a solution, backtrack
        grid[row][col] = 0

    # If no number leads to a solution, return False (backtrack)
    return False


# Example Sudoku grid to solve
grid = [
    [8, 0, 1, 3, 0, 0, 9, 0, 0],
    [0, 4, 9, 0, 0, 0, 0, 5, 1],
    [2, 5, 6, 8, 9, 0, 4, 0, 0],
    [0, 1, 5, 6, 8, 0, 0, 4, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 8, 0, 0, 0, 4, 1, 9, 7],
    [1, 0, 2, 0, 7, 9, 0, 0, 0],
    [0, 6, 0, 5, 3, 8, 0, 0, 0],
    [0, 0, 8, 0, 6, 0, 0, 3, 4]
]

# Solve the Sudoku puzzle
if solve(grid, 0, 0):
    # Print the solved Sudoku grid
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
else:
    print("No Solution for this Sudoku!")
