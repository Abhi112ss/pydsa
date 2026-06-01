METADATA = {
    "id": 3162,
    "name": "Find the Number of Good Pairs I",
    "slug": "find-the-number-of-good-pairs-i",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "counting"],
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
    # frequency_map stores the count of each number encountered so far
    frequency_map: dict[int, int] = {}
    good_pairs_count: int = 0

    for num in nums:
        # If the number has been seen before, every previous occurrence 
        # forms a new 'good pair' with the current element.
        if num in frequency_map:
            current_count = frequency_map[num]
            good_pairs_count += current_count
            frequency_map[num] = current_count + 1
        else:
            frequency_map[num] = 1

    return good_pairs_count
