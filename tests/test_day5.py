import pytest 
from Days.Day5.part1 import part1

def test_part1_example():
    assert part1('C:\dev\AdventOfCode\Days\Day5\example.txt') == 9999999999999

# def test_part1_puzzleInput():
#     assert part1('C:\dev\AdventOfCode\Days\Day5\input.txt') == 9999999999999

if __name__ == "__main__":
    pytest.main()