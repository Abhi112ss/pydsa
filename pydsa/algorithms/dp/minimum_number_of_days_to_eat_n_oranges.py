METADATA = {
    "id": 1553,
    "name": "Minimum Number of Days to Eat N Oranges",
    "slug": "minimum-number-of-days-to-eat-n-oranges",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "recursion", "math"],
    "difficulty": "hard",
    "time_complexity": "O(log n)",
    "space_complexity": "O(log n)",
    "description": "Find the minimum number of days to eat all oranges given three specific eating rules.",
}

def solve(n: int) -> int:
    """
    Calculates the minimum number of days to eat all n oranges.

    The rules are:
    1. Eat 1 orange.
    2. Eat half the oranges (if even).
    3. Eat 2 oranges for every 1 orange eaten in the previous step (if n % 3 == 0).

    Args:
        n: The total number of oranges.

    Returns:
        The minimum number of days required to eat all oranges.

    Examples:
        >>> solve(2)
        1
        >>> solve(5)
        4
        >>> solve(10)
        4
    """
    memo: dict[int, int] = {0: 0, 1: 1, 2: 1, 3: 3}

    def get_min_days(remaining: int) -> int:
        if remaining in memo:
            return memo[remaining]

        # Option 1: Eat 1 orange at a time until we reach a number divisible by 2 or 3.
        # We calculate the cost to reach the nearest multiple of 2 or 3 to avoid 
        # linear recursion (O(n)), making it logarithmic.
        
        # Case A: Reach a multiple of 2
        # We can reach the nearest even number by eating 1 orange (if odd) or 0 (if even).
        # However, to optimize, we look at the cost to reach the nearest multiple of 2 or 3.
        
        # To reach a multiple of 2:
        res_even = (remaining % 2) + 1 + get_min_days(remaining // 2)
        
        # To reach a multiple of 3:
        # We eat (remaining % 3) oranges to reach a multiple of 3, 
        # then we use the "eat 2 for 1" rule which effectively reduces n to n/3.
        res_triple = (remaining % 3) + 1 + get_min_days(remaining // 3)

        # We take the minimum of the two paths
        memo[remaining] = min(res_even, res_triple)
        return memo[remaining]

    # The logic above needs a slight adjustment for the "eat 1" vs "eat 2 for 1" 
    # to ensure we don't just do 1+1+1... 
    # The optimal strategy is always to jump to the nearest multiple of 2 or 3.
    
    memo_optimized: dict[int, int] = {0: 0, 1: 1, 2: 1, 3: 3}

    def dp(num: int) -> int:
        if num in memo_optimized:
            return memo_optimized[num]
        
        # Option 1: Eat 1s until even, then divide by 2
        # Cost = (num % 2) + 1 (the division step)
        res_2 = (num % 2) + 1 + dp(num // 2)
        
        # Option 2: Eat 1s until divisible by 3, then divide by 3
        # Cost = (num % 3) + 1 (the division step)
        res_3 = (num % 3) + 1 + dp(num // 3)
        
        memo_optimized[num] = min(res_2, res_3)
        return memo_optimized[num]

    return dp(n)
