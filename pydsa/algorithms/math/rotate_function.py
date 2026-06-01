METADATA = {
    "id": 396,
    "name": "Rotate Function",
    "slug": "rotate-function",
    "category": "Math",
    "aliases": [],
    "tags": ["array", "math", "dynamic-programming"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the maximum value of a function F(k) defined by the sum of elements in an array after k rotations.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum value of the function F(k) using a rolling sum approach.

    The function F(k) represents the sum of (i * nums[i]) after k rotations.
    Instead of recomputing the sum for every k, we observe the difference:
    F(k) = F(k-1) + total_sum - n * nums[n-k]

    Args:
        nums: A list of integers.
        k: The number of rotations to consider (0 <= k < len(nums)).

    Returns:
        The maximum value of F(k) for all k in [0, n-1].

    Examples:
        >>> solve([0, 3, 0], 0)
        3
        >>> solve([5, 1, 1, 1, 1], 0)
        13
    """
    n = len(nums)
    k %= n  # Ensure k is within bounds
    
    current_f = 0
    total_sum = 0
    
    # Calculate F(0) and the total sum of the array in one pass
    for i in range(n):
        current_f += i * nums[i]
        total_sum += nums[i]
        
    max_f = current_f
    
    # Use the mathematical relationship to find F(1) through F(k)
    # Each rotation shifts indices, effectively adding the total sum 
    # and subtracting the contribution of the element that 'wraps around'.
    for i in range(1, k + 1):
        # The element at index (n - i) moves from the end to the front
        # In the context of the formula, we subtract its contribution 
        # relative to its old position and adjust for the shift.
        current_f = current_f + total_sum - n * nums[n - i]
        if current_f > max_f:
            max_f = current_f
            
    return max_f
