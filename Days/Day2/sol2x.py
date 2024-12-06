safe_count = 0

def is_safe(report):
    decreasing = None

    prev = report[0]

    for i in range(1, len(report)):
        curr = report[i]
        
        diff = abs(prev - curr)
        if diff < 1 or diff > 3:
            return False
        
        if decreasing == None:
            decreasing = prev > curr # false if increasing
        else:
            if decreasing and curr > prev:
                return False
            if not decreasing and curr < prev:
                return False
            
        prev = curr

    return True

def safe_with_dampener(report):
    for i in range(len(report)):
        dampened_report = report[:i] + report[i+1:]
        if is_safe(dampened_report):
            return True
    return False

with open(r'C:\dev\AdventOfCode\Day 2\input.txt') as file:
# with open(r'C:\dev\AdventOfCode\Day 2\test_input.txt') as file:
    for line in file:
        report = [int(level) for level in line.split()]

        if is_safe(report) or safe_with_dampener(report):
            safe_count += 1

print(f'Safe reports: {safe_count}')

