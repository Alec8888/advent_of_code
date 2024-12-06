def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))


def print_grid_with_indices(grid):
    """
    Prints a 2D grid with row and column indices, maintaining alignment even for multi-digit indices.

    Args:
        grid (list of list): The grid to print.

    Example:
        Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        Output:
             0   1   2
        0    1   2   3
        1    4   5   6
        2    7   8   9
    """
    if not grid or not grid[0]:
        print("Empty grid")
        return

    # Determine the width of the largest element in the grid
    max_cell_width = max(len(str(cell)) for row in grid for cell in row)

    # Determine the width of the largest row index
    max_index_width = len(str(len(grid) - 1))

    # Print column headers with padding
    col_headers = " " * (max_index_width + 1) + " ".join(f"{col:>{max_cell_width}}" for col in range(len(grid[0])))
    print(col_headers)

    # Print rows with row indices and padded cells
    for i, row in enumerate(grid):
        row_str = " ".join(f"{cell:>{max_cell_width}}" for cell in row)
        print(f"{i:>{max_index_width}} {row_str}")
