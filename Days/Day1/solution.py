import heapq
from collections import Counter

def part1(input):
    # Part 1 ------------------------------------
    left_list: list = []
    left_heap = []
    right_list: list = []
    right_heap = []
    heapPushCount: int = 0
    with open(input) as file:
        for line in file:
            left, right = line.split()

            left_list.append(int(left))
            left_heap.append(int(left))
            right_list.append(int(right))
            right_heap.append(int(right))


    heapq.heapify(left_heap)
    heapq.heapify(right_heap)

    result: int = 0
    diff_count = 0
    while left_heap and right_heap:
        left = heapq.heappop(left_heap)
        right = heapq.heappop(right_heap)
        diff = abs(left - right)
        # print(diff)
        result = result + diff
        diff_count += 1

    # print(f'diff count: {diff_count}')
    return result

# input_filePath = 'C:\dev\AdventOfCode\Day1\day1 input.txt'
# print(part1(input_filePath))

# # Part Two -------------------------------------------
# right_freq = Counter(right_list)

# similarity_score = 0

# for num in left_list:
#     similarity_score += num * right_freq[num]

# print(f'Similarity Score: {similarity_score}')
