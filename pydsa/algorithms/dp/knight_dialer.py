METADATA = {
    "id": 935,
    "name": "Knight Dialer",
    "slug": "knight-dialer",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the number of distinct phone numbers of length n that can be dialed using a knight's moves on a phone keypad.",
}

def solve(n: int) -> int:
    """
    Calculates the number of distinct phone numbers of length n that can be 
    dialed using a knight's moves on a standard phone keypad.

    Args:
        n: The length of the phone number to be dialed.

    Returns:
        The total number of valid phone numbers modulo 10^9 + 7.

    Examples:
        >>> solve(1)
        10
        >>> solve(2)
        20
    """
    if n <= 0:
        return 0
    if n == 1:
        return 10

    MOD = 1_000_000_007

    # Adjacency list representing valid knight moves on a phone keypad
    # 0: [4, 6]
    # 1: [6, 8]
    # 2: [7, 9]
    # 3: [4, 8]
    # 4: [0, 3, 9]
    # 5: []
    # 6: [0, 1, 7]
    # 7: [2, 6]
    # 8: [1, 3]
    # 9: [2, 4]
    adj = [
        [4, 6],    # 0
        [6, 8],    # 1
        [7, 9],    # 2
        [4, 8],    # 3
        [0, 3, 9], # 4
        [],        # 5
        [0, 1, 7], # 6
        [2, 6],    # 7
        [1, 3],    # 8
        [2, 4]     # 9
    ]

    # dp[i] stores the number of ways to end at digit i for the current length
    # Initialize for n=1: each digit can be a starting point (1 way each)
    dp = [1] * 10

    # Iterate from length 2 up to n
    for _ in range(2, n + 1):
        new_dp = [0] * 10
        # For each digit, calculate how many ways we could have arrived there
        # from its valid knight-move neighbors
        for current_digit in range(10):
            # Instead of looking at neighbors of current_digit, we distribute 
            # the current ways to the neighbors to build the next state.
            # However, to keep it simple, we iterate through all digits and 
            # sum up the ways from their predecessors.
            pass 
        
        # Correct DP transition: new_dp[target] = sum(dp[source] for source in neighbors_of_target)
        # To optimize, we iterate through each digit and add its current count to its neighbors.
        for source_digit in range(10):
            if dp[source_digit] == 0:
                continue
            for target_digit in adj[source_digit]:
                new_dp[target_digit] = (new_dp[target_digit] + dp[source_digit]) % MOD
        
        dp = new_dp

    # The answer is the sum of all ways to end at any digit after n steps
    return sum(dp) % MOD
