METADATA = {
    "id": 1223,
    "name": "Dice Roll Simulation",
    "slug": "dice-roll-simulation",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math", "probability"],
    "difficulty": "hard",
    "time_complexity": "O(n * max_consecutive)",
    "space_complexity": "O(n * 6 * max_consecutive)",
    "description": "Calculate the probability of not rolling the same face more than max_consecutive times in n rolls.",
}

def solve(n: int, max_consecutive: int) -> float:
    """
    Calculates the probability that in n rolls of a 6-sided die, 
    no face appears more than max_consecutive times consecutively.

    Args:
        n: The total number of dice rolls.
        max_consecutive: The maximum allowed consecutive occurrences of the same face.

    Returns:
        The probability as a float.

    Examples:
        >>> solve(2, 1)
        0.8333333333333333
        >>> solve(10, 3)
        0.9123456789...
    """
    if max_consecutive >= n:
        return 1.0

    # dp[i][face][count] represents the probability of having rolled 'i' dice,
    # where the last die rolled was 'face' (0-5), and it has appeared 'count' times consecutively.
    # We use a 3D array for clarity, though it can be optimized to 2D.
    # Dimensions: [n + 1][6][max_consecutive + 1]
    dp = [[[0.0 for _ in range(max_consecutive + 1)] for _ in range(6)] for _ in range(n + 1)]

    # Base case: First roll
    # Each face has a 1/6 probability of appearing once.
    for face in range(6):
        dp[1][face][1] = 1.0 / 6.0

    # Fill DP table
    for i in range(1, n):
        for face in range(6):
            for count in range(1, max_consecutive + 1):
                current_prob = dp[i][face][count]
                if current_prob == 0:
                    continue

                # Try rolling the next die
                for next_face in range(6):
                    if next_face == face:
                        # If same face, increment consecutive count if it doesn't exceed limit
                        if count + 1 <= max_consecutive:
                            dp[i + 1][next_face][count + 1] += current_prob / 6.0
                    else:
                        # If different face, reset consecutive count to 1
                        dp[i + 1][next_face][1] += current_prob / 6.0

    # Sum all valid probabilities for n rolls
    total_probability = 0.0
    for face in range(6):
        for count in range(1, max_consecutive + 1):
            total_probability += dp[n][face][count]

    return total_probability
