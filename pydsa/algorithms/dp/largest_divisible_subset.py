METADATA = {
    "id": 368,
    "name": "Largest Divisible Subset",
    "slug": "largest_divisible_subset",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the largest subset of a given set of integers such that every pair (a, b) in the subset satisfies a % b == 0 or b % a == 0.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Finds the largest subset where every pair of elements satisfies the divisibility property.

    Args:
        nums: A list of integers.

    Returns:
        A list of integers representing the largest divisible subset.

    Examples:
        >>> solve([1, 2, 3])
        [1, 2] (or [1, 3])
        >>> solve([1, 2, 4, 8])
        [1, 2, 4, 8]
    """
    if not nums:
        return []

    # Sorting allows us to only check if nums[i] % nums[j] == 0 where i > j
    nums.sort()
    n = len(nums)
    
    # dp[i] stores the size of the largest divisible subset ending with nums[i]
    dp = [1] * n
    # predecessors[i] stores the index of the previous element in the subset to reconstruct the path
    predecessors = [-1] * n

    max_size = 0
    last_index = 0

    for i in range(n):
        for j in range(i):
            # If nums[i] is divisible by nums[j], it can extend the subset ending at j
            if nums[i] % nums[j] == 0:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    predecessors[i] = j
        
        # Keep track of the global maximum size and its ending index
        if dp[i] > max_size:
            max_size = dp[i]
            last_index = i

    # Reconstruct the subset using the predecessors array
    result = []
    current = last_index
    while current != -1:
        result.append(nums[current])
        current = predecessors[current]

    return result[::-1]
