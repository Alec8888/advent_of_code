def find_value(grid, target_val):
    """
    Find first position of a value in a grid.

    Returns:
        tuple: (row, col)
    """
    if not isinstance(target_val, (set, list, tuple)): # if not an iterable, convert to set
        target_vals = {target_val}
    else: # is an iterable so can use set() to conver tot set
        target_vals = set(target_val)

    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val in target_vals:
                return (i, j)
    return None
            
def find_value_all(grid, target_val):
    positions = []
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == target_val:
                positions.append((i, j))
    return positions