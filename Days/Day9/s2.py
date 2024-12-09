import os
print(f"Current working directory: {os.getcwd()}")

from typing import List, Tuple, Dict

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
    return decoded_disk, file_info

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
            res += int(char) * i
    return res

def get_fragged_blocks(disk, size, file_pos):
    for i in range(len(disk)):
        if i >= file_pos:
            break
        if disk[i] == '.':
            if all(disk[j] == '.' for j in range(i, i + size) if j < len(disk)):
                return i
    return None

def move_blocks(disk, file_info):
    for file_id in reversed(list(file_info.keys())):
        blocks_needed = file_info[file_id][1]
        file_pos = file_info[file_id][0]

        free_space_pos = get_fragged_blocks(disk, blocks_needed, file_pos)
        # print(f'free space: id:{file_id} blocks_needed:{blocks_needed} free_space_pos:{free_space_pos}')
        if free_space_pos is not None:
            for i in range(free_space_pos, free_space_pos + blocks_needed):
                disk[i] = file_id
            for i in range(file_pos, file_pos + blocks_needed):
                disk[i] = '.'
        # print(f'processed file: {file_id}{disk}')


example_path = r'.\Days\Day9\example.txt'
puzzle_input = r'.\Days\Day9\input.txt'

disk_map = load_puzzle_from_file(puzzle_input)
# print(f'disk_map: {disk_map}')

disk, file_info = decode_disk_map(disk_map)
print(f'decoded_disk: {disk}')
# print(f'file_info: {file_info}')

move_blocks(disk, file_info)
# print(f'Moved blocks: {disk}')

checksum = calculate_checksum(disk)
print(f'checksum: {checksum}')