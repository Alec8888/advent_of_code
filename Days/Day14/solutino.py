import re
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")


def load_robots(path):
    bots = [] # (pos), (vel)
    with open(path) as f:
        lines = [line.strip() for line in f]

        pattern = r'p=(\d+),(\d+)\s*v=(-?\d+),(-?\d+)'

        for line in lines:
            match = re.match(pattern, line)
            if match:
                bots.append([((int(match.group(1))), int(match.group(2))),(int(match.group(3)), int(match.group(4)))])
            else:
                logging.error(f"No match found for the line: '{line}'")
    return bots

def print_bot_info(robots):
    for bot in bots:
        print(bot)

def grid_build(rows, cols):
    rows = 7
    cols = 11
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    return grid

def place_bots(grid, bots):
    for bot in bots:
        x, y = bot[0]
        grid[y][x] += 1
    return grid

def print_grid(grid):
    for row in grid:
        print(row)

def simulate_bots(grid, bots):
    for i in range(100):
        print(f'After 1 sec: ')
        for bot in bots:
            x, y = bot[0]
            dx, dy = bot[1]
            if y + dy >= len(grid):
                new_y = (y + dy) - len(grid) 
            else:
                new_y = y + dy
            if x + dx >= len(grid[0]):
                new_x = (x + dx) - len(grid[0])
            else:
                new_x = x + dx

            grid[y][x] -= 1
            grid[new_y][new_x] += 1
            bot[0] = (new_x, new_y)
        # log bots and grid here
    return grid, bots

path = r'.\Days\Day14\example.txt'
bots = load_robots(path)

grid = grid_build(7, 11)

grid = place_bots(grid, bots)
grid, bots = simulate_bots(grid, bots)
print_grid(grid)

# print_bot_info(bots)

