import re

example_path = r'C:\dev\AdventOfCode\Days\Day5\example.txt'
input_path = r'C:\dev\AdventOfCode\Days\Day5\input.txt'


with open(input_path, "r") as file:
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

valid_updates = []
invalid_updates = []

for update in updates:
    is_valid_update = True
    for prereq, page in rules:
        if prereq in update and page in update:
            if update.index(prereq) > update.index(page):
                is_valid_update = False
                break
    if is_valid_update:
        valid_updates.append(update)
    else:
        invalid_updates.append(update)

prereqs = {}
for prereq, page in rules:
    if page not in prereqs:
        prereqs[page] = []
    prereqs[page].append(prereq)

def fix_invalid_update(update, prereqs):
    page_indexes = {page: i for i, page in enumerate(update)}
    
    for page in update:
        if page in prereqs:
            for prereq in prereqs[page]:
                if prereq in page_indexes:
                    if page_indexes[page] > page_indexes[prereq]:
                        update.remove(page)
                        prereq_index = update.index(prereq)
                        update.insert(prereq_index, page)
                        page_indexes = {page: i for i, page in enumerate(update)}
    return update

fixed_updates = [fix_invalid_update(update, prereqs) for update in invalid_updates]

valid_sum = sum(update[len(update) // 2] for update in valid_updates)

invalid_sum = sum(update[len(update) // 2] for update in fixed_updates)

print(f'rules: {rules}')
print(f'updates: {updates}')
print(f'invalid_updates: {invalid_updates}')
print(f'fixed_updates: {fixed_updates}')
print(f'valid_updates: {valid_updates}')
print(f'valid_sum: {valid_sum}')
print(f'invalid_sum: {invalid_sum}')
