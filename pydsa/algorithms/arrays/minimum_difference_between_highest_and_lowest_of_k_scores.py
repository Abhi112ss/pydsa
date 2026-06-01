METADATA = {
    "id": 1984,
    "name": "Minimum Difference Between Highest and Lowest of K Scores",
    "slug": "minimum-difference-between-highest-and-lowest-of-k-scores",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "sliding_window"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum difference between the highest and lowest scores among any k scores selected from the array.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the minimum difference between the highest and lowest scores among any k scores.

    Args:
        nums: A list of integers representing scores.
        k: The number of scores to select.

    Returns:
        The minimum possible difference between the maximum and minimum score in a subset of size k.

    Examples:
        >>> solve([9, 4, 1, 7], 2)
        3
        >>> solve([9, 4, 1, 7], 3)
        3
    """
    # Sorting allows us to ensure that for any contiguous window of size k,
    # the difference between the first and last element is the difference 
    # between the minimum and maximum of that subset.
    nums.sort()
    
    n = len(nums)
    # Initialize min_diff with a large value. 
    # Since scores are non-negative, float('inf') is a safe upper bound.
    min_diff = float('inf')
    
    # Use a sliding window of size k.
    # The window starts at index i and ends at index i + k - 1.
    for i in range(n - k + 1):
        current_diff = nums[i + k - 1] - nums[i]
        if current_diff < min_diff:
            min_diff = current_diff
            
    return int(min_diff)
