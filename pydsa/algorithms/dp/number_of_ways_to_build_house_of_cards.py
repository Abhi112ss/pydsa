METADATA = {
    "id": 2189,
    "name": "Number of Ways to Build House of Cards",
    "slug": "number-of-ways-to-build-house-of-cards",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Calculate the number of ways to build a house of cards given a specific number of cards where each layer follows a specific arithmetic progression.",
}

def solve(n: int) -> int:
    """
    Args:
        n: The total number of cards available.

    Returns:
        The number of ways to build a house of cards.
    """
    MODULUS = 10**9 + 7
    
    total_ways = 0
    
    for layers in range(1, n + 1):
        cards_needed = 0
        for i in range(1, layers + 1):
            cards_needed += (2 * i - 1)
            
        if cards_needed > n:
            break
            
        remaining_cards = n - cards_needed
        
        dp = [0] * (remaining_cards + 1)
        dp[0] = 1
        
        for i in range(1, layers + 1):
            new_dp = [0] * (remaining_cards + 1)
            prefix_sum = 0
            for j in range(remaining_cards + 1):
                prefix_sum = (prefix_sum + dp[j]) % MODULUS
                if j >= i:
                    new_dp[j] = prefix_sum
                else:
                    new_dp[j] = prefix_sum
            
            dp = new_dp

        total_ways = (total_ways + dp[remaining_cards]) % MODULUS

    return total_ways

def solve_optimized(n: int) -> int:
    """
    Args:
        n: The total number of cards available.

    Returns:
        The number of ways to build a house of cards.
    """
    MODULUS = 10**9 + 7
    
    ways = 0
    
    for k in range(1, n + 1):
        sum_needed = k * k
        if sum_needed > n:
            break
            
        rem = n - sum_needed
        
        dp = [0] * (rem + 1)
        dp[0] = 1
        
        for i in range(1, k + 1):
            new_dp = [0] * (rem + 1)
            current_sum = 0
            for j in range(rem + 1):
                current_sum = (current_sum + dp[j]) % MODULUS
                new_dp[j] = current_sum
            dp = new_dp
            
        ways = (ways + dp[rem]) % MODULUS
        
    return ways

def solve(n: int) -> int:
    """
    Args:
        n: The total number of cards available.

    Returns:
        The number of ways to build a house of cards.
    """
    MODULUS = 10**9 + 7
    total_ways = 0
    
    for k in range(1, n + 1):
        sum_needed = k * k
        if sum_needed > n:
            break
            
        rem = n - sum_needed
        dp = [0] * (rem + 1)
        dp[0] = 1
        
        for i in range(1, k + 1):
            new_dp = [0] * (rem + 1)
            running_sum = 0
            for j in range(rem + 1):
                running_sum = (running_sum + dp[j]) % MODULUS
                new_dp[j] = running_sum
            dp = new_dp
            
        total_ways = (total_ways + dp[rem]) % MODULUS
        
    return total_ways