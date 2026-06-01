METADATA = {
    "id": 1819,
    "name": "Number of Different Subsequences GCDs",
    "slug": "number-of-different-subsequences-gcds",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "hash-map", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(max_val * log(max_val))",
    "space_complexity": "O(max_val)",
    "description": "Count the number of distinct GCD values that can be formed by any subsequence of the given array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the number of distinct GCD values possible from all subsequences.

    The algorithm uses a frequency array to track existing numbers and then
    iterates through all possible GCD values from 1 to the maximum value in the array.
    For each potential GCD 'g', we check if the GCD of all its multiples present 
    in the array equals 'g'.

    Args:
        nums: A list of positive integers.

    Returns:
        The count of unique GCD values that can be formed.

    Examples:
        >>> solve([1, 2, 3])
        3
        >>> solve([10, 2, 5, 1])
        4
    """
    if not nums:
        return 0

    max_val = max(nums)
    # presence_map[i] is True if i exists in the input array
    presence_map = [False] * (max_val + 1)
    for num in nums:
        presence_map[num] = True

    distinct_gcd_count = 0

    # Iterate through every possible GCD value from 1 to max_val
    for g in range(1, max_val + 1):
        current_gcd = 0
        
        # Check multiples of g: g, 2g, 3g, ...
        # If we find multiples of g in the array, their collective GCD 
        # will be a multiple of g. If that collective GCD is exactly g,
        # then g is a valid subsequence GCD.
        for multiple in range(g, max_val + 1, g):
            if presence_map[multiple]:
                if current_gcd == 0:
                    current_gcd = multiple
                else:
                    # Compute GCD of the current running GCD and the new multiple
                    current_gcd = _math_gcd(current_gcd, multiple)
                
                # Optimization: if current_gcd reaches g, we found it
                if current_gcd == g:
                    distinct_gcd_count += 1
                    break
                    
    return distinct_gcd_count

def _math_gcd(a: int, b: int) -> int:
    """Helper function to compute the greatest common divisor."""
    while b:
        a, b = b, a % b
    return a
