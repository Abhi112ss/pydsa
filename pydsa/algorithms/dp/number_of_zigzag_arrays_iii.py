METADATA = {
    "id": 3916,
    "name": "Number of ZigZag Arrays III",
    "slug": "number_of_zigzag_arrays_iii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "combinatorics", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Count the number of zigzag arrays of length n with elements in range [1, k] modulo 10^9 + 7.",
}

def solve(n: int, k: int) -> int:
    """
    Calculates the number of zigzag arrays of length n with elements in [1, k].
    A zigzag array is defined such that elements alternate between increasing 
    and decreasing.

    Args:
        n: The length of the array.
        k: The maximum value of an element in the array.

    Returns:
        The total number of zigzag arrays modulo 10^9 + 7.

    Examples:
        >>> solve(3, 3)
        # Possible arrays: [1,3,2], [2,3,1], [2,1,3], [3,1,2], etc.
        # This is a simplified example; actual count depends on definition.
    """
    if n == 0:
        return 0
    if n == 1:
        return k % 1000000007

    MOD = 1000000007

    # dp_up[i][v] = number of zigzag arrays of length i ending with value v, 
    # where the last step was an increase (arr[i-2] < arr[i-1]).
    # dp_down[i][v] = number of zigzag arrays of length i ending with value v, 
    # where the last step was a decrease (arr[i-2] > arr[i-1]).
    
    # Using 1-based indexing for values 1 to k for clarity.
    # We only need the previous length's DP state to compute the current,
    # but for O(n^2) space as requested, we use full tables.
    dp_up = [[0] * (k + 1) for _ in range(n + 1)]
    dp_down = [[0] * (k + 1) for _ in range(n + 1)]

    # Base case: length 1. 
    # Since there's no "previous" element, we treat length 1 as a neutral state.
    # However, the zigzag property starts from length 2.
    # For length 2, we can go up or down.
    for v in range(1, k + 1):
        # We initialize length 1 as a base for length 2 transitions.
        # To simplify, we can think of length 1 as having both "up" and "down" 
        # potential for the next step.
        dp_up[1][v] = 1
        dp_down[1][v] = 1

    # For length 2, we explicitly define the first direction.
    # dp_up[2][v] means arr[0] < arr[1]=v. So arr[0] can be any value in [1, v-1].
    # dp_down[2][v] means arr[0] > arr[1]=v. So arr[0] can be any value in [v+1, k].
    
    # To optimize the O(n * k^2) to O(n * k), we use prefix sums.
    for i in range(2, n + 1):
        # Precompute prefix sums for the previous length's dp tables
        # sum_up[v] = sum(dp_up[i-1][1...v])
        # sum_down[v] = sum(dp_down[i-1][1...v])
        # Note: For length 2, dp_up[1] and dp_down[1] are both 1.
        # But for i > 2, dp_up[i][v] must come from dp_down[i-1][prev_v] where prev_v < v.
        # And dp_down[i][v] must come from dp_up[i-1][prev_v] where prev_v > v.
        
        # Special case for i=2: the "previous" state doesn't have a direction yet.
        # We use the neutral dp[1][v] = 1.
        if i == 2:
            current_sum_up = 0
            for v in range(1, k + 1):
                dp_up[2][v] = current_sum_up
                current_sum_up = (current_sum_up + 1) % MOD
            
            current_sum_down = 0
            for v in range(k, 0, -1):
                dp_down[2][v] = current_sum_down
                current_sum_down = (current_sum_down + 1) % MOD
        else:
            # Standard zigzag transition:
            # To end with an UP move at index i (value v), 
            # the previous move (at i-1) must have been a DOWN move.
            # dp_up[i][v] = sum(dp_down[i-1][prev_v]) for all prev_v < v.
            
            prefix_sum_down = 0
            for v in range(1, k + 1):
                dp_up[i][v] = prefix_sum_down
                prefix_sum_down = (prefix_sum_down + dp_down[i-1][v]) % MOD
            
            # To end with a DOWN move at index i (value v),
            # the previous move (at i-1) must have been an UP move.
            # dp_down[i][v] = sum(dp_up[i-1][prev_v]) for all prev_v > v.
            
            suffix_sum_up = 0
            for v in range(k, 0, -1):
                dp_down[i][v] = suffix_sum_up
                suffix_sum_up = (suffix_sum_up + dp_up[i-1][v]) % MOD

    # The total number of zigzag arrays is the sum of all valid ends at length n.
    # A zigzag array can end with either an up move or a down move.
    total_count = 0
    for v in range(1, k + 1):
        total_count = (total_count + dp_up[n][v] + dp_down[n][v]) % MOD

    return total_count
