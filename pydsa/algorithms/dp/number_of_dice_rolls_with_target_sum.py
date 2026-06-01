METADATA = {
    "id": 1155,
    "name": "Number of Dice Rolls With Target Sum",
    "slug": "number-of-dice-rolls-with-target-sum",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n * target * k)",
    "space_complexity": "O(target)",
    "description": "Calculate the number of ways to roll n dice with k faces each to reach a specific target sum.",
}

def solve(n: int, k: int, target: int) -> int:
    """
    Calculates the number of ways to roll n dice, each with k faces, to get a target sum.
    
    The solution uses dynamic programming with space optimization. Instead of a 2D table,
    we use a 1D array representing the number of ways to reach each sum with the current 
    number of dice processed.

    Args:
        n: The number of dice.
        k: The number of faces on each die (faces are 1 to k).
        target: The target sum to achieve.

    Returns:
        The number of ways to reach the target sum modulo 10^9 + 7.

    Examples:
        >>> solve(2, 6, 7)
        6
        >>> solve(3, 2, 5)
        1
    """
    MOD = 1_000_000_007

    # Base case: If target is impossible given the number of dice and faces
    if target < n or target > n * k:
        return 0

    # dp[s] stores the number of ways to get sum 's' with the current number of dice
    dp = [0] * (target + 1)
    
    # Base case for 0 dice: there is 1 way to get sum 0
    dp[0] = 1

    # Iterate through each die
    for die_idx in range(1, n + 1):
        # new_dp will store the ways for the current number of dice
        new_dp = [0] * (target + 1)
        
        # For each possible sum achieved by previous dice
        for current_sum in range(target + 1):
            if dp[current_sum] == 0:
                continue
            
            # Try every face value from 1 to k
            for face_value in range(1, k + 1):
                next_sum = current_sum + face_value
                if next_sum <= target:
                    new_dp[next_sum] = (new_dp[next_sum] + dp[current_sum]) % MOD
                else:
                    # Since face_value increases, if next_sum > target, it will stay > target
                    break
        
        # Move to the next die
        dp = new_dp

    return dp[target]
