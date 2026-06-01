METADATA = {
    "id": 334,
    "name": "Increasing Triplet Subsequence",
    "slug": "increasing-triplet-subsequence",
    "category": "Arrays",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].",
}

def solve(nums: list[int]) -> bool:
    """
    Determines if there exists an increasing triplet subsequence in the given list.

    The algorithm uses a greedy approach by maintaining the two smallest values 
    encountered so far that could potentially form the start of an increasing triplet.

    Args:
        nums: A list of integers.

    Returns:
        True if an increasing triplet subsequence exists, False otherwise.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        True
        >>> solve([5, 4, 3, 2, 1])
        False
        >>> solve([2, 1, 5, 0, 4, 6])
        True
    """
    # Initialize the two smallest values to infinity.
    # first_smallest will track the smallest element seen so far.
    # second_smallest will track the smallest element that has a smaller element before it.
    first_smallest = float('inf')
    second_smallest = float('inf')

    for current_num in nums:
        if current_num <= first_smallest:
            # Found a new minimum, update first_smallest.
            first_smallest = current_num
        elif current_num <= second_smallest:
            # current_num is greater than first_smallest but smaller than second_smallest.
            # This updates our potential middle element of the triplet.
            second_smallest = current_num
        else:
            # If current_num is greater than both first_smallest and second_smallest,
            # we have found our third element in the increasing sequence.
            return True

    return False
