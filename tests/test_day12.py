import pytest
from Days.Day12.s import solution

abc = r'C:\dev\AdventOfCode\Days\Day12\example.txt'
xoxox = r'.\Days\Day12\e2.txt'
eShape = r'.\Days\Day12\eshape.txt'
ab = r'.\Days\Day12\ab.txt'
puzzle = r'.\Days\Day12\input.txt'
large = r'.\Days\Day12\elarge.txt'
matt = r'.\Days\Day12\matt_input.txt'



def test_part2_abc():
    assert solution(abc) == 80

def test_part2_xoxo():
    assert solution(xoxox) == 436

def test_part2_eshape():
    assert solution(eShape) == 236

def test_part2_ab():
    assert solution(ab) == 368

def test_part2_large():
    assert solution(large) == 1206

def test_part2_puzzle():
    assert solution(puzzle) == 902742

def test_part2_puzzle():
    assert solution(matt) == 901100


if __name__ == "__main__":
    pytest.main()