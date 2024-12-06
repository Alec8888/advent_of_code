# build 2d array
puzzle = None

example = 'C:\dev\AdventOfCode\Day4\example.txt'
input = 'C:\dev\AdventOfCode\Day4\input.txt'
with open(input) as file:
    puzzle = [list(line.strip()) for line in file]


for line in puzzle:
    print(line)

print(f'puzzle[0][1]: {puzzle[0][3]}')

# hash map for seen combos
count = 0
for i, l in enumerate(puzzle):
    for j, c in enumerate(l):
        if puzzle[i][j] == 'X':
            # check forward
            if j + 3 < len(puzzle[i]) and puzzle[i][j + 1] == 'M' and puzzle[i][j + 2] == 'A' and puzzle[i][j + 3] == 'S':
                count += 1
            # backwards
            if j - 3 >= 0 and puzzle[i][j - 1] == 'M' and puzzle[i][j - 2] == 'A' and puzzle[i][j - 3] == 'S':
                count += 1
            # vertical down
            if i + 3 < len(puzzle) and puzzle[i + 1][j] == 'M' and puzzle[i + 2][j] == 'A' and puzzle[i + 3][j] == 'S':
                count += 1
            # vertical up
            if i - 3 >= 0 and puzzle[i - 1][j] == 'M' and puzzle[i - 2][j] == 'A' and puzzle[i - 3][j] == 'S':
                count += 1
            # diag right up
            if j + 3 < len(puzzle[i]) and i - 3 >= 0 and puzzle[i - 1][j + 1] == 'M' and puzzle[i - 2][j + 2] == 'A' and puzzle[i - 3][j + 3] == 'S':
                count += 1
            # diag right down
            if j + 3 < len(puzzle[i]) and i + 3 < len(puzzle) and puzzle[i + 1][j + 1] == 'M' and puzzle[i + 2][j + 2] == 'A' and puzzle[i + 3][j + 3] == 'S':
                count += 1
            # diag left up
            if j - 3 >= 0 and i - 3 >= 0 and puzzle[i - 1][j - 1] == 'M' and puzzle[i - 2][j - 2] == 'A' and puzzle[i - 3][j - 3] == 'S':
                count += 1
            # diag left down
            if j - 3 >= 0 and i + 3 < len(puzzle) and puzzle[i + 1][j - 1] == 'M' and puzzle[i + 2][j - 2] == 'A' and puzzle[i + 3][j - 3] == 'S':
                count += 1
print(f'count: {count}')

