import re

def get_valid_mul(filePath):
    mul_pattern = r'(mul\(\d{1,3},\d{1,3}\))'
    with open(filePath) as file:
        corrupted_text = file.read()
    return re.findall(mul_pattern, corrupted_text)

# valid_mul = get_valid_mul('C:\dev\AdventOfCode\Day3\example.txt')
valid_mul = get_valid_mul('C:\dev\AdventOfCode\Day3\input.txt')

# print(valid_mul)

def multiply(mul_list):
    sum_products = 0
    for mul in mul_list:
        mutiplicand, multiplier = re.findall(r'(\d{1,3})', mul)
        print(f'mutiplicand: {mutiplicand} * multiplier: {multiplier}')
        product = int(mutiplicand) * int(multiplier)
        print(f'product: {product}')
        sum_products += product
    return sum_products

print(multiply(valid_mul))