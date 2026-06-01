METADATA = {
    "id": 3213,
    "name": "Construct String with Minimum Cost",
    "slug": "construct-string-with-minimum-cost",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["greedy", "dynamic_programming", "string"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Construct a target string using available patterns with minimum total cost.",
}

def solve(target: str, patterns: list[str], costs: list[int]) -> int:
    """
    Finds the minimum cost to construct the target string using a set of patterns.

    Args:
        target: The target string to be constructed.
        patterns: A list of available pattern strings.
        costs: A list of costs associated with each pattern.

    Returns:
        The minimum cost to construct the target string. Returns -1 if impossible.

    Examples:
        >>> solve("abc", ["a", "b", "c"], [1, 1, 1])
        3
        >>> solve("abc", ["ab", "c"], [10, 5])
        15
        >>> solve("abc", ["a", "bc"], [1, 10])
        11
    """
    n = len(target)
    # dp[i] represents the minimum cost to construct the prefix target[0:i]
    # Initialize with infinity to represent unreachable states
    inf = float('inf')
    dp = [inf] * (n + 1)
    dp[0] = 0

    # Pre-process patterns into a dictionary for faster lookup if needed,
    # but since we iterate through patterns for each index, we can just loop.
    # To optimize, we can group patterns by their starting character.
    pattern_map: dict[str, list[tuple[str, int]]] = {}
    for pattern, cost in zip(patterns, costs):
        first_char = pattern[0]
        if first_char not in pattern_map:
            pattern_map[first_char] = []
        pattern_map[first_char].append((pattern, cost))

    for i in range(n):
        # If the current prefix cannot be formed, skip
        if dp[i] == inf:
            continue

        current_char = target[i]
        # Only attempt to apply patterns that start with the character at target[i]
        if current_char in pattern_map:
            for pattern, cost in pattern_map[current_char]:
                pattern_len = len(pattern)
                # Check if the pattern matches the substring starting at index i
                if i + pattern_len <= n and target[i : i + pattern_len] == pattern:
                    # Update the DP state for the end of this pattern
                    new_cost = dp[i] + cost
                    if new_cost < dp[i + pattern_len]:
                        dp[i + pattern_len] = new_cost

    result = dp[n]
    return int(result) if result != inf else -1
