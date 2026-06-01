METADATA = {
    "id": 2470,
    "name": "Number of Subarrays With LCM Equal to K",
    "slug": "number-of-subarrays-with-lcm-equal-to-k",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "sliding_window", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Count the number of non-empty subarrays where the Least Common Multiple of all elements equals k.",
}

import math

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the number of subarrays whose Least Common Multiple (LCM) is exactly k.

    Args:
        nums: A list of positive integers.
        k: The target LCM value.

    Returns:
        The total count of subarrays with LCM equal to k.

    Examples:
        >>> solve([2, 3, 4], 6)
        1
        >>> solve([1, 1, 1], 1)
        6
    """
    total_count = 0
    n = len(nums)

    for start_index in range(n):
        current_lcm = nums[start_index]
        
        # If the starting element itself is not a divisor of k, 
        # no subarray starting here can ever have an LCM equal to k.
        if k % current_lcm != 0:
            continue

        # Check if the single element subarray matches k
        if current_lcm == k:
            total_count += 1

        # Expand the subarray from the start_index to the right
        for end_index in range(start_index + 1, n):
            next_val = nums[end_index]
            
            # If the next element is not a divisor of k, any subarray 
            # containing it will have an LCM that is not a divisor of k.
            if k % next_val != 0:
                break
            
            # Update the running LCM using the formula: lcm(a, b) = (a * b) // gcd(a, b)
            current_lcm = (current_lcm * next_val) // math.gcd(current_lcm, next_val)
            
            # If the running LCM exceeds k, further expansion won't help
            if current_lcm > k:
                break
            
            # If the current running LCM matches the target k, increment count
            if current_lcm == k:
                total_count += 1
                
    return total_count
