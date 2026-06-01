METADATA = {
    "id": 1512,
    "name": "Number of Good Pairs",
    "slug": "number-of-good-pairs",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "arrays", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of pairs (i, j) such that nums[i] == nums[j] and i < j.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the number of good pairs in an integer array.
    A pair (i, j) is good if nums[i] == nums[j] and i < j.

    Args:
        nums: A list of integers.

    Returns:
        The total count of good pairs.

    Examples:
        >>> solve([1, 2, 3, 1, 1, 3])
        4
        >>> solve([1, 1, 1, 1])
        6
        >>> solve([1, 2, 3])
        0
    """
    # Dictionary to store the frequency of each number encountered so far
    counts: dict[int, int] = {}
    good_pairs_count: int = 0

    for number in nums:
        # If the number has been seen before, it can form a pair with 
        # every previous occurrence of itself.
        if number in counts:
            good_pairs_count += counts[number]
            counts[number] += 1
        else:
            # First time seeing this number
            counts[number] = 1

    return good_pairs_count
