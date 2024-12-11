from collections import Counter

def split_num_digits_in_half(n, digit_count):
    half_digits = digit_count // 2
    divisor = 10 ** half_digits
    left = n // divisor
    right = n % divisor
    return left, right

def blink(stones):
    new_stones = Counter()

    for stone, count in stones.items():
        if stone == 0:
            # 0 -> 1
            new_stones[1] += count
        else:
            digits = len(str(stone))
            if digits % 2 == 0:
                # Split
                left, right = split_num_digits_in_half(stone, digits)
                new_stones[left] += count
                new_stones[right] += count
            else:
                # * 2024
                product = stone * 2024
                new_stones[product] += count

    return new_stones

def solution(blinks):
    example_input = r'.\Days\Day11\example2.txt'
    puzzle_input = r'.\Days\Day11\input.txt'
    with open(puzzle_input) as f:
        starting_stones = [int(stone) for stone in f.read().strip().split()]
    stones = Counter(starting_stones)

    # Blinks
    for i in range(blinks):
        stones = blink(stones)
        stone_count = sum(stones.values())
        print(f'Blink {i + 1}: {stone_count} stones')

    total_stones = sum(stones.values())
    print(f'Total stones after {blinks} blinks: {total_stones}')
    return total_stones

solution(75)
