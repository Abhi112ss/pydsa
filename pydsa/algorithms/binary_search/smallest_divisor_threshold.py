METADATA = {
    "id": 1283,
    "name": "Find the Smallest Divisor Given a Threshold",
    "slug": "find-the-smallest-divisor-given-a-threshold",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n log(max(nums)))",
    "space_complexity": "O(1)",
    "description": "Find the smallest divisor such that the sum of the division results (rounded up) is less than or equal to a given threshold.",
}

import math

def solve(nums: list[int], threshold: int) -> int:
    """
    Finds the smallest divisor such that the sum of the division results 
    (rounded up) is less than or equal to the threshold.

    Args:
        nums: A list of positive integers.
        threshold: An integer representing the maximum allowed sum.

    Returns:
        The smallest integer divisor that satisfies the condition.

    Examples:
        >>> solve([1, 2, 5, 9], 6)
        5
        >>> solve([44, 22, 33, 11, 1], 5)
        44
    """
    # The smallest possible divisor is 1.
    # The largest useful divisor is the maximum element in the array,
    # because any divisor larger than max(nums) will result in a sum of len(nums).
    low = 1
    high = max(nums)
    ans = high

    while low <= high:
        mid = (low + high) // 2
        
        # Calculate the sum of division results rounded up.
        # Using (num + mid - 1) // mid is an efficient way to compute ceil(num / mid)
        # without floating point precision issues.
        current_sum = 0
        for num in nums:
            current_sum += (num + mid - 1) // mid
        
        # If the sum is within the threshold, this divisor is a candidate.
        # We try to find a smaller divisor by searching the left half.
        if current_sum <= threshold:
            ans = mid
            high = mid - 1
        else:
            # If the sum exceeds the threshold, the divisor is too small.
            # We must increase the divisor by searching the right half.
            low = mid + 1
            
    return ans
