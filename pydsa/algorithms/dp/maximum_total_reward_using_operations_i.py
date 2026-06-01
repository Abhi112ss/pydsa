METADATA = {
    "id": 3180,
    "name": "Maximum Total Reward Using Operations I",
    "slug": "maximum-total-reward-using-operations-i",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "bit_manipulation", "knapsack"],
    "difficulty": "medium",
    "time_complexity": "O(max_val^2)",
    "space_complexity": "O(max_val)",
    "description": "Find the maximum total reward by picking operations such that the reward is always greater than the current total.",
}

def solve(reward: list[int]) -> int:
    """
    Calculates the maximum total reward possible by selecting operations.
    
    An operation with value 'x' can be picked if the current total reward 'current_reward'
    is less than 'x'. The new reward becomes 'current_reward + x'.

    Args:
        reward: A list of integers representing the value of each operation.

    Returns:
        The maximum possible total reward.

    Examples:
        >>> solve([4, 5, 2, 1])
        12
        >>> solve([1, 1, 1])
        1
        >>> solve([10, 10, 10])
        10
    """
    # Sort rewards to process them in increasing order.
    # This ensures that when we consider a reward, we are building upon 
    # smaller totals, which is a requirement for the knapsack-style DP.
    reward.sort()
    
    # The maximum possible reward is bounded by the sum of all elements,
    # but specifically, the condition 'current_reward < x' implies that
    # the maximum reward we can ever reach is roughly 2 * max(reward).
    # Since max(reward) is 50,000, we use a bitset-like approach or a boolean DP.
    # However, for the 'I' version, the constraints allow for a simpler DP.
    max_val = reward[-1]
    
    # dp[i] will be True if a total reward of 'i' is achievable.
    # We use a bitset approach via a large integer for efficiency in Python.
    # bitset represents the set of all reachable rewards.
    reachable_rewards = 1  # Initially, reward 0 is reachable (bit 0 is set)

    for x in reward:
        # We can only pick 'x' if the current reward 'r' is less than 'x'.
        # This means we only care about bits in the bitset that are less than 'x'.
        # We create a mask to isolate bits from 0 to x-1.
        mask = (1 << x) - 1
        valid_current_rewards = reachable_rewards & mask
        
        # For every valid current reward 'r', the new reward is 'r + x'.
        # This is equivalent to shifting the valid bits left by 'x' positions.
        new_rewards = valid_current_rewards << x
        
        # Update the set of reachable rewards.
        reachable_rewards |= new_rewards

    # The answer is the highest bit set in the reachable_rewards integer.
    return reachable_rewards.bit_length() - 1
