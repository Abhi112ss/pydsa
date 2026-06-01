METADATA = {
    "id": 2787,
    "name": "Ways to Express an Integer as Sum of Powers",
    "slug": "ways-to-express-an-integer-as-sum-of-powers",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math", "subset sum"],
    "difficulty": "medium",
    "time_complexity": "O(n * m^(1/x))",
    "space_complexity": "O(n)",
    "description": "Find the number of ways to express an integer n as the sum of unique x-th powers of positive integers.",
}

def solve(n: int, x: int) -> int:
    """
    Calculates the number of ways to express n as a sum of unique x-th powers.

    This problem is a variation of the 0/1 Knapsack problem (specifically the 
    subset sum problem), where the 'items' are the x-th powers of integers 
    starting from 1 up to the point where the power exceeds n.

    Args:
        n: The target integer to express as a sum.
        x: The power to which each integer is raised.

    Returns:
        The number of ways to express n as a sum of unique x-th powers, 
        modulo 10^9 + 7.

    Examples:
        >>> solve(10, 2)
        1
        # 1^2 + 3^2 = 1 + 9 = 10
        >>> solve(4, 1)
        1
        # 4 = 4 (only one way using unique integers)
    """
    MODULO = 1_000_000_007
    
    # dp[i] will store the number of ways to get sum i
    # We use a 1D array to optimize space from O(n * num_elements) to O(n)
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: there is one way to make the sum 0 (using no elements)

    # Iterate through each integer starting from 1
    current_val = 1
    while True:
        # Calculate the x-th power of the current integer
        power_val = current_val ** x
        
        # If the power exceeds n, no further integers can contribute to the sum
        if power_val > n:
            break
            
        # Update the DP table in reverse to ensure each power is used at most once
        # (Standard 0/1 Knapsack space optimization)
        for target_sum in range(n, power_val - 1, -1):
            dp[target_sum] = (dp[target_sum] + dp[target_sum - power_val]) % MODULO
            
        current_val += 1

    return dp[n]
