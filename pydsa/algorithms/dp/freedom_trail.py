METADATA = {
    "id": 514,
    "name": "Freedom Trail",
    "slug": "freedom-trail",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "memoization", "string"],
    "difficulty": "hard",
    "time_complexity": "O(k * r^2)",
    "space_complexity": "O(k * r)",
    "description": "Find the minimum cost to type a key string using a circular ring of characters.",
}

def solve(key: str, ring: str) -> int:
    """
    Calculates the minimum cost to type the given key using a circular ring.

    The cost is calculated as the distance between characters in the ring,
    plus 1 for each character typed. The ring is circular, so distance
    can be measured clockwise or counter-clockwise.

    Args:
        key: The string of characters to be typed.
        ring: The circular ring of characters.

    Returns:
        The minimum cost to type the key. Returns -1 if the key cannot be typed.

    Examples:
        >>> solve("abc", "abccba")
        5
        >>> solve("abc", "abcde")
        5
        >>> solve("abc", "acb")
        -1
    """
    key_len = len(key)
    ring_len = len(ring)

    # Pre-calculate positions of each character in the ring to avoid O(R) lookups
    # A character might appear multiple times in the ring.
    char_to_indices: dict[str, list[int]] = {}
    for index, char in enumerate(ring):
        if char not in char_to_indices:
            char_to_indices[char] = []
        char_to_indices[char].append(index)

    # dp[i][j] represents the minimum cost to have typed the first i characters
    # of the key, ending at position j in the ring.
    # Initialize with infinity.
    inf = float('inf')
    dp: list[list[float]] = [[inf] * ring_len for _ in range(key_len + 1)]

    # Base case: Before typing any characters, we are at position 0 with cost 0.
    # However, the problem implies we start at position 0, but the first character
    # typed also incurs a cost based on distance from 0 to its position.
    # To simplify, we treat the "0-th" state as being at index 0 with cost 0.
    dp[0][0] = 0

    for i in range(key_len):
        target_char = key[i]
        if target_char not in char_to_indices:
            return -1
        
        target_indices = char_to_indices[target_char]

        # For every possible current position in the ring from the previous step
        for current_pos in range(ring_len):
            if dp[i][current_pos] == inf:
                continue

            # Try moving to every possible occurrence of the target character
            for next_pos in target_indices:
                # Calculate circular distance
                dist = abs(next_pos - current_pos)
                move_cost = min(dist, ring_len - dist)
                
                # Total cost = previous cost + movement + 1 (for typing the char)
                new_cost = dp[i][current_pos] + move_cost + 1
                
                if new_cost < dp[i + 1][next_pos]:
                    dp[i + 1][next_pos] = new_cost

    # The answer is the minimum value in the last row of the DP table
    result = min(dp[key_len])
    return int(result) if result != inf else -1
