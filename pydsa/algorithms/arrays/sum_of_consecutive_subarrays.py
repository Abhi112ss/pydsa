METADATA = {
    "id": 3284,
    "name": "Sum of Consecutive Subarrays",
    "slug": "sum_of_consecutive_subarrays",
    "category": "Math",
    "aliases": [],
    "tags": ["prefix_sum", "math", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the sum of all possible consecutive subarrays of a given array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the sum of all possible consecutive subarrays of the input array.

    The total sum can be calculated by determining how many subarrays each 
    element `nums[i]` belongs to. An element at index `i` (0-indexed) is 
    part of a subarray if the subarray starts at any index from `0` to `i` 
    and ends at any index from `i` to `n-1`.

    Args:
        nums: A list of integers.

    Returns:
        The sum of all consecutive subarrays.

    Examples:
        >>> solve([1, 2, 3])
        20
        # Subarrays: [1], [2], [3], [1,2], [2,3], [1,2,3]
        # Sums: 1 + 2 + 3 + 3 + 5 + 6 = 20
        >>> solve([1, 1, 1])
        6
    """
    total_sum = 0
    n = len(nums)

    for i in range(n):
        # An element at index i is included in all subarrays that:
        # 1. Start at index j, where 0 <= j <= i (i + 1 choices)
        # 2. End at index k, where i <= k < n (n - i choices)
        # Total occurrences of nums[i] = (i + 1) * (n - i)
        occurrences = (i + 1) * (n - i)
        total_sum += nums[i] * occurrences

    return total_sum
