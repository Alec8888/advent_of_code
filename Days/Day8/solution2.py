def load_puzzle_input(file_path):
    with open(file_path) as file:
        return [list(line.strip()) for line in file]

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def find_value_all(grid, target_val):
    positions = []
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == target_val:
                positions.append((i, j))
    return positions

def detect_out_of_bounds(grid, i, j):
    """
    Checks if given pos is out of bounds of the grid.
    """
    return i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0])

def show_anti_nodes_on_grid(grid, antinodes):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if (i, j) in antinodes:
                print('#', end=' ')
            else:
                print(val, end=' ')
        print()  # Newline after each row

def create_dict_char_positions(grid):
    chars_mapped = set()
    char_pos_map = {}
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if not char == '.' and not char in chars_mapped:
                char_pos_map[char] = find_value_all(grid, char)
                chars_mapped.add(char)
    return char_pos_map

def find_anti_nodes(grid, char_pos_list):
    anti_nodes = set()
    # for each pos, find ij diff and 
    for i, pos in enumerate(char_pos_list):
        for j in range(i + 1, len(char_pos_list)):
            pos1 = char_pos_list[i]
            pos2 = char_pos_list[j]
            rise = pos2[1] - pos1[1]
            run = pos2[0] - pos1[0]

            # find all anti_nodes along the line
            k = 1
            while True:
                antinode1 = (pos1[0] - k * run, pos1[1] - k * rise)
                antinode2 = (pos2[0] + k * run, pos2[1] + k * rise)
                if not detect_out_of_bounds(grid, antinode1[0], antinode1[1]) and antinode1 not in char_pos_list:
                    anti_nodes.add(antinode1)
                if not detect_out_of_bounds(grid, antinode2[0], antinode2[1]) and antinode2 not in char_pos_list:
                    anti_nodes.add(antinode2)
                if detect_out_of_bounds(grid, antinode1[0], antinode1[1]) and detect_out_of_bounds(grid, antinode2[0], antinode2[1]):
                    break
                k += 1

            # antennas pos that are on an antenna line are anti_nodes in part 2
            anti_nodes.add(pos1)
            anti_nodes.add(pos2)
            
    return anti_nodes

example_path = r'C:\dev\AdventOfCode\Days\Day8\example.txt'
input_path = r'C:\dev\AdventOfCode\Days\Day8\input.txt'

puzzle = load_puzzle_input(input_path)
print('Antennas------------------------------------')
print_grid(puzzle)

# create a map of char and their locations
char_pos_map = create_dict_char_positions(puzzle)
# print(char_pos_map)

# for each char in char_pos_map, find the anti_nodes 
anti_nodes = set()
for char in char_pos_map:
    char_anti_nodes = find_anti_nodes(puzzle, char_pos_map[char])
    count_found_anti_nodes = len(char_anti_nodes)
    # print(f'found this many anti nodes: {count_found_anti_nodes}')
    anti_nodes.update(char_anti_nodes)


# print(f'anti_nodes: {anti_nodes}')
print('AnitNodes------------------------------------')
show_anti_nodes_on_grid(puzzle, anti_nodes)

puzzle_solution = len(anti_nodes)
print(f'puzzle_solution: {puzzle_solution}')