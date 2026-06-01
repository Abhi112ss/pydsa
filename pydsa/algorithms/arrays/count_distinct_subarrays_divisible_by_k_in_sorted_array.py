METADATA = {
    "id": 3729,
    "name": "Count Distinct Subarrays Divisible by K in Sorted Array",
    "slug": "count-distinct-subarrays-divisible-by-k-in-sorted-array",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "hash_map", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Count the number of subarrays whose sum is divisible by k in a given sorted array.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Counts the number of subarrays whose sum is divisible by k.

    Args:
        nums: A list of integers representing a sorted array.
        k: The divisor.

    Returns:
        The total count of subarrays whose sum is divisible by k.

    Examples:
        >>> solve([4, 5, 0, -2, -3, 1], 5)
        7
        >>> solve([5], 9)
        0
    """
    # remainder_counts stores the frequency of each prefix sum modulo k.
    # We initialize with {0: 1} to account for subarrays starting from index 0.
    remainder_counts: dict[int, int] = {0: 1}
    
    current_prefix_sum = 0
    total_count = 0
    
    for num in nums:
        current_prefix_sum += num
        
        # Calculate the remainder. In Python, % operator on negative numbers 
        # returns a result in [0, k-1], which is exactly what we need.
        remainder = current_prefix_sum % k
        
        # If this remainder has been seen before, it means the sum of the 
        # elements between the previous occurrence and now is divisible by k.
        if remainder in remainder_counts:
            total_count += remainder_counts[remainder]
            remainder_counts[remainder] += 1
        else:
            remainder_counts[remainder] = 1
            
    return total_count
