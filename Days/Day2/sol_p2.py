
safe_count: int = 0
# with open(r'C:\dev\AdventOfCode\Day 2\input.txt') as file:

with open(r'C:\dev\AdventOfCode\Day 2\test_input.txt') as file:
    for line in file:
        report = line.split()

        # convert from str to int
        report = [int(level) for level in line.split()]

        unsafe = 0
        activated_dampener = False
        decreasing: bool = False
        increasing: bool = False
        prev_level = None
        for i, level in enumerate(report):
            if prev_level == None:
                prev_level = level
                continue

            # first level was removed so skip forward
            if i == 1 and activated_dampener:
                prev_level = level
                decreasing = increasing = False
                continue

            # Acend or Decend not set yet
            if not (decreasing or increasing):
                if prev_level == level:
                    unsafe += 1
                    break
                if prev_level < level:
                    increasing = True
                else: # already checked equality
                    decreasing = True

            # process list
            if decreasing and (prev_level < level):
                unsafe += 1
            if increasing and (prev_level > level):
                unsafe += 1
            level_diff = abs(prev_level - level)
            if (level_diff < 1) or (level_diff > 3):
                unsafe += 1

            # remove first unsafe level, does that do it?
            if (not activated_dampener) and (unsafe == 1):
                activated_dampener = True
                continue
            prev_level = level

        if (unsafe == 0) or ((unsafe == 1) and activated_dampener):
            safe_count += 1

print(f'Safe reports: {safe_count}')


