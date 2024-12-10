import pytest
from Days.Day10.s import solve_part1, solve_part2

def test_part1_example():
    assert solve_part1(r'.\Days\Day10\input.txt') == 674

def test_part2_solution():
    assert solve_part2(r'.\Days\Day10\input.txt') == 1372
