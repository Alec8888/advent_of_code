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
        print(' '.join(map(str, row)))

def simulate_bots(grid, bots):
    for i in range(100):
        print(f'After {i + 1} sec: ')
        for bot in bots:
            x, y = bot[0]
            dx, dy = bot[1]
            new_x = x + dx
            new_y = y + dy

            if new_y >= len(grid):
                new_y = new_y - len(grid)
            elif new_y < 0:
                new_y = len(grid) + new_y

            if new_x >= len(grid[0]):
                new_x = new_x - len(grid[0])
            elif new_x < 0:
                new_x = len(grid[0]) + new_x

            grid[y][x] -= 1
            grid[new_y][new_x] += 1
            bot[0] = (new_x, new_y)
        # log bots and grid here
    return grid, bots

def calc_safety_factor(grid):
    x_mid = len(grid[0]) // 2
    y_mid = len(grid) // 2
    score = 0

    # Q1
    q1_bots = 0
    for i in range(y_mid):
        for j in range(x_mid):
            q1_bots += grid[i][j]
    
    # Q2
    q2_bots = 0
    for i in range(y_mid):
        for j in range(x_mid + 1, len(grid[0])):
            q2_bots += grid[i][j]

    # Q3
    q3_bots = 0
    for i in range(y_mid + 1):
        for j in range(x_mid):
            q3_bots += grid[i][j]
    
    # Q4
    q4_bots = 0
    for i in range(y_mid):
        for j in range(x_mid + 1, len(grid[0])):
            q4_bots += grid[i][j]

    score = q1_bots * q2_bots * q3_bots * q4_bots

    return score
    

path = r'.\Days\Day14\example.txt'
bots = load_robots(path)
grid = grid_build(7, 11)
grid = place_bots(grid, bots)
print_grid(grid)
grid, bots = simulate_bots(grid, bots)
print_grid(grid)

safety_score = calc_safety_factor(grid)
print(f'safety score: {safety_score}')

# print_bot_info(bots)

