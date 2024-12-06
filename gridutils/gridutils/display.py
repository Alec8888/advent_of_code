def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))


def print_grid_with_indices(grid):
    """
    Prints a 2D grid with row and column indices.

    Args:
        grid (list of list): The grid to print.

    Example:
        Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        Output:
          0 1 2
        0 1 2 3
        1 4 5 6
        2 7 8 9
    """
    # Print column headers
    col_headers = "  " + " ".join(map(str, range(len(grid[0]))))
    print(col_headers)

    # Print rows with row indices
    for i, row in enumerate(grid):
        print(f"{i} " + " ".join(map(str, row)))
