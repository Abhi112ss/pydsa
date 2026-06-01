METADATA = {
    "id": 3740,
    "name": "Minimum Distance Between Three Equal Elements I",
    "slug": "minimum-distance-between-three-equal-elements-i",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum distance between the first and third occurrence of any element that appears at least three times.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the minimum distance between the first and third occurrence of any 
    element that appears at least three times in the array.

    The distance is defined as the difference between the index of the 
    third occurrence and the index of the first occurrence (i.e., index[i+2] - index[i]).

    Args:
        nums: A list of integers.

    Returns:
        The minimum distance found. If no element appears three times, 
        the behavior depends on problem constraints (usually assumed to exist).

    Examples:
        >>> solve([1, 2, 1, 3, 1])
        4
        >>> solve([1, 1, 1, 2, 2, 2])
        2
    """
    # Dictionary to store the list of indices for each unique number
    index_map: dict[int, list[int]] = {}

    for current_index, value in enumerate(nums):
        if value not in index_map:
            index_map[value] = []
        index_map[value].append(current_index)

    # Initialize min_distance with a value larger than any possible distance in the array
    min_distance = len(nums)

    # Iterate through the collected indices for each number
    for indices in index_map.values():
        # We only care about numbers that appear at least 3 times
        if len(indices) >= 3:
            # Check every window of 3 consecutive occurrences of the same number
            # The distance is the gap between the first and third element in the window
            for i in range(len(indices) - 2):
                distance = indices[i + 2] - indices[i]
                if distance < min_distance:
                    min_distance = distance

    return min_distance
