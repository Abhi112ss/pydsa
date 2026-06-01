METADATA = {
    "id": 2950,
    "name": "Number of Divisible Substrings",
    "slug": "number-of-divisible-substrings",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "hash_map", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Count the number of substrings whose sum is divisible by k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the number of substrings whose sum is divisible by k.

    The algorithm uses the prefix sum property: if (prefix_sum[j] - prefix_sum[i]) % k == 0,
    then prefix_sum[j] % k == prefix_sum[i] % k. We track the frequency of each 
    remainder encountered so far to count valid pairs.

    Args:
        nums: A list of integers.
        k: The divisor.

    Returns:
        The total count of substrings whose sum is divisible by k.

    Examples:
        >>> solve([4, 5, 0, -2, -3, 1], 5)
        7
        >>> solve([1, 2, 3], 3)
        2
    """
    # remainder_counts stores how many times a specific remainder has occurred.
    # We initialize with {0: 1} to account for substrings starting from index 0.
    remainder_counts: dict[int, int] = {0: 1}
    
    current_prefix_sum = 0
    total_divisible_substrings = 0
    
    for num in nums:
        current_prefix_sum += num
        
        # Calculate remainder and normalize it to be within [0, k-1]
        # This handles negative sums correctly in Python (e.g., -1 % 5 = 4)
        remainder = current_prefix_sum % k
        
        # If this remainder has been seen before, every previous occurrence 
        # marks the start of a valid substring ending at the current index.
        if remainder in remainder_counts:
            total_divisible_substrings += remainder_counts[remainder]
            remainder_counts[remainder] += 1
        else:
            remainder_counts[remainder] = 1
            
    return total_divisible_substrings
