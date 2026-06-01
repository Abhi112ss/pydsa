METADATA = {
    "id": 2318,
    "name": "Number of Distinct Roll Sequences",
    "slug": "number-of-distinct-roll-sequences",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the number of distinct sequences of n rolls of a 6-sided die such that no two adjacent rolls are the same, given a set of forbidden pairs.",
}

def solve(n: int, forbidden: list[list[int]]) -> int:
    """
    Calculates the number of distinct sequences of n rolls of a 6-sided die
    where no two adjacent rolls are the same and no forbidden pairs occur.

    Args:
        n: The number of rolls in the sequence.
        forbidden: A list of pairs [a, b] representing forbidden adjacent rolls.

    Returns:
        The total number of valid sequences modulo 10^9 + 7.

    Examples:
        >>> solve(2, [[1, 2]])
        35
        >>> solve(3, [[1, 2], [2, 1]])
        114
    """
    MOD = 1_000_000_007

    # Create an adjacency matrix to quickly check if a pair (i, j) is allowed.
    # We use 1-based indexing for convenience, so size is 7x7.
    is_allowed = [[True for _ in range(7)] for _ in range(7)]
    
    # Rule 1: No two adjacent rolls can be the same.
    for i in range(1, 7):
        is_allowed[i][i] = False
        
    # Rule 2: Apply the forbidden pairs provided in the input.
    for u, v in forbidden:
        is_allowed[u][v] = False

    # dp[i][j] represents the number of valid sequences of length i ending with die value j.
    # To optimize space from O(n * 6) to O(6), we only keep the current and previous state.
    # However, for clarity and given n is up to 10^5, O(n) space is acceptable.
    # We'll use a 1D array representing the counts for the current roll length.
    
    # Base case: For n = 1, there is exactly 1 way to end with each die value.
    current_counts = [0] * 7
    for i in range(1, 7):
        current_counts[i] = 1

    # Iteratively build the sequences up to length n.
    for _ in range(2, n + 1):
        next_counts = [0] * 7
        # Pre-calculate the sum of all counts from the previous step to optimize.
        # Total ways to form a sequence of length i-1.
        total_prev_sum = sum(current_counts) % MOD
        
        for current_die in range(1, 7):
            # The number of ways to end with 'current_die' is the sum of all ways 
            # to end with 'prev_die' such that (prev_die, current_die) is allowed.
            # Instead of iterating through all prev_die, we can subtract forbidden ones.
            # But since the number of dice is constant (6), a simple loop is O(1).
            ways = 0
            for prev_die in range(1, 7):
                if is_allowed[prev_die][current_die]:
                    ways = (ways + current_counts[prev_die]) % MOD
            next_counts[current_die] = ways
            
        current_counts = next_counts

    # The answer is the sum of all valid sequences of length n ending in any die value.
    return sum(current_counts) % MOD
