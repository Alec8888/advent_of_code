import os
print(f"Current working directory: {os.getcwd()}")

from typing import List, Tuple, Dict

example_path = r'.\Days\Day9\example.txt'
puzzle_input = r'.\Days\Day9\input.txt'

def load_puzzle_from_file(file_path):
    with open(file_path) as f:
        return [int(block_length) for block_length in f.read().strip()]

def decode_disk_map(disk_map):
    decoded_disk = []
    file_info = {} # fileID: (pos, len)
    file_id = 0
    for i, num in enumerate(disk_map):
        if i % 2 == 0: # file, write it
            file_info[file_id] = (len(decoded_disk), num)
            for _ in range(num):
                decoded_disk.append(file_id)
            file_id += 1
        else:
            for _ in range(num):
                decoded_disk.append('.')
    return decoded_disk

def get_first_fragged_block(disk: List) -> int:
    fragged_block_pos = None
    potential_pos = None
    free_block_seen = False
    free = '.'
    for i, block in enumerate(disk):
        if block != free and free_block_seen:
            fragged_block_pos = potential_pos
            return fragged_block_pos
        if block == free and not free_block_seen:
            free_block_seen = True
            potential_pos = i

    return fragged_block_pos

def defrag(disk: list):
    fragged_block = get_first_fragged_block(disk)
    while fragged_block is not None:
        # search from end of file and 
        for i in range(len(disk) - 1, -1, -1):
            if disk[i] != '.':
                disk[fragged_block] = disk[i]
                disk[i] = '.'
                break
        fragged_block = get_first_fragged_block(disk)

def calculate_checksum(disk):
    res = 0
    for i, char in enumerate(disk):
        if char != '.':
            res += char * i
    return res

def get_fragged_blocks(disk, size, file_pos) -> int: # return pos or None
    free_block_start = None
    free_block_size = 0
    in_a_free_block = False
    for i, block in enumerate(disk):
        if i >= file_pos:
            return None
        if block == '.' and not in_a_free_block:
            in_a_free_block = True
            free_block_size += 1
            free_block_start = i
        if block == '.' and in_a_free_block:
            free_block_size += 1
        if block != '.' and in_a_free_block:
            in_a_free_block = False
            if free_block_size >= size:
                return free_block_start
            
    return free_block_start

# Example ---------------------------------------------------
disk_map = load_puzzle_from_file(example_path)
print(f'disk_map: {disk_map}')

disk = decode_disk_map(disk_map)
print(f'decoded_disk: {disk}')

defrag(disk)
print(f'After block move: {disk}')

checksum = calculate_checksum(disk)
print(f'checksum: {checksum}')

# Puzzle ---------------------------------------------------
disk_map = load_puzzle_from_file(puzzle_input)
# print(f'disk_map: {disk_map}')

disk = decode_disk_map(disk_map)
print(f'decoded_disk: {disk}')

defrag(disk)
# print(f'After block move: {disk}')

checksum = calculate_checksum(disk)
print(f'checksum: {checksum}')

