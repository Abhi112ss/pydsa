METADATA = {
    "id": 3334,
    "name": "Find the Maximum Factor Score of Array",
    "slug": "find-the-maximum-factor-score-of-array",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum factor score of a triplet (a, b, c) such that a divides b and b divides c, where the score is the product of the triplet.",
}

import math

def solve(nums: list[int]) -> int:
    """
    Finds the maximum factor score of a triplet (nums[i], nums[j], nums[k]) 
    such that nums[i] divides nums[j] and nums[j] divides nums[k].
    The score is defined as nums[i] * nums[j] * nums[k].

    Args:
        nums: A list of integers.

    Returns:
        The maximum factor score found.

    Examples:
        >>> solve([2, 4, 8, 16])
        1024
        >>> solve([1, 2, 3, 4, 5, 6])
        48
    """
    # Sort the array to ensure that if i < j < k, then nums[i] <= nums[j] <= nums[k].
    # This simplifies the divisibility check as we only need to check if 
    # larger numbers are divisible by smaller ones.
    nums.sort()
    n = len(nums)
    max_score = -1

    # Iterate through all possible triplets (i, j, k) where i < j < k.
    # Since the array is sorted, we check if nums[j] % nums[i] == 0 
    # and nums[k] % nums[j] == 0.
    for i in range(n):
        for j in range(i + 1, n):
            # Optimization: If nums[j] is not divisible by nums[i], 
            # this j cannot be the middle element for this i.
            if nums[j] % nums[i] == 0:
                for k in range(j + 1, n):
                    # Check if the third element is divisible by the second.
                    if nums[k] % nums[j] == 0:
                        current_score = nums[i] * nums[j] * nums[k]
                        if current_score > max_score:
                            max_score = current_score
                            
    return max_score
