METADATA = {
    "id": 2341,
    "name": "Maximum Number of Pairs in Array",
    "slug": "maximum_number_of_pairs_in_array",
    "category": "array",
    "aliases": [],
    "tags": ["hash_map", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of equal-value pairs that can be formed from an array and the count of leftover elements.",
}

import sys
from typing import List, Dict

def solve() -> None:
    """Read an integer array from standard input and output the maximum number of
    equal-value pairs that can be formed and the number of leftover elements.

    Input format:
        n
        a1 a2 ... an

    Output format:
        pairs leftover

    Example:
        Input:
            7
            1 3 2 3 2 2 2
        Output:
            3 1
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return
    # First token is the length of the array; the rest are the elements.
    array_length: int = int(data[0])
    numbers: List[int] = list(map(int, data[1:1 + array_length]))

    # Count occurrences of each number.
    frequency_map: Dict[int, int] = {}
    for value in numbers:
        frequency_map[value] = frequency_map.get(value, 0) + 1

    total_pairs: int = 0
    for count in frequency_map.values():
        total_pairs += count // 2  # each pair consumes two equal numbers

    leftover_elements: int = len(numbers) - total_pairs * 2
    sys.stdout.write(f"{total_pairs} {leftover_elements}")
