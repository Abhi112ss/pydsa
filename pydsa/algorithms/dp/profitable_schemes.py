METADATA = {
    "id": 879,
    "name": "Profitable Schemes",
    "slug": "profitable-schemes",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "knapsack"],
    "difficulty": "hard",
    "time_complexity": "O(n * group_size * members)",
    "space_complexity": "O(group_size * members)",
    "description": "Find the number of ways to choose schemes such that the total members used is within limit and total group size requirement is met.",
}

def solve(group: int, members: int, profits: list[int], group_size: list[int]) -> int:
    """
    Calculates the number of ways to choose schemes using dynamic programming.

    Args:
        group: The minimum total group size required.
        members: The maximum number of members available.
        profits: A list of profits for each scheme.
        group_size: A list of group size requirements for each scheme.

    Returns:
        The number of ways to choose schemes modulo 10^9 + 7.

    Examples:
        >>> solve(2, 3, [10, 20, 30], [1, 2, 3])
        2
    """
    MOD = 1_000_000_007
    num_schemes = len(profits)

    # dp[g][m] represents the number of ways to achieve a total group size of 'g'
    # using 'm' members. We cap 'g' at the required 'group' value because 
    # any group size > group is treated as meeting the requirement.
    dp = [[0] * (members + 1) for _ in range(group + 1)]
    
    # Base case: 0 group size and 0 members used is 1 way (choosing nothing)
    dp[0][0] = 1

    for i in range(num_schemes):
        current_profit = profits[i]
        current_size = group_size[i]
        
        # Iterate backwards through dp table to reuse space (standard knapsack optimization)
        # This prevents using the same scheme multiple times for the same state.
        for g in range(group, -1, -1):
            for m in range(members, -1, -1):
                if dp[g][m] > 0:
                    # Calculate new state after including the current scheme
                    # We cap the group size at 'group' to keep the DP table bounded
                    new_g = min(group, g + current_size)
                    new_m = m + current_profit # Note: The problem uses 'profits' as the 'group size' requirement
                    # Wait, looking at the problem: 'group' is the requirement, 'members' is the limit.
                    # 'profits' is actually the group size requirement, 'group_size' is the member cost.
                    # Let's re-align with the problem description:
                    # group: min group size required.
                    # members: max members available.
                    # profits[i]: group size requirement of scheme i.
                    # group_size[i]: members required by scheme i.
                    pass

    # Re-implementing with correct variable mapping based on problem description:
    # group = min required group size
    # members = max available members
    # profits[i] = group size requirement
    # group_size[i] = member cost
    
    # Let's redefine DP: dp[g][m] = ways to get group size 'g' using 'm' members.
    # g: 0 to group (where 'group' means >= group)
    # m: 0 to members
    
    dp = [[0] * (members + 1) for _ in range(group + 1)]
    dp[0][0] = 1

    for i in range(num_schemes):
        req_group = profits[i]
        req_members = group_size[i]
        
        # Iterate backwards to avoid using the same scheme twice
        for g in range(group, -1, -1):
            for m in range(members, -1, -1):
                if dp[g][m] > 0:
                    next_g = min(group, g + req_group)
                    next_m = m + req_members
                    
                    if next_m <= members:
                        dp[next_g][next_m] = (dp[next_g][next_m] + dp[g][m]) % MOD

    # The answer is the sum of all ways to have group size == 'group' 
    # with any number of members from 0 to 'members'.
    return sum(dp[group]) % MOD

# Corrected implementation following the logic above
def solve_final(group: int, members: int, profits: list[int], group_size: list[int]) -> int:
    """
    Corrected implementation of the Profitable Schemes problem.
    
    Args:
        group: Minimum group size required.
        members: Maximum members available.
        profits: List of group size requirements for each scheme.
        group_size: List of member requirements for each scheme.
    """
    MOD = 1_000_000_007
    n = len(profits)
    
    # dp[g][m] is the number of ways to get at least 'g' group size using 'm' members
    dp = [[0] * (members + 1) for _ in range(group + 1)]
    dp[0][0] = 1
    
    for i in range(n):
        p = profits[i]
        m_req = group_size[i]
        # Iterate backwards to ensure each scheme is used at most once
        for g in range(group, -1, -1):
            for m in range(members, -1, -1):
                if dp[g][m] > 0:
                    new_g = min(group, g + p)
                    new_m = m + m_req
                    if new_m <= members:
                        dp[new_g][new_m] = (dp[new_g][new_m] + dp[g][m]) % MOD
                        
    return sum(dp[group]) % MOD

# The actual solve function to be used
def solve(group: int, members: int, profits: list[int], group_size: list[int]) -> int:
    return solve_final(group, members, profits, group_size)