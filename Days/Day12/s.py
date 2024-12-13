def get_neighbors(x, y, grid):
    neighbors = []
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == grid[x][y]:  # Check bounds
            neighbors.append((nx, ny))
    return neighbors

def build_region(x, y, grid, visited, region_char):
    if visited[x][y]:
        return []
    
    visited[x][y] = True
    region = [(x, y)]
    
    # Explore neighbors
    for nx, ny in get_neighbors(x, y, grid):
        if not visited[nx][ny] and grid[nx][ny] == region_char:  # Same character
            region.extend(build_region(nx, ny, grid, visited, region_char))
    
    return region

def find_regions(grid):
    visited = [[False for _ in row] for row in grid]
    regions = {} 
    region_count = {}

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if not visited[x][y]: 
                region_char = grid[x][y]
                region = build_region(x, y, grid, visited, region_char)
                if region:
                    region_count[region_char] = region_count.get(region_char, 0) + 1
                    region_key = f"{region_char}{region_count[region_char]}"
                    regions[region_key] = region
    
    return regions

def print_grid(grid):
    for row in grid:
        print(' '.join(row))

def perimeter(region):
    perimeter = 0
    near_plants = {0: 4, 1: 3, 2: 2, 3: 1, 4: 0}
    for i, j in region:
        up = (i - 1, j)
        down = (i + 1, j)
        left = (i, j - 1)
        right = (i, j + 1)
        near = 0
        if up in region:
            near += 1
        if down in region:
            near += 1
        if left in region:
            near += 1
        if right in region:
            near += 1
        perimeter += near_plants[near]
    # print(f'perimeter ({region}): {perimeter}')
    return perimeter

def calculate_price(regions):
    price = 0
    for region_key, region in regions.items():
        r_price = len(region) * perimeter(region)
        price += r_price
    return price

def get_region_walls(region):
    # vert
    walls = []
    for i, j in region:
        # left
        if (i, j - 1) not in region:
            walls.append((i, j - 1, 'v') )
        # right 
        if (i, j + 1) not in region:
            walls.append((i, j + 1, 'v') )
        # up
        if (i - 1, j) not in region:
            walls.append((i - 1, j, 'h') )
        # down
        if (i + 1, j) not in region:
            walls.append((i + 1, j, 'h') )
    # print(f'walls: {walls}')
    return walls

def count_corners(region):
    corners = set()
    diag_corners = set()
    for i, j in region:
        # ways to have a corner
        up, down, left, right, diag1, diag2 = (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i + 1, j + 1), (i - 1, j + 1)
        # .A X
        #  X A
        if right not in region and down not in region and diag1 in region:
            diag_corners.add(((i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)))
        #  X A
        # .A X
        if up not in region and right not in region and diag2 in region:
            diag_corners.add(((i - 1, j), (i - 1, j + 1), (i, j), (i, j + 1)))

        # tl
        #   X
        # X A.
        if left not in region and up not in region:
            corners.add(((i - 1, j - 1), (i - 1, j), (i, j - 1), (i, j)))

        # tl
        # X A
        # A A.
        elif left in region and up in region and (i - 1, j - 1) not in region:
            corners.add(((i - 1, j - 1), (i - 1, j), (i, j - 1), (i, j)))

        # tr
        #  X
        # .A X
        if right not in region and up not in region:
            corners.add(((i - 1, j), (i - 1, j + 1), (i, j), (i, j + 1)))
        
        #  A X
        # .A A
        elif right in region and up in region and (i - 1, j + 1) not in region:
            corners.add(((i - 1, j), (i - 1, j + 1), (i, j), (i, j + 1)))

        # bl
        # X A.
        #   X
        if left not in region and down not in region:
            corners.add(((i, j - 1), (i, j), (i + 1, j - 1), (i + 1, j)))

        # bl
        # A A.
        # X A
        elif left in region and down in region and (i + 1, j - 1) not in region:
            corners.add(((i, j - 1), (i, j), (i + 1, j - 1), (i + 1, j)))

        # br
        # .A X
        #  X
        if right not in region and down not in region:
            corners.add(((i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)))

        # br
        # .A A
        #  A X
        elif right in region and down in region and (i + 1, j + 1) not in region:
            corners.add(((i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)))

    
    return len(corners) + len(diag_corners)

def solution(puzzle_input):
    print('Starting solution -------------------------------------------\n')
    with open(puzzle_input) as f:
        garden = [list(line.strip()) for line in f]

    regions = find_regions(garden)

    price2 = 0
    side_count = 0
    for id, region in regions.items():
        walls = get_region_walls(region)
        print(f'\n{id} walls: {walls}')

        print(f'\nCounting Sides for {id}')
        count_corners
        side_count_region = count_corners(region)
        area = len(region)
        price = area * side_count_region
        print(f'price {price} = area {area} * sides {side_count_region}')
        price2 += price

        side_count += side_count_region
        print(f'\n\nside_count: {id} {side_count_region} total running sides: {side_count}')

    price = calculate_price(regions)
    print(f"\nPrice: {price}")
    print(f"Price2: {price2}")

    return price2

abc = r'.\Days\Day12\example.txt'
xoxox = r'.\Days\Day12\e2.txt'
eShape = r'.\Days\Day12\eshape.txt'
ab = r'.\Days\Day12\ab.txt'
large = r'.\Days\Day12\elarge.txt'

puzzle = r'.\Days\Day12\input.txt'
sol2 = solution(puzzle)
print(f'sol2: {sol2}')