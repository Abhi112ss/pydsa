METADATA = {
    "id": 1959,
    "name": "Minimum Total Space Wasted With K Resizing Operations",
    "slug": "minimum-total-space-wasted-with-k-resizing-operations",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "array", "partitioning"],
    "difficulty": "medium",
    "time_complexity": "O(k * n^2)",
    "space_complexity": "O(k * n)",
    "description": "Find the minimum total wasted space by partitioning an array into at most k+1 segments, where each segment's size is determined by its maximum element.",
}

def solve(sizes: list[int], k: int) -> int:
    """
    Calculates the minimum total wasted space by partitioning the array into at most k+1 segments.

    Args:
        sizes: A list of integers representing the size of each task.
        k: The maximum number of resizing operations allowed.

    Returns:
        The minimum total wasted space.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 2)
        2
        >>> solve([3, 1, 2], 0)
        3
    """
    n = len(sizes)
    
    # Precompute the cost of a single segment [i, j]
    # cost[i][j] = (max(sizes[i...j]) * (j - i + 1)) - sum(sizes[i...j])
    # This represents the wasted space if we don't resize within this segment.
    segment_waste = [[0] * n for _ in range(n)]
    
    for i in range(n):
        current_max = 0
        current_sum = 0
        for j in range(i, n):
            current_max = max(current_max, sizes[j])
            current_sum += sizes[j]
            segment_waste[i][j] = (current_max * (j - i + 1)) - current_sum

    # dp[i][j] = minimum waste for the first j elements using exactly i segments.
    # We want to find the minimum waste using 1 to k+1 segments.
    # To simplify, we use dp[i][j] as min waste for prefix of length j using i segments.
    # Initialize with infinity.
    inf = float('inf')
    dp = [[inf] * (n + 1) for _ in range(k + 2)]
    
    # Base case: 0 elements with 0 segments costs 0.
    dp[0][0] = 0
    
    # Iterate through the number of segments allowed (from 1 to k+1)
    for i in range(1, k + 2):
        # Iterate through the end position of the current prefix
        for j in range(1, n + 1):
            # Try all possible split points 'p' to form the i-th segment from [p, j-1]
            # The previous i-1 segments covered elements up to index p.
            for p in range(j):
                if dp[i-1][p] != inf:
                    # The cost is the min waste of previous segments + waste of the new segment
                    cost = dp[i-1][p] + segment_waste[p][j-1]
                    if cost < dp[i][j]:
                        dp[i][j] = cost
                        
    # The answer is the minimum waste using any number of segments from 1 to k+1
    # that covers all n elements.
    ans = inf
    for i in range(1, k + 2):
        ans = min(ans, dp[i][n])
        
    return int(ans)
