METADATA = {
    "id": 3645,
    "name": "Maximum Total from Optimal Activation Order",
    "slug": "maximum-total-from-optimal-activation-order",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the maximum total value achievable by activating elements in an optimal sequence where each activation provides a benefit based on previously activated elements.",
}

def solve(values: list[int], multipliers: list[int]) -> int:
    """
    Calculates the maximum total value achievable by activating elements in an optimal order.
    
    The problem implies that when an element is activated, it contributes its own value 
    plus a bonus derived from the multipliers applied to previously activated elements.
    To maximize the total, we want to pair larger multipliers with larger values 
    or strategically order them to maximize the cumulative sum.

    Args:
        values: A list of integers representing the base values of elements.
        multipliers: A list of integers representing the multipliers applied to 
            the current value based on the sequence.

    Returns:
        The maximum total value achievable.

    Examples:
        >>> solve([1, 2, 3], [1, 2, 3])
        14
        >>> solve([10, 20], [1, 5])
        120
    """
    n = len(values)
    if n == 0:
        return 0

    # Sort values to allow for optimal greedy/DP selection
    # We sort values to ensure that when we pick a subset, we pick the largest ones
    sorted_values = sorted(values)
    sorted_multipliers = sorted(multipliers)

    # dp[j] will store the maximum total value using a subset of size j
    # This is a variation of the knapsack/subset selection problem
    # where the order of multipliers matters.
    # However, the optimal strategy for a fixed set of values and multipliers
    # is to pair the largest multiplier with the largest value.
    
    # Since the problem asks for the maximum total from an optimal activation order,
    # and the multipliers are applied to the sequence, the total sum is 
    # Sum(values[i] * multipliers[sequence_index[i]])
    
    # To maximize Sum(V_i * M_j), we use the Rearrangement Inequality:
    # The sum is maximized when both sequences are sorted in the same order.
    
    total_sum = 0
    # We pair the largest available values with the largest available multipliers
    # to maximize the product sum.
    for i in range(n):
        total_sum += sorted_values[i] * sorted_multipliers[i]
        
    return total_sum
