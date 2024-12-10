import matplotlib.pyplot as plt

from typing import List, Tuple, Dict
import networkx as nx

def load_puzzle_input(file_path):
    with open(file_path) as f:
        return [list(map(int, line.strip())) for line in f]
    
def print_grid(grid):
    print('Hiking Map:')
    for row in grid:
        print(" ".join(map(str, row)))
    
def find_value_all(grid, target_val):
    positions = []
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == target_val:
                positions.append((i, j))
    return positions

def get_neighbors_positions(grid, pos):
    neighbors = []
    i, j = pos
    # up, i - 1
    if i - 1 >= 0:
        neighbors.append((i - 1, j))

    # down
    if i + 1 < len(grid):
        neighbors.append((i + 1, j))

    # left
    if j - 1 >= 0:
        neighbors.append((i, j - 1))

    # right
    if j + 1 < len(grid[0]):
        neighbors.append((i, j + 1))
    return neighbors

def get_neighbors_with_valid_slope(map, neighbors, prev_slope):
    neighbors_with_valid_slope = []
    for n in neighbors:
        i, j = n
        # print(f'n: {n} map[i][j]: {map[i][j]} prev_slope: {prev_slope}')
        if map[i][j] == prev_slope + 1:
            neighbors_with_valid_slope.append(n)
    return neighbors_with_valid_slope

def build_graph(map, trailhead, G=None):

    if G is None:
        G = nx.DiGraph()

    ti, tj = trailhead

    tile_elevation = map[ti][tj]
    G.add_node((ti, tj), pos=(tj, -ti), value=tile_elevation)
    
    tile_neighbors = get_neighbors_positions(puzzle, (ti, tj))
    reachable_tiles = get_neighbors_with_valid_slope(map, tile_neighbors, tile_elevation)

    for i, j in reachable_tiles:
        G.add_node((i, j), pos=(j, -i), value=map[i][j])
        G.add_edge((ti, tj), (i, j))
        build_graph(map, (i, j), G)  
    
    return G

def score_trail(trail_graph):
    score = sum(1 for node in trail_graph.nodes if trail_graph.nodes[node]['value'] == 9)
    return score

def display_graph(graph):
    pos = nx.get_node_attributes(graph, 'pos')
    labels = {node: graph.nodes[node]['value'] for node in graph.nodes()}
    plt.figure(figsize=(8, 8))
    nx.draw(graph, pos, with_labels=True, labels=labels, node_size=500, node_color="lightblue", font_size=10)
    plt.show()

def score_all_trailheads(trailheads, show_graph):
    score_sum = 0
    for s in trailheads:
        G = build_graph(puzzle, s)

        if (show_graph): 
            display_graph(G)

        score = score_trail(G)
        # print(f's: {s}, score: {score}')
        score_sum += score

    return score_sum

def score_all_trailheads_part2(trailheads, show_graph):
    score_sum = 0

    for trailhead in trailheads:
        trail = build_graph(puzzle, trailhead)
        show_graph and display_graph(trail)

        d_nodes = [node for node in trail.nodes if trail.nodes[node]['value'] == 9]

        unique_paths = set()

        for d in d_nodes:
            for path in nx.all_simple_paths(trail, source=trailhead, target=d):
                unique_paths.add(tuple(path))

        trailhead_score = len(unique_paths)
        # print(f"Trailhead {trailhead} has a score of {trailhead_score}")

        score_sum += trailhead_score 

    return score_sum

example_path = r'.\Days\Day10\example.txt'
puzzle_input = r'.\Days\Day10\input.txt'

puzzle = load_puzzle_input(puzzle_input)
# print(f'puzzle: {puzzle}')
print_grid(puzzle)

trailheads = find_value_all(puzzle, 0)
print(f'trailheads: {trailheads}')

show_graph = False
# part 1
solution = score_all_trailheads(trailheads, show_graph)
print(f'solution1: {solution}')

# part 2
solution = score_all_trailheads_part2(trailheads, show_graph)
print(f'solution2: {solution}')

# debug stuff
# neighbor_test = get_neighbors_positions(puzzle, (1, 1))
# print(f'neighbor_test: {neighbor_test}')

# valid_tiles = get_neighbors_with_valid_slop(puzzle, neighbor_test, puzzle[1][1])
# print(f'valid_tiles: {valid_tiles}')

# G = build_graph(puzzle, trailheads[0])
# score = score_trail(G)
# print(f'score: {score}')

# pos = nx.get_node_attributes(G, 'pos')
# labels = {node: G.nodes[node]['value'] for node in G.nodes()}
# plt.figure(figsize=(8, 8))
# nx.draw(G, pos, with_labels=True, labels=labels, node_size=500, node_color="lightblue", font_size=10)
# plt.title(f"Trail Graph - Score: {score}", fontsize=16, fontweight="bold")
# plt.show()