METADATA = {
    "id": 2908,
    "name": "Minimum Sum of Mountain Triplets I",
    "slug": "minimum-sum-of-mountain-triplets-i",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "brute_force"],
    "difficulty": "medium",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(1)",
    "description": "Find the minimum sum of a mountain triplet (i, j, k) such that i < j < k and nums[i] < nums[j] > nums[k].",
}

def solve(nums: list[int]) -> int:
    """
    Finds the minimum sum of a mountain triplet (nums[i] + nums[j] + nums[k])
    where 0 <= i < j < k < n and nums[i] < nums[j] and nums[k] < nums[j].

    Args:
        nums: A list of integers representing the mountain elements.

    Returns:
        The minimum sum of a mountain triplet, or -1 if no such triplet exists.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        -1
        >>> solve([5, 4, 3, 2, 1])
        -1
        >>> solve([1, 5, 2])
        8
        >>> solve([2, 4, 3, 1, 5])
        8
    """
    n = len(nums)
    min_sum = float('inf')
    found = False

    # Iterate through every possible middle element (the peak of the mountain)
    # The peak must have at least one element to its left and one to its right.
    for j in range(1, n - 1):
        peak_val = nums[j]
        
        # Find the smallest element to the left of j that is smaller than nums[j]
        min_left = float('inf')
        for i in range(j):
            if nums[i] < peak_val:
                if nums[i] < min_left:
                    min_left = nums[i]
        
        # Find the smallest element to the right of j that is smaller than nums[j]
        min_right = float('inf')
        for k in range(j + 1, n):
            if nums[k] < peak_val:
                if nums[k] < min_right:
                    min_right = nums[k]
        
        # If both a valid left and right neighbor were found, calculate the sum
        if min_left != float('inf') and min_right != float('inf'):
            current_sum = min_left + peak_val + min_right
            if current_sum < min_sum:
                min_sum = current_sum
                found = True

    return int(min_sum) if found else -1
