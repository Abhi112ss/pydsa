METADATA = {
    "id": 3441,
    "name": "Minimum Cost Good Caption",
    "slug": "minimum-cost-good-caption",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "strings"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum cost to transform a string into a 'good' caption where every character belongs to a contiguous segment of length at least 3.",
}

def solve(s: str, costs: list[int]) -> int:
    """
    Calculates the minimum cost to make a string 'good'. 
    A string is good if every character is part of a contiguous segment of 
    the same character with length at least 3.

    Args:
        s: The input string.
        costs: A list of integers representing the cost to change each character.

    Returns:
        The minimum cost to make the string good. Returns -1 if impossible.

    Examples:
        >>> solve("aaabbb", [0, 0, 0, 0, 0, 0])
        0
        >>> solve("abcde", [1, 1, 1, 1, 1])
        -1
    """
    n = len(s)
    if n == 0:
        return 0
    if n < 3:
        # A string shorter than 3 cannot have segments of length at least 3
        # unless it's empty, but the problem implies non-empty constraints.
        # If the string is non-empty and < 3, it's impossible.
        return -1

    # dp[i] represents the minimum cost to make the prefix s[0...i-1] good.
    # We initialize with infinity.
    inf = float('inf')
    dp = [inf] * (n + 1)
    dp[0] = 0

    # To optimize, we observe that a segment of length k >= 3 can be 
    # viewed as a segment of length 3 followed by segments of length 1.
    # However, the rule is every character must be in a segment of length >= 3.
    # This means we can transition from dp[i-3], dp[i-4], dp[i-5]...
    # But actually, any segment of length L >= 3 can be decomposed into 
    # segments of length 3 and 4 (since 3a + 4b can represent any integer >= 3 except 1, 2, 5 is 3+2? No).
    # Actually, any L >= 3 can be formed by segments of length 3 and 4? 
    # 3=3, 4=4, 5=no, 6=3+3, 7=3+4, 8=4+4. 
    # Wait, the rule is: a segment of length L must consist of the SAME character.
    # So if we decide s[i-k...i-1] is a segment of character 'c', 
    # the cost is sum of costs of changing s[j] to 'c' for j in [i-k, i-1].
    
    # Let's refine: dp[i] is min cost for s[0...i-1].
    # dp[i] = min(dp[i-k] + cost_to_make_segment(i-k, i, char)) for k >= 3.
    # This is still O(n^2). To get O(n), we notice that for a fixed character 'c',
    # we want to find min(dp[i-k] + cost_to_make_segment(i-k, i, 'c')) for k >= 3.
    # cost_to_make_segment(i-k, i, 'c') = sum_{j=i-k}^{i-1} (costs[j] if s[j] != 'c' else 0).
    # Let total_cost_to_char(i, 'c') = sum_{j=0}^{i-1} (costs[j] if s[j] != 'c' else 0).
    # Then cost_to_make_segment(i-k, i, 'c') = total_cost_to_char(i, 'c') - total_cost_to_char(i-k, 'c').
    # dp[i] = min_{char 'c'} [ min_{k >= 3} (dp[i-k] - total_cost_to_char(i-k, 'c')) + total_cost_to_char(i, 'c') ]

    # Precompute prefix sums for costs to change to each character 'a'-'z'
    # prefix_costs[char_idx][i] = sum of costs to make s[0...i-1] all char_idx
    prefix_costs = [[0] * (n + 1) for _ in range(26)]
    for i in range(n):
        char_idx = ord(s[i]) - ord('a')
        for c in range(26):
            cost_to_change = 0 if c == char_idx else costs[i]
            prefix_costs[c][i + 1] = prefix_costs[c][i] + cost_to_change

    # best_prev[c] stores the minimum value of (dp[j] - prefix_costs[c][j]) 
    # for all j such that the current i can form a segment of length >= 3 with j.
    # Specifically, for a fixed i, we need j <= i-3.
    # As i increases, the set of valid j's grows.
    best_prev = [inf] * 26

    for i in range(1, n + 1):
        # When we are at index i, the new possible j that becomes valid for 
        # segments ending at i is j = i - 3.
        j_new = i - 3
        if j_new >= 0:
            if dp[j_new] != inf:
                for c in range(26):
                    val = dp[j_new] - prefix_costs[c][j_new]
                    if val < best_prev[c]:
                        best_prev[c] = val
        
        # Calculate dp[i] using the best_prev values
        for c in range(26):
            if best_prev[c] != inf:
                current_cost = best_prev[c] + prefix_costs[c][i]
                if current_cost < dp[i]:
                    dp[i] = current_cost

    result = dp[n]
    return result if result != inf else -1
