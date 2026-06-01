METADATA = {
    "id": 1259,
    "name": "Handshakes That Don't Cross",
    "slug": "handshakes-that-dont-cross",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the number of ways n pairs of people sitting around a circle can shake hands without any handshakes crossing.",
}

def solve(n: int) -> int:
    """
    Calculates the number of ways n pairs of people can shake hands without crossing.
    
    The problem is a classic application of Catalan numbers. For n pairs (2n people),
    if one person shakes hands with another, they divide the circle into two 
    separate groups. For the handshakes not to cross, both groups must contain 
    an even number of people.

    Args:
        n: The number of pairs of people.

    Returns:
        The total number of non-crossing handshake configurations.

    Examples:
        >>> solve(1)
        1
        >>> solve(2)
        2
        >>> solve(3)
        5
    """
    if n == 0:
        return 1
    
    # dp[i] stores the number of ways i pairs of people can shake hands.
    # This is equivalent to the i-th Catalan number.
    dp = [0] * (n + 1)
    dp[0] = 1
    
    # Fill the DP table using the recurrence relation:
    # C(n) = sum(C(i) * C(n-1-i)) for i from 0 to n-1
    for i in range(1, n + 1):
        for j in range(i):
            # Person 1 shakes hands with person 2j + 2.
            # This leaves 2j people on one side and 2(i - 1 - j) people on the other.
            # We use j and (i - 1 - j) as the number of pairs in each partition.
            dp[i] += dp[j] * dp[i - 1 - j]
            
    return dp[n]
