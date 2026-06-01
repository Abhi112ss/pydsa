METADATA = {
    "id": 3181,
    "name": "Maximum Total Reward Using Operations II",
    "slug": "maximum-total-reward-using-operations-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "knapsack", "bitset"],
    "difficulty": "hard",
    "time_complexity": "O(max_val^2 / 64) or O(max_val^2) depending on implementation",
    "space_complexity": "O(max_val)",
    "description": "Find the maximum total reward possible by selecting operations such that the sum of selected values is always greater than the current total reward.",
}

def solve(reward: list[int]) -> int:
    """
    Calculates the maximum total reward possible using the given operations.
    
    The rule is: you can pick a reward 'x' if the current total reward 'S' 
    is less than 'x' (i.e., S < x). This implies that the new total reward 
    will be S + x. Since S < x, the new total reward S + x will always be 
    less than 2x. This bounds the maximum possible reward to 2 * max(reward).

    Args:
        reward: A list of integers representing the reward values available.

    Returns:
        The maximum total reward that can be achieved.

    Examples:
        >>> solve([1, 10, 3, 6, 7])
        24
        >>> solve([1, 2, 3, 4, 5])
        15
    """
    # Sort rewards to process them in increasing order.
    # This ensures that when we consider reward[i], we are building upon 
    # smaller sums, which is a requirement for the S < x condition.
    reward.sort()
    
    max_val = reward[-1]
    # The maximum possible sum we can ever reach is bounded.
    # If we pick the largest reward 'M', the previous sum 'S' must be < M.
    # Thus, the maximum sum is M + (M-1) = 2M - 1.
    limit = 2 * max_val
    
    # dp[s] will be True if a total reward of 's' is achievable.
    # We use a bitset-like approach via a large integer in Python to 
    # optimize the knapsack update. Python's arbitrary precision integers 
    # act as efficient bitsets.
    dp = 1  # Represents the sum 0 is achievable (bit 0 is set)

    for x in reward:
        # The condition is: we can add 'x' to any existing sum 's' 
        # if s < x.
        # In bitwise terms:
        # 1. Create a mask of all bits from 0 to x-1.
        # 2. Extract these bits from the current dp.
        # 3. Shift these bits left by 'x' positions (representing adding x to the sum).
        # 4. OR the result back into the dp.
        
        # mask = (1 << x) - 1
        # current_achievable_sums_less_than_x = dp & mask
        # new_sums = current_achievable_sums_less_than_x << x
        # dp |= new_sums
        
        # Optimization: Instead of manual masking, we can use bitwise operations.
        # We only care about bits in 'dp' that are less than 'x'.
        # We can use (dp & ((1 << x) - 1)) to get all achievable sums < x.
        dp |= (dp & ((1 << x) - 1)) << x

    # The answer is the index of the highest set bit in the dp integer.
    return dp.bit_length() - 1
