METADATA = {
    "id": 927,
    "name": "Three Equal Parts",
    "slug": "three-equal-parts",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if an array can be partitioned into three contiguous parts with an equal number of ones.",
}

def solve(arr: list[int]) -> bool:
    """
    Args:
        arr: A list of integers consisting of 0s and 1s.

    Returns:
        True if the array can be partitioned into three parts with equal ones, False otherwise.
    """
    total_ones = sum(arr)

    if total_ones % 3 != 0:
        return False

    if total_ones == 0:
        return True

    target_ones = total_ones // 3
    current_ones = 0
    parts_found = 0
    first_part_end = -1
    second_part_end = -1

    for index, value in enumerate(arr):
        current_ones += value
        if current_ones == target_ones and parts_found == 0:
            first_part_end = index
            parts_found = 1
        elif current_ones == 2 * target_ones and parts_found == 1:
            second_part_end = index
            parts_found = 2
            break

    if parts_found < 2:
        return False

    return True