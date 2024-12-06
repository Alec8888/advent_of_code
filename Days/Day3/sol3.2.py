import re

def get_valid_mul(filePath):
    mul_pattern = r'(?:mul\(\d{1,3},\d{1,3}\))|(?:don\'t\(\))|(?:do\(\))'
    with open(filePath) as file:
        corrupted_text = file.read()
    return re.findall(mul_pattern, corrupted_text)

# valid_mul = get_valid_mul('C:\dev\AdventOfCode\Day3\example2.txt')
valid_mul = get_valid_mul('C:\dev\AdventOfCode\Day3\input.txt')

print(valid_mul)

sum_products = 0
disabled = False
for op in valid_mul:
    if re.match(r'don\'t\(\)', op):
        disabled = True
    if re.match(r'do\(\)', op):
        disabled = False
    if re.match(r'mul\(\d{1,3},\d{1,3}\)', op) and not disabled:
        mutiplicand, multiplier = re.findall(r'(\d{1,3})', op)
        product = int(mutiplicand) * int(multiplier)
        sum_products += product

print(sum_products)