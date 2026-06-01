METADATA = {
    "id": 2448,
    "name": "Minimum Cost to Make Array Equal",
    "slug": "minimum-cost-to-make-array-equal",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum cost to make all elements in an arithmetic progression equal by choosing an optimal target value.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the minimum cost to make all elements in an arithmetic progression equal.
    
    The elements are defined as nums[i] + i * k. To minimize the sum of absolute 
    differences |target - x_i|, the optimal target is the median of the sequence x_i.

    Args:
        nums: A list of integers representing the starting values.
        k: The common difference of the arithmetic progression.

    Returns:
        The minimum total cost as an integer.

    Examples:
        >>> solve([1, 2, 3], 1)
        0
        >>> solve([1, 10, 100], 1)
        99
    """
    n = len(nums)
    # The actual values we are working with are x[i] = nums[i] + i * k.
    # Since nums[i] is non-decreasing and i * k is non-decreasing, 
    # the sequence x[i] is already sorted.
    
    # The median of a sorted array is at index n // 2.
    median_index = n // 2
    median_value = nums[median_index] + median_index * k
    
    total_cost = 0
    
    # Calculate the sum of absolute differences from the median.
    # Cost = sum(|x[i] - median|)
    for i in range(n):
        current_value = nums[i] + i * k
        total_cost += abs(current_value - median_value)
        
    return total_cost
