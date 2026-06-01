METADATA = {
    "id": 1437,
    "name": "Check If All 1's Are at Least Length K Places Away",
    "slug": "check-if-all-1s-are-at-least-length-k-places-away",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "arrays", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if all 1s in a binary array are separated by at least k zeros.",
}

def solve(arr: list[int], k: int) -> bool:
    """
    Checks if all 1s in the array are separated by at least k zeros.

    Args:
        arr: A list of integers containing only 0s and 1s.
        k: The minimum number of zeros required between any two 1s.

    Returns:
        True if all 1s are at least k places away from each other, False otherwise.

    Examples:
        >>> solve([1, 0, 0, 0, 1, 0, 0, 1], 2)
        True
        >>> solve([1, 0, 0, 1, 0, 0, 1], 2)
        False
        >>> solve([1, 1], 1)
        False
    """
    # last_one_index tracks the position of the most recent '1' encountered.
    # Initialized to -float('inf') so the first '1' doesn't trigger a distance check.
    last_one_index = -float('inf')

    for current_index, value in enumerate(arr):
        if value == 1:
            # The distance between two indices i and j is |i - j|.
            # The problem requires at least k zeros between them, 
            # which means the difference in indices must be at least k + 1.
            if current_index - last_one_index <= k:
                return False
            
            # Update the last seen position of '1'
            last_one_index = current_index

    return True
