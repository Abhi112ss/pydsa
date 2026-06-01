METADATA = {
    "id": 2367,
    "name": "Number of Arithmetic Triplets",
    "slug": "number-of-arithmetic-triplets",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_set", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of unique triplets (i, j, k) such that nums[j] - nums[i] == diff and nums[k] - nums[j] == diff.",
}

def solve(nums: list[int], diff: int) -> int:
    """
    Counts the number of arithmetic triplets in a strictly increasing array.

    An arithmetic triplet is a set of indices (i, j, k) such that 
    i < j < k and nums[j] - nums[i] == diff and nums[k] - nums[j] == diff.

    Args:
        nums: A strictly increasing integer array.
        diff: The required difference between consecutive elements in the triplet.

    Returns:
        The total count of arithmetic triplets found.

    Examples:
        >>> solve([0, 1, 4, 6, 7, 10], 3)
        2
        >>> solve([4, 5, 6, 7, 8, 9], 2)
        2
    """
    # Convert the list to a set for O(1) average time complexity lookups
    num_set = set(nums)
    triplet_count = 0

    for num in nums:
        # For each number, check if the two subsequent values required 
        # to form an arithmetic progression exist in the set.
        # If num + diff and num + 2*diff are present, we found a triplet.
        if (num + diff) in num_set and (num + 2 * diff) in num_set:
            triplet_count += 1

    return triplet_count
