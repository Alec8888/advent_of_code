import pytest
from Days.Day11.solution import solution

def test_part1():
    assert solution(25) == 183620

def test_part2():
    assert solution(75) == 220377651399268

if __name__ == "__main__":
    pytest.main()