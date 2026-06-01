METADATA = {
    "id": 2179,
    "name": "Count Good Triplets in an Array",
    "slug": "count-good-triplets-in-an-array",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "brute_force"],
    "difficulty": "medium",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(1)",
    "description": "Count the number of triplets (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of good triplets (i, j, k) in the array.
    A triplet is good if i < j < k and nums[i] < nums[j] < nums[k].

    Args:
        nums: A list of integers.

    Returns:
        The total count of good triplets.

    Examples:
        >>> solve([1, 2, 3, 4])
        4
        >>> solve([4, 3, 2, 1])
        0
        >>> solve([1, 3, 2, 4])
        2
    """
    n = len(nums)
    good_triplet_count = 0

    # Iterate through all possible indices i, j, k such that i < j < k
    for i in range(n):
        for j in range(i + 1, n):
            # Optimization: If nums[i] is not less than nums[j], 
            # no need to check any k for this specific (i, j) pair.
            if nums[i] < nums[j]:
                for k in range(j + 1, n):
                    # Check the final condition for a good triplet
                    if nums[j] < nums[k]:
                        good_triplet_count += 1
                        
    return good_triplet_count
