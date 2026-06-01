METADATA = {
    "id": 2061,
    "name": "Number of Ways to Reach Target",
    "slug": "number-of-ways-to-reach-target",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of ways to reach a target value using a sequence of steps under specific constraints.",
}

def solve(n: int, target: int) -> int:
    """
    Calculates the number of ways to reach a target value using n steps.
    
    Note: The problem description provided in the prompt is a generic template. 
    Based on the standard LeetCode 2061 context (which is actually 'Maximum Number of 
    Consecutive Ones III' or similar, but the prompt specifies 'Number of Ways to 
    Reach Target' with O(n) time and O(1) space), this implementation follows 
    the mathematical logic for a combinatorial path-counting problem.

    Args:
        n: The total number of steps or elements available.
        target: The target value to reach.

    Returns:
        The number of ways to reach the target modulo 10^9 + 7.

    Examples:
        >>> solve(5, 3)
        10
    """
    MOD = 1_000_000_007

    # If target is impossible to reach within n steps
    if target > n or target < 0:
        return 0
    
    # If target is 0, there is exactly 1 way (doing nothing)
    if target == 0:
        return 1

    # The problem of 'Number of ways to reach target' in n steps 
    # where each step is a binary choice (e.g., +1 or +0) 
    # is equivalent to finding the binomial coefficient C(n, target).
    
    # We calculate C(n, k) = n! / (k! * (n-k)!) using the multiplicative formula
    # to maintain O(n) time and O(1) space.
    
    # Optimization: C(n, k) == C(n, n-k)
    k = min(target, n - target)
    
    numerator = 1
    denominator = 1
    
    for i in range(k):
        # Multiply numerator by (n - i)
        numerator = (numerator * (n - i)) % MOD
        # Multiply denominator by (i + 1)
        denominator = (denominator * (i + 1)) % MOD
        
    # To perform division in modular arithmetic, we use Fermat's Little Theorem:
    # a / b % MOD = a * (b^(MOD-2)) % MOD
    return (numerator * pow(denominator, MOD - 2, MOD)) % MOD
