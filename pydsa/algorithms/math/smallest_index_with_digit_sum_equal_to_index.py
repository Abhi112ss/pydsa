METADATA = {
    "id": 3550,
    "name": "Smallest Index With Digit Sum Equal to Index",
    "slug": "smallest-index-with-digit-sum-equal-to-index",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "brute_force"],
    "difficulty": "easy",
    "time_complexity": "O(n * log10(n))",
    "space_complexity": "O(1)",
    "description": "Find the smallest index i such that the sum of the digits of i is equal to i.",
}

def solve(n: int) -> int:
    """
    Finds the smallest index i (where 1 <= i <= n) such that the sum of 
    the digits of i is equal to i.

    Args:
        n (int): The upper bound of the range to search.

    Returns:
        int: The smallest index satisfying the condition, or -1 if no such index exists.

    Examples:
        >>> solve(10)
        1
        >>> solve(0)
        -1
    """
    # The condition 'sum of digits of i == i' can only be true for single-digit numbers.
    # For any number i >= 10, the sum of its digits is strictly less than i.
    # Proof: Let i = d_k*10^k + ... + d_1*10 + d_0. 
    # Sum of digits = d_k + ... + d_1 + d_0.
    # Since 10^m > 1 for m >= 1, i will always be greater than the sum of its digits for i >= 10.
    
    for current_index in range(1, n + 1):
        # Optimization: If current_index >= 10, the condition sum_digits(i) == i 
        # can never be met. We can break early.
        if current_index >= 10:
            break
            
        digit_sum = 0
        temp_val = current_index
        
        # Calculate sum of digits using modulo and division
        while temp_val > 0:
            digit_sum += temp_val % 10
            temp_val //= 10
            
        if digit_sum == current_index:
            return current_index
            
    return -1
