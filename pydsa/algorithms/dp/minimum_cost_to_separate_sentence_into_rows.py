METADATA = {
    "id": 2052,
    "name": "Minimum Cost to Separate Sentence Into Rows",
    "slug": "minimum-cost-to-separate-sentence-into-rows",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the minimum cost to split a sentence into rows such that no row exceeds a maximum length and the cost is calculated based on the number of rows.",
}

def solve(sentence: str, max_length: int, cost_per_row: int) -> int:
    """
    Calculates the minimum cost to split a sentence into rows.

    Args:
        sentence: The input string to be split.
        max_length: The maximum number of characters allowed in a single row.
        cost_per_row: The cost incurred for each row created.

    Returns:
        The minimum total cost to separate the sentence.

    Examples:
        >>> solve("abcde", 3, 10)
        20
        >>> solve("aaaaa", 2, 5)
        15
    """
    n = len(sentence)
    # dp[i] represents the minimum cost to split the prefix sentence[0:i]
    # Initialize with infinity as we want to minimize the cost.
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        # Try all possible lengths for the last row ending at index i-1
        # The row can have length from 1 up to max_length
        for length in range(1, max_length + 1):
            start_index = i - length
            
            # If start_index is negative, the current row length is invalid
            if start_index < 0:
                break
            
            # If the previous state is reachable, update the current state
            # Cost = cost of previous split + cost of the new row
            if dp[start_index] != float('inf'):
                dp[i] = min(dp[i], dp[start_index] + cost_per_row)

    return int(dp[n])
