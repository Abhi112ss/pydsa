METADATA = {
    "id": 3699,
    "name": "Number of ZigZag Arrays I",
    "slug": "number_of_zigzag_arrays_i",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "combinatorics", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Count the number of zigzag arrays of length n where elements are within a specific range.",
}

def solve(n: int, max_val: int) -> int:
    """
    Calculates the number of zigzag arrays of length n with elements in [1, max_val].
    A zigzag array is defined such that elements alternate between increasing and decreasing.
    
    Args:
        n: The length of the array.
        max_val: The maximum possible value for any element in the array.
        
    Returns:
        The total number of valid zigzag arrays modulo 10^9 + 7.
        
    Examples:
        >>> solve(2, 3)
        6
        # Valid: [1,2], [1,3], [2,1], [2,3], [3,1], [3,2]
        >>> solve(3, 2)
        2
        # Valid: [1,2,1], [2,1,2]
    """
    MOD = 10**9 + 7

    if n == 0:
        return 0
    if n == 1:
        return max_val % MOD

    # dp_inc[v] = number of zigzag arrays ending at value v where the last step was increasing
    # dp_dec[v] = number of zigzag arrays ending at value v where the last step was decreasing
    # We use space optimization to keep only the current and previous state.
    
    # Base case: n = 2
    # For n=2, an array [a, b] is "increasing" if a < b and "decreasing" if a > b.
    # Note: The problem definition for zigzag usually implies the direction flips.
    # For n=2, any pair (a, b) with a != b is a valid start of a zigzag.
    
    dp_inc = [0] * (max_val + 1)
    dp_dec = [0] * (max_val + 1)

    # Initialize for n = 2
    # dp_inc[v] means array ends with ... < v
    # dp_dec[v] means array ends with ... > v
    for v in range(1, max_val + 1):
        # To end with v as an increasing step, previous element must be < v
        dp_inc[v] = (v - 1) % MOD
        # To end with v as a decreasing step, previous element must be > v
        dp_dec[v] = (max_val - v) % MOD

    # Iterate from length 3 to n
    for length in range(3, n + 1):
        new_dp_inc = [0] * (max_val + 1)
        new_dp_dec = [0] * (max_val + 1)
        
        # To calculate new_dp_inc[v], we need sum(dp_dec[prev]) where prev < v
        # To calculate new_dp_dec[v], we need sum(dp_inc[prev]) where prev > v
        
        # Prefix sums for dp_dec to optimize the sum(dp_dec[prev] for prev < v)
        prefix_sum_dec = [0] * (max_val + 2)
        for v in range(1, max_val + 1):
            prefix_sum_dec[v] = (prefix_sum_dec[v-1] + dp_dec[v]) % MOD
            
        # Suffix sums for dp_inc to optimize the sum(dp_inc[prev] for prev > v)
        suffix_sum_inc = [0] * (max_val + 2)
        for v in range(max_val, 0, -1):
            suffix_sum_inc[v] = (suffix_sum_inc[v+1] + dp_inc[v]) % MOD

        for v in range(1, max_val + 1):
            # Current step is increasing: previous step must have been decreasing
            # and previous value < current value
            new_dp_inc[v] = prefix_sum_dec[v-1]
            
            # Current step is decreasing: previous step must have been increasing
            # and previous value > current value
            new_dp_dec[v] = suffix_sum_inc[v+1]
            
        dp_inc = new_dp_inc
        dp_dec = new_dp_dec

    # The total count is the sum of all valid zigzag arrays ending at any v
    total_count = (sum(dp_inc) + sum(dp_dec)) % MOD
    return total_count
