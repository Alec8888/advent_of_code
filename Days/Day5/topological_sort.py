import re

example_path = r'C:\dev\AdventOfCode\Days\Day5\example.txt'
input_path = r'C:\dev\AdventOfCode\Days\Day5\input.txt'

# read input
with open(example_path, "r") as file:
    puzzle = file.read()

sections = puzzle.strip().split("\n\n")

# Parse rules
rules = []
if len(sections) > 0:
    rule_sec = sections[0].strip()
    for line in rule_sec.split("\n"):
        match = re.match(r'(\d+)\|(\d+)', line)
        if match:
            rules.append((int(match.group(1)), int(match.group(2))))

# Parse updates
updates = []
if len(sections) > 1:
    update_sec = sections[1].strip()
    for update in update_sec.split('\n'):
        pages = [int(page) for page in update.split(',') if page.strip().isdigit()]
        updates.append(pages)

print(f'rules: {rules}')
print(f'updates: {updates}')

# Identify valid updates
valid_updates = []
invalid_updates = []
for update in updates:
    # index map
    page_indices = {page: i for i, page in enumerate(update)}
    # check rules
    adheres_to_rules = True
    for pre_req, page in rules:
        if page in update and pre_req in update and page_indices[pre_req] >= page_indices[page]:
            invalid_updates.append(update)
            adheres_to_rules = False
            break
    if adheres_to_rules:
        valid_updates.append(update)

print(f'valid_updates: {valid_updates}')
print(f'invalid_updates: {invalid_updates}')

valid_sum = sum(update[len(update) // 2] for update in valid_updates)
print(f'valid_sum: {valid_sum}')

import networkx as nx
import matplotlib.pyplot as plt
corrected_updates = []
for update in invalid_updates:  
    G = nx.DiGraph()
    G.add_nodes_from(update)

    # edges, only add edges with both page in update
    for rule in rules:
        p1, p2 = rule
        if p1 in update and p2 in update:
            G.add_edge(p1, p2)

    # Display Graph
    pos = {node: (i, 0) for i, node in enumerate(update)} # horizontal layout
    nx.draw(G, pos, with_labels=True)
    plt.title("Invalid Update")
    plt.show()

    sorted_update = list(nx.topological_sort(G))
    corrected_updates.append(sorted_update)

    # Display Graph
    pos = {node: (i, 0) for i, node in enumerate(sorted_update)} # horizontal layout
    nx.draw(G, pos, with_labels=True)
    plt.title("Corrected Update")
    plt.show()

corrected_sum = sum(update[len(update) // 2] for update in corrected_updates)

print(f'corrected_updates: {corrected_updates}')
print(f'corrected_sum: {corrected_sum}')
# sum should be exampe: 123 puzzle: 6370