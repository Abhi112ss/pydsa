METADATA = {
    "id": 300,
    "name": "Longest Increasing Subsequence",
    "slug": "longest-increasing-subsequence",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "binary_search", "patience_sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest strictly increasing subsequence in a given integer array.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest strictly increasing subsequence using 
    the patience sorting algorithm with binary search.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest strictly increasing subsequence.

    Examples:
        >>> solve([10, 9, 2, 5, 3, 7, 101, 18])
        4
        >>> solve([0, 1, 0, 3, 2, 3])
        4
        >>> solve([7, 7, 7, 7, 7, 7, 7])
        1
    """
    if not nums:
        return 0

    # tails[i] will store the smallest tail of all increasing subsequences of length i+1.
    # This array will always be sorted, allowing for binary search.
    tails: list[int] = []

    for num in nums:
        # Binary search to find the smallest element in tails >= num
        # We use a manual implementation of bisect_left
        low = 0
        high = len(tails)
        
        while low < high:
            mid = (low + high) // 2
            if tails[mid] < num:
                low = mid + 1
            else:
                high = mid
        
        # If low is equal to the length of tails, it means num is larger than 
        # any element in tails, so we extend the longest subsequence found so far.
        if low == len(tails):
            tails.append(num)
        else:
            # Otherwise, we replace the existing tail at index 'low' with 'num'
            # to maintain the smallest possible tail for a subsequence of that length.
            tails[low] = num

    return len(tails)
