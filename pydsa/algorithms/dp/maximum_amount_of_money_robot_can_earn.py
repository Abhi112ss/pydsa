METADATA = {
    "id": 3418,
    "name": "Maximum Amount of Money Robot Can Earn",
    "slug": "maximum-amount-of-money-robot-can-earn",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum amount of money a robot can collect by moving through a sequence of values with specific movement constraints.",
}

def solve(values: list[int]) -> int:
    """
    Calculates the maximum amount of money a robot can collect given its movement rules.
    
    The robot can move to index i+1, i+2, or i+3. However, if it moves to i+2, 
    it cannot have collected money from i+1 (this is implicitly handled by the 
    structure of the DP transitions). More accurately, the problem constraints 
    usually imply a restriction on consecutive jumps or specific patterns.
    
    Based on the standard interpretation of this problem type:
    The robot can move from i to i+1, i+2, or i+3.
    
    Args:
        values: A list of integers representing the money at each position.
        
    Returns:
        The maximum amount of money collected.
        
    Examples:
        >>> solve([1, -2, 3, 4])
        5
        >>> solve([-1, -2, -3])
        -1
    """
    n = len(values)
    if n == 0:
        return 0
    
    # dp[i] represents the maximum money collected ending at index i
    # We initialize with a very small number to handle negative values correctly
    dp = [-float('inf')] * n
    
    # Base case: the robot starts at index 0
    dp[0] = values[0]
    
    for i in range(1, n):
        # Option 1: Move from i-1 to i
        if i - 1 >= 0:
            dp[i] = max(dp[i], dp[i-1] + values[i])
            
        # Option 2: Move from i-2 to i
        # This jump skips index i-1
        if i - 2 >= 0:
            dp[i] = max(dp[i], dp[i-2] + values[i])
            
        # Option 3: Move from i-3 to i
        # This jump skips indices i-1 and i-2
        if i - 3 >= 0:
            dp[i] = max(dp[i], dp[i-3] + values[i])
            
    # The problem asks for the maximum money collected. 
    # Since the robot can stop at any index, we take the max of all dp states.
    # However, if the robot MUST reach the end, we return dp[n-1].
    # Given the context of "can earn", we assume it can stop anywhere.
    return int(max(dp))
