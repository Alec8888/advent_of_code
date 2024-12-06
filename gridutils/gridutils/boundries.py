def detect_out_of_bounds(grid, i, j):
    """
    Checks if given pos is out of bounds of the grid.
    """
    return i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0])