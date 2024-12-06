from gridutils import detect_out_of_bounds, find_value, print_grid, print_grid_with_indices
import time

start_time = time.time()

def load_puzzle_input(file_path):
    """Create a List[][]"""
    with open(file_path) as file:
        return [list(line.strip()) for line in file]

def guard_turn(current_dir):
    return {'^': '>', '>': 'v', 'v': '<', '<': '^'}[current_dir]

def guard_move(current_pos, current_dir):
    """Returns new position after one move"""
    i, j = current_pos
    if current_dir == '^':
        return i - 1, j
    if current_dir == 'v':
        return i + 1, j
    if current_dir == '<':
        return i, j - 1
    if current_dir == '>':
        return i, j + 1

def guard_walks_part1(grid, start_pos, start_dir):
    """Returns visited positions count"""
    visited_positions = set()
    pos = start_pos
    dir = start_dir

    while True:
        new_pos = guard_move(pos, dir)
        i, j = new_pos
        if detect_out_of_bounds(grid, i, j):
            break
        elif grid[i][j] == "#":
            dir = guard_turn(dir)
        else:
            visited_positions.add(new_pos)
            pos = new_pos
    return len(visited_positions)

example_path = r'C:\dev\AdventOfCode\Days\Day6\example.txt'
input_path = r'C:\dev\AdventOfCode\Days\Day6\input.txt'
grid = load_puzzle_input(input_path)

directions = {'^', '<', '>', 'v'}
guard_start_pos = find_value(grid, directions)
guard_start_dir = grid[guard_start_pos[0]][guard_start_pos[1]]

# print_grid(grid)
print_grid_with_indices(grid)
print(f'guard_start_pos: {guard_start_pos}')
print(f'guard_start_dir: {guard_start_dir}')

visited_positions_count = guard_walks_part1(grid, guard_start_pos, guard_start_dir)
print(f'puzzle answer: {visited_positions_count}')

end_time = time.time()
elapsed_time = end_time - start_time
print(f'Part 1 runtime: {elapsed_time:.4f}')

# part 2
# for each pos, add an obstruction, then detect if guard is in a cycle
print("\nPart 2...")
start_time = time.time()
def guard_walks_part2_detect_cycle(grid, start_pos, start_dir):
    """Returns True if cycle"""
    visited_positions = set()
    pos = start_pos
    dir = start_dir
    visited_positions = {(pos, dir)}

    while True:
        new_pos = guard_move(pos, dir)
        if (new_pos, dir) in visited_positions:
            return True
        i, j = new_pos
        if detect_out_of_bounds(grid, i, j):
            break
        elif grid[i][j] == "#":
            dir = guard_turn(dir)
        else:
            visited_positions.add((new_pos, dir))
            pos = new_pos
    return False

cycle_causing_obstructions = set()
for i, row in enumerate(grid):
    for j, char in enumerate(row):
        if grid[i][j] == "#":
            continue
        if grid[i][j] in directions:
            continue
        grid[i][j] = '#' # place obstacle
        if guard_walks_part2_detect_cycle(grid, guard_start_pos, guard_start_dir):
            cycle_causing_obstructions.add((i, j))
            grid[i][j] = '.' # reset grid
            continue
        grid[i][j] = '.' # reset grid

puzzle_answer = len(cycle_causing_obstructions)

print(f'puzzle_answer: {puzzle_answer}')

end_time = time.time()
elapsed_time = end_time - start_time
print(f'Part 2 runtime: {elapsed_time:.4f}')




