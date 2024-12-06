import pytest 
from Days.Day1.solution import part1

def test_part1_example():
    assert part1('C:\dev\AdventOfCode\Days\Day1\example.txt') == 11

def test_part1_puzzleInput():
    assert part1('C:\dev\AdventOfCode\Days\Day1\input.txt') == 3508942

if __name__ == "__main__":
    pytest.main()