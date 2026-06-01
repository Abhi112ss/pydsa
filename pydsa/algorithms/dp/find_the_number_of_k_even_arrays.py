METADATA = {
    "id": 3339,
    "name": "Find the Number of K-Even Arrays",
    "slug": "find-the-number-of-k-even-arrays",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "combinatorics", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n * k)",
    "space_complexity": "O(n * k)",
    "description": "Count the number of ways to construct an array of length n such that exactly k elements are even, given constraints on the range of values.",
}

def solve(n: int, k: int, min_val: int, max_val: int, mod: int) -> int:
    """
    Calculates the number of arrays of length n where exactly k elements are even.

    Args:
        n: The length of the array.
        k: The required number of even elements.
        min_val: The minimum possible value for an element in the array.
        max_val: The maximum possible value for an element in the array.
        mod: The modulo value for the result.

    Returns:
        The number of valid arrays modulo mod.

    Examples:
        >>> solve(2, 1, 1, 2, 10**9 + 7)
        2
    """
    # Calculate the count of even and odd numbers in the range [min_val, max_val]
    # Total numbers in range: max_val - min_val + 1
    total_elements = max_val - min_val + 1
    
    # To find even count: count of evens up to max_val minus count of evens up to min_val - 1
    def count_evens_up_to(x: int) -> int:
        if x < 0:
            return 0
        return x // 2 + 1 if x >= 0 else 0

    # A more robust way to count evens in [L, R]:
    # Number of evens in [0, x] is floor(x/2) + 1
    # But we need to handle the range carefully.
    # Let's use the property: count of evens in [1, x] is x // 2
    # Let's use a simpler approach:
    evens_in_range = 0
    if min_val % 2 == 0:
        # If min is even, evens are min, min+2, ...
        # If max is even, last even is max. If max is odd, last even is max-1.
        last_even = max_val if max_val % 2 == 0 else max_val - 1
        if last_even >= min_val:
            evens_in_range = (last_even - min_val) // 2 + 1
    else:
        # If min is odd, first even is min+1
        first_even = min_val + 1
        last_even = max_val if max_val % 2 == 0 else max_val - 1
        if last_even >= first_even:
            evens_in_range = (last_even - first_even) // 2 + 1
            
    odds_in_range = total_elements - evens_in_range

    # dp[i][j] = number of ways to have j even elements in an array of length i
    # We use a 2D DP table.
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(k + 1):
            # Case 1: The i-th element is even. 
            # This contributes to the j-th even count if we had j-1 evens before.
            if j > 0:
                dp[i][j] = (dp[i][j] + dp[i-1][j-1] * evens_in_range) % mod
            
            # Case 2: The i-th element is odd.
            # This contributes to the j-th even count if we already had j evens before.
            # Note: We must ensure we don't exceed the total length n-j for odds, 
            # but the DP state naturally handles the count of evens.
            # However, we must account for the fact that we can only pick an odd number 
            # if we aren't forced to pick an even one to reach k.
            # Actually, the standard DP for "exactly k" is:
            # dp[i][j] = (ways to have j-1 evens) * (count of evens) + (ways to have j evens) * (count of odds)
            dp[i][j] = (dp[i][j] + dp[i-1][j] * odds_in_range) % mod

    # The problem asks for exactly k even elements in an array of length n.
    # However, the standard DP above calculates ways to have j evens in length i.
    # But there's a catch: if we need exactly k evens, the remaining (n-k) MUST be odd.
    # The DP above actually calculates:
    # dp[n][k] = ways to have exactly k even numbers and (n-k) odd numbers.
    
    return dp[n][k]

# Note: The problem description in the prompt implies a specific DP structure.
# The logic above follows: dp[i][j] = dp[i-1][j-1] * evens + dp[i-1][j] * odds
# This is the standard way to count combinations with replacement/selection.
