METADATA = {
    "id": 3149,
    "name": "Find the Minimum Cost Array Permutation",
    "slug": "find-the-minimum-cost-array-permutation",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum cost to permute an array where cost is defined by the sum of absolute differences of adjacent elements.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Finds the permutation of the input array that minimizes the cost.
    The cost is defined as the sum of absolute differences between adjacent elements.
    The minimum cost is achieved when the array is sorted.

    Args:
        nums: A list of integers.

    Returns:
        A list of integers representing the permutation with the minimum cost.

    Examples:
        >>> solve([3, 1, 2])
        [1, 2, 3]
        >>> solve([10, 5, 20])
        [5, 10, 20]
    """
    # The cost function sum(|nums[i] - nums[i+1]|) is minimized 
    # when the elements are in monotonic order (either non-decreasing or non-increasing).
    # Sorting the array provides the non-decreasing order which minimizes the total path.
    
    # Create a copy to avoid mutating the original input if required by caller,
    # though in LeetCode context, returning a new sorted list is standard.
    sorted_nums = sorted(nums)
    
    return sorted_nums
