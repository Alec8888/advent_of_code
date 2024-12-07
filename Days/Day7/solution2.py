def load_puzzle_input(file_path):
    with open(file_path) as file:
        return [[int(part.rstrip(':')) for part in line.strip().split()] for line in file]

def valid_operator_combo_exists(operands, target, current_value=0, index=0):
    """
    try all operator combos
    Returns True if target reached
    """
    if index == 0: # start with first operand
        current_value = operands[0]
        index += 1

    if index == len(operands): # used all operands
        return current_value == target # did we find a valid operator combo?

    # try + for this operator pos
    if valid_operator_combo_exists(operands, target, current_value + operands[index], index + 1):
        return True

    # try * for this operator pos
    if valid_operator_combo_exists(operands, target, current_value * operands[index], index + 1):
        return True
    
    # try ||
    concat_val = int(str(current_value) + str(operands[index]))
    if valid_operator_combo_exists(operands, target, concat_val, index + 1):
        return True
        
    return False

def solve_puzzle(puzzle):
    """
    For each calibration equation, evaluate if target can be reached.
    Returns sum of reachable targets.
    """
    valid_totals = []
    for row in puzzle:
        target = row[0]
        operands = row[1:]
        if valid_operator_combo_exists(operands, target):
            valid_totals.append(target)
    return sum(valid_totals)

example_path = r'C:\dev\AdventOfCode\Days\Day7\example.txt'
input_path = r'C:\dev\AdventOfCode\Days\Day7\input.txt'

# load puzzle input
puzzle_input = load_puzzle_input(input_path)

print("Puzzle:")
for calibration_equation in puzzle_input:
    print(f'{calibration_equation}')

puzzle_solution = solve_puzzle(puzzle_input)
print(f'puzzle_solution: {puzzle_solution}')
