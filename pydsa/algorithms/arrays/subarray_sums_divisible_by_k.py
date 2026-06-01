METADATA = {
    "id": 974,
    "name": "Subarray Sums Divisible by K",
    "slug": "subarray-sums-divisible-by-k",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "hash_map", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Find the total number of non-empty subarrays that have a sum divisible by k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the number of subarrays whose sum is divisible by k using prefix sums and remainders.

    Args:
        nums: A list of integers.
        k: The divisor.

    Returns:
        The total count of subarrays whose sum is divisible by k.

    Examples:
        >>> solve([4, 5, 0, -2, -3, 1], 5)
        7
        >>> solve([5], 9)
        0
    """
    # remainder_counts stores the frequency of each remainder encountered so far.
    # We initialize with {0: 1} because a prefix sum that is directly divisible by k
    # (remainder 0) represents a valid subarray starting from index 0.
    remainder_counts: dict[int, int] = {0: 1}
    
    current_prefix_sum = 0
    total_subarrays = 0
    
    for num in nums:
        current_prefix_sum += num
        
        # Calculate the remainder of the current prefix sum.
        # In Python, the % operator handles negative numbers correctly for this problem
        # (e.g., -2 % 5 = 3), ensuring the remainder is always in [0, k-1].
        remainder = current_prefix_sum % k
        
        # If this remainder has been seen before, it means the sum of the elements
        # between the previous occurrence and the current index is a multiple of k.
        if remainder in remainder_counts:
            total_subarrays += remainder_counts[remainder]
            remainder_counts[remainder] += 1
        else:
            remainder_counts[remainder] = 1
            
    return total_subarrays
