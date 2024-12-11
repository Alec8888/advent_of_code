import math

def sol_1(puzzle_input):

    # Read input
    with open(puzzle_input) as f:
        stones = [int(stone) for stone in f.read().strip().split()]

    multiply_cache = {}
    spilt_cache = {}
    digits_cache = {}

    def split_num_digits_in_half(n, digit_count):
        half_digits = digit_count // 2
        divisor = 10 ** half_digits

        left = n // divisor
        right = n % divisor
        return left, right

    def count_digits(n):
        if n == 0:
            return 1
        digit_count = math.floor(math.log10(n)) + 1
        return digit_count

    def blink(stones):
        new_stones = []
        for stone in stones:
            if stone in digits_cache:
                l = digits_cache[stone]
            else:
                digits = count_digits(stone)
                digits_cache[stone] = digits
                l = digits

            if stone == 0:
                new_stones.append(1)
            elif l % 2 == 0:
                if stone in spilt_cache:
                    left, right = spilt_cache[stone]
                else:
                    left, right = split_num_digits_in_half(stone, l)
                    spilt_cache[stone] = (left, right)
                new_stones.append(left)
                new_stones.append(right)
            else:
                if stone in multiply_cache:
                    new_stones.append(multiply_cache[stone])
                else:
                    product = stone * 2024
                    multiply_cache[stone] = product
                    new_stones.append(product)
        return new_stones

    print(f'{stones}')
    blinks = 25
    prev_count = 0
    for i in range(blinks):
        stones = blink(stones)
        # stones = blink2(stones)
        # print(f'i:{i} stones: {stones}')
        stone_count = len(stones)
        # print(f'{stones}')
        print(f'Blink {i + 1}: Stone count: {stone_count} diff: {stone_count - prev_count}')
        prev_count = stone_count

    # Final count of stones
    print(f'Total stones after {blinks} blinks: {len(stones)}')

puzzle_input = r'.\Days\Day11\input.txt'
example_input2 = r'.\Days\Day11\example2.txt'
sol_1(puzzle_input)












    # def get_evens(len_stones):
    #     even_indices = []
    #     for i in range(len_stones):
    #         if stones[i] == 0:
    #             continue
    #         if count_digits(stones[i]) % 2 == 0:
    #             even_indices.append(i)
    #     return even_indices
    
    # def blink2(stones):
    #     len_stones = len(stones)
    #     even_indices = get_evens(len_stones)
    #     new_len = len_stones + len(even_indices)
    #     new_list = [0] * new_len

    #     j = 0
    #     for i in range(len_stones):
    #         digits = count_digits(stones[i])
    #         if stones[i] == 0:
    #             new_list[j] = 1
    #         elif i in even_indices:
    #             # split
    #             new_list[j], new_list[j+1] = split_num_digits_in_half(stones[i], digits)
    #             j += 1 # skip the new even
    #         else:
    #             new_list[j] = stones[i] * 2024 # can we optimize this, cache or precompute?
    #         j += 1
    #     return new_list

    # # Store stones as integers for better performance
    # stones = list(map(int, input_data))
