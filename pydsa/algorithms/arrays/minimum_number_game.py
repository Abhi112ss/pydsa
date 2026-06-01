METADATA = {
    "id": 2974,
    "name": "Minimum Number Game",
    "slug": "minimum-number-game",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given an even-sized array, return a new array where each element is the minimum of the adjacent pair.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Transforms an even-sized array by replacing each pair of adjacent elements 
    with their minimum value.

    Args:
        nums: A list of integers with an even length.

    Returns:
        A list of integers containing the minimum of each pair.

    Examples:
        >>> solve([1, 2, 3, 4])
        [1, 3]
        >>> solve([10, 5, 20, 15])
        [5, 15]
    """
    result = []
    # Iterate through the array in steps of 2 to process pairs
    for i in range(0, len(nums), 2):
        # Compare the current element with its immediate neighbor
        pair_min = min(nums[i], nums[i + 1])
        result.append(pair_min)
        
    return result
