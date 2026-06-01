METADATA = {
    "id": 818,
    "name": "Race Car",
    "slug": "race-car",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "bfs", "math"],
    "difficulty": "hard",
    "time_complexity": "O(target * log(target))",
    "space_complexity": "O(target)",
    "description": "Find the minimum number of instructions to reach a target position starting from position 1 with specific acceleration and velocity rules.",
}

def solve(target: int) -> int:
    """
    Calculates the minimum number of instructions to reach the target position.

    The car starts at position 1 with velocity 1. 
    Instructions:
    - 'A' (Accelerate): position += velocity, velocity *= 2
    - 'R' (Reverse): velocity = -1 if velocity > 0 else 1

    Args:
        target: The target position to reach.

    Returns:
        The minimum number of instructions required.

    Examples:
        >>> solve(3)
        2
        >>> solve(2)
        3
    """
    # dp[i] stores the minimum instructions to reach position i
    # We use a dictionary or a list. Since target can be large, 
    # but we only care about positions up to target, a list is efficient.
    dp = [0] * (target + 1)

    for i in range(1, target + 1):
        # Find the number of 'A' steps to reach or pass the target i
        # Let n be the number of accelerations.
        # Position after n steps: 2^n - 1
        n = i.bit_length()
        
        # Case 1: We land exactly on i after n accelerations
        if (1 << n) - 1 == i:
            dp[i] = n
            continue

        # Case 2: We overshoot i (n steps) and then reverse and move back
        # We take n steps to reach (2^n - 1), then reverse, then solve for the remaining distance.
        # The remaining distance is (2^n - 1) - i.
        dp[i] = n + 1 + dp[(1 << n) - 1 - i]

        # Case 3: We undershoot i (n-1 steps) and then reverse and move forward
        # We take n-1 steps to reach (2^(n-1) - 1), then reverse, then solve for the remaining distance.
        # The remaining distance is i - (2^(n-1) - 1).
        # We add 1 for the reverse instruction.
        dp[i] = min(dp[i], (n - 1) + 1 + dp[i - (1 << (n - 1)) + 1])

    return dp[target]
