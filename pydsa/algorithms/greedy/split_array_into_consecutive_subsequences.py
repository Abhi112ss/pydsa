METADATA = {
    "id": 659,
    "name": "Split Array into Consecutive Subsequences",
    "slug": "split-array-into-consecutive-subsequences",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "hash_map", "heap"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if an array can be split into one or more subsequences such that each subsequence consists of at least three consecutive integers.",
}

def solve(nums: list[int]) -> bool:
    """
    Args:
        nums: A list of integers.

    Returns:
        True if the array can be split into consecutive subsequences of length at least 3, False otherwise.
    """
    frequency_map = {}
    end_map = {}

    for number in nums:
        frequency_map[number] = frequency_map.get(number, 0) + 1

    for number in nums:
        if frequency_map[number] == 0:
            continue

        if end_map.get(number - 1, 0) > 0:
            frequency_map[number] -= 1
            end_map[number - 1] -= 1
            end_map[number] = end_map.get(number, 0) + 1
        elif frequency_map.get(number + 1, 0) > 0 and frequency_map.get(number + 2, 0) > 0:
            frequency_map[number] -= 1
            frequency_map[number + 1] -= 1
            frequency_map[number + 2] -= 1
            end_map[number + 2] = end_map.get(number + 2, 0) + 1
        else:
            return False

    return True