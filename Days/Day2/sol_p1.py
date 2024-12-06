# one report per line
# each report is a list of levels separated by spaces
# Report safety relies on two constraints
# 1. levels within a report must increase or decrease
# 2. adjacent levels diff must be >= 1 and <= 3
# return number of safe reports

safe_count: int = 0
with open('C:\dev\AdventOfCode\Day 2\input.txt') as file:

    for line in file:
        report = line.split()

        # convert from str to int
        report = [int(level) for level in line.split()]

        unsafe = False
        decreasing: bool = False
        increasing: bool = False
        prev_level = None
        for level in report:
            if prev_level == None:
                prev_level = level
                continue

            # Acend or Decend not set yet
            if not (decreasing or increasing):
                if prev_level == level:
                    unsafe = True
                    break
                if prev_level < level:
                    increasing = True
                else: # already checked equality
                    decreasing = True

            # process list
            if decreasing and (prev_level < level):
                unsafe = True
            if increasing and (prev_level > level):
                unsafe = True
            level_diff = abs(prev_level - level)
            if (level_diff < 1) or (level_diff > 3):
                unsafe = True

            prev_level = level

        if not unsafe:
            safe_count += 1

print(f'Safe reports: {safe_count}')


