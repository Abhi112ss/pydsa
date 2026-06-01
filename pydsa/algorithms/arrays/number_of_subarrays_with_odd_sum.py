METADATA = {
    "id": 1524,
    "name": "Number of Sub-arrays With Odd Sum",
    "slug": "number-of-sub-arrays-with-odd-sum",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "hash_map", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of non-empty subarrays with an odd sum.",
}

def solve(arr: list[int]) -> int:
    """
    Calculates the total number of subarrays that have an odd sum.

    The algorithm uses the property of prefix sums:
    - A subarray sum (from index i to j) is odd if:
        (prefix_sum[j] - prefix_sum[i-1]) is odd.
    - This happens if one prefix sum is even and the other is odd.

    Args:
        arr: A list of integers.

    Returns:
        The total count of subarrays with an odd sum, modulo 10^9 + 7.

    Examples:
        >>> solve([1, 3, 5])
        4
        >>> solve([2, 4, 6])
        0
        >>> solve([1, 2, 3, 4, 5, 6, 7])
        16
    """
    MODULO = 1_000_000_007
    
    # odd_count tracks how many prefix sums encountered so far were odd
    # even_count tracks how many prefix sums encountered so far were even
    # We start with even_count = 1 because the initial prefix sum (before any elements) is 0 (even)
    odd_count = 0
    even_count = 1
    
    current_prefix_sum = 0
    total_odd_subarrays = 0
    
    for num in arr:
        current_prefix_sum += num
        
        # Check parity of the current prefix sum
        if current_prefix_sum % 2 != 0:
            # If current prefix sum is odd, it forms an odd subarray when 
            # paired with any previous even prefix sum.
            total_odd_subarrays += even_count
            odd_count += 1
        else:
            # If current prefix sum is even, it forms an odd subarray when 
            # paired with any previous odd prefix sum.
            total_odd_subarrays += odd_count
            even_count += 1
            
        # Apply modulo to prevent integer overflow in other languages, 
        # though Python handles large ints, it's good practice for LeetCode.
        total_odd_subarrays %= MODULO
            
    return total_odd_subarrays
