METADATA = {
    "id": 1547,
    "name": "Minimum Cost to Cut a Stick",
    "slug": "minimum-cost-to-cut-a-stick",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "intervals"],
    "difficulty": "hard",
    "time_complexity": "O(m^3)",
    "space_complexity": "O(m^2)",
    "description": "Find the minimum cost to cut a stick at given positions using interval dynamic programming.",
}

def solve(n: int, cuts: list[int]) -> int:
    """
    Calculates the minimum cost to cut a stick of length n at specified positions.

    The cost of a cut is the length of the stick segment being cut. We use 
    interval dynamic programming where dp[i][j] represents the minimum cost 
    to perform all cuts within the segment defined by cuts[i] and cuts[j].

    Args:
        n: The total length of the stick.
        cuts: A list of integers representing the positions where the stick must be cut.

    Returns:
        The minimum total cost to perform all cuts.

    Examples:
        >>> solve(7, [1, 3, 4, 5])
        16
        >>> solve(9, [5, 6, 1, 5, 2]) # Note: input might not be sorted
        22
    """
    # Add the boundaries of the stick (0 and n) to the cuts list
    # and sort them to define clear intervals.
    sorted_cuts = sorted([0] + cuts + [n])
    m = len(sorted_cuts)
    
    # dp[i][j] will store the minimum cost to cut the stick segment 
    # between sorted_cuts[i] and sorted_cuts[j].
    dp = [[0] * m for _ in range(m)]

    # length is the number of segments between indices i and j.
    # We need at least 2 segments (i and i+2) to have a cut in between.
    for length in range(2, m):
        for i in range(m - length):
            j = i + length
            
            # The cost to make the current cut is the length of the current segment.
            current_segment_length = sorted_cuts[j] - sorted_cuts[i]
            
            # Find the optimal cut position 'k' between i and j.
            # We initialize with a very large value.
            min_cut_cost = float('inf')
            for k in range(i + 1, j):
                # The cost is the current segment length + costs of sub-problems.
                cost = dp[i][k] + dp[k][j]
                if cost < min_cut_cost:
                    min_cut_cost = cost
            
            # If no cut was possible (length < 2), min_cut_cost remains inf.
            # However, our loop range ensures length >= 2, so k always exists.
            dp[i][j] = current_segment_length + min_cut_cost

    # The answer is the minimum cost to cut the segment from index 0 to m-1.
    return int(dp[0][m - 1])
