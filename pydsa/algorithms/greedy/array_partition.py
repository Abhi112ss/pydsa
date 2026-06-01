METADATA = {
    "id": 561,
    "name": "Array Partition",
    "slug": "array_partition",
    "category": "Greedy",
    "aliases": [],
    "tags": ["sorting", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Partition the array into pairs to maximize the sum of the smaller element in each pair.",
}


def solve(nums: list[int]) -> int:
    """Calculate the maximum possible sum of the minimum elements of n/2 pairs.

    Args:
        nums: A list of even length containing integers.

    Returns:
        The maximum sum achievable by pairing the elements such that each pair
        contributes its smaller element to the total.

    Examples:
        >>> solve([1, 4, 3, 2])
        4
        >>> solve([6, 2, 6, 5, 1, 2])
        9
    """
    # Sort the array so that each adjacent pair contains the two closest values.
    nums.sort()
    total_sum = 0
    # Sum every element at an even index; these are the minima of each pair.
    for index in range(0, len(nums), 2):
        total_sum += nums[index]  # add the smaller element of the current pair
    return total_sum