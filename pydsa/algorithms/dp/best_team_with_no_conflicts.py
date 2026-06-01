METADATA = {
    "id": 1626,
    "name": "Best Team With No Conflicts",
    "slug": "best-team-with-no-conflicts",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "sorting", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the maximum size of a team where no player in the team has a higher index and a lower score than another player.",
}

def solve(player_scores: list[int], player_indices: list[int]) -> int:
    """
    Finds the maximum size of a team such that no two players in the team conflict.
    A conflict occurs if one player has a higher index and a lower score than another.

    Args:
        player_scores: A list of integers representing the scores of each player.
        player_indices: A list of integers representing the indices of each player.

    Returns:
        The maximum number of players that can be in a team without conflicts.

    Examples:
        >>> solve([1, 3, 5], [0, 1, 2])
        3
        >>> solve([1, 2, 3, 4], [0, 1, 2, 3])
        4
        >>> solve([1, 5, 10, 11], [0, 1, 2, 3])
        4
        >>> solve([10, 1, 2, 3], [0, 1, 2, 3])
        3
    """
    # Combine scores and indices into pairs to keep them linked during sorting
    players = []
    for i in range(len(player_scores)):
        players.append((player_indices[i], player_scores[i]))

    # Sort players primarily by index. 
    # If indices are sorted, we only need to ensure scores are non-decreasing 
    # to avoid the conflict condition (index_i < index_j AND score_i > score_j).
    players.sort()

    n = len(players)
    # dp[i] stores the maximum team size ending with player i
    dp = [1] * n

    # We use a Longest Increasing Subsequence (LIS) approach on the scores.
    # Since players are already sorted by index, we look for the longest 
    # non-decreasing subsequence of scores.
    for i in range(n):
        current_score = players[i][1]
        for j in range(i):
            prev_score = players[j][1]
            # If the previous player's score is less than or equal to the current,
            # no conflict exists because index_j < index_i and score_j <= score_i.
            if prev_score <= current_score:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp) if dp else 0
