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
        if puzzle[i][j] == 'A':
            # in bounds?
            if j - 1 >= 0 and j + 1 < len(puzzle[i]) and i - 1 >= 0 and i + 1 < len(puzzle):
                # (top left, bottom left, top right, bottom right)
                # forwards 
                if puzzle[i-1][j-1] == 'M' and puzzle[i+1][j-1] == 'M'and puzzle[i-1][j+1] == 'S' and puzzle[i+1][j+1] == 'S':
                    count += 1
                # backwards
                if puzzle[i-1][j-1] == 'S' and puzzle[i+1][j-1] == 'S'and puzzle[i-1][j+1] == 'M' and puzzle[i+1][j+1] == 'M':
                    count += 1
                # upside down
                if puzzle[i-1][j-1] == 'S' and puzzle[i+1][j-1] == 'M'and puzzle[i-1][j+1] == 'S' and puzzle[i+1][j+1] == 'M':
                    count += 1
                if puzzle[i-1][j-1] == 'M' and puzzle[i+1][j-1] == 'S'and puzzle[i-1][j+1] == 'M' and puzzle[i+1][j+1] == 'S':
                    count += 1
                    


print(f'count: {count}')

