METADATA = {
    "id": 2245,
    "name": "Maximum Trailing Zeros in a Cornered Path",
    "slug": "maximum-trailing-zeros-in-a-cornered-path",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math"],
    "difficulty": "hard",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the maximum number of trailing zeros in a path from top-left to bottom-right in a grid of integers.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the maximum number of trailing zeros in a path from (0,0) to (m-1, n-1).
    
    Trailing zeros are determined by the minimum of the counts of prime factors 2 and 5.
    Since the product can be extremely large, we track the counts of 2s and 5s separately.

    Args:
        grid: A 2D list of integers representing the grid.

    Returns:
        The maximum number of trailing zeros possible in any valid path.

    Examples:
        >>> solve([[10, 1, 1], [1, 1, 1], [1, 1, 10]])
        1
        >>> solve([[2, 5], [5, 2]])
        1
    """
    rows = len(grid)
    cols = len(grid[0])

    def get_prime_counts(num: int) -> tuple[int, int]:
        """Helper to count factors of 2 and 5 in a number."""
        count2 = 0
        count5 = 0
        if num == 0:
            # In most LeetCode contexts, 0 is treated as having infinite factors,
            # but usually, grid values are positive. If 0 is possible, 
            # it would technically make the product 0 (trailing zeros undefined/infinite).
            # We assume positive integers based on standard problem constraints.
            return 0, 0
        
        temp = num
        while temp > 0 and temp % 2 == 0:
            count2 += 1
            temp //= 2
        
        temp = num
        while temp > 0 and temp % 5 == 0:
            count5 += 1
            temp //= 5
        return count2, count5

    # dp_2[r][c] stores the maximum number of factor 2s reachable at (r, c)
    # dp_5[r][c] stores the maximum number of factor 5s reachable at (r, c)
    # However, we need to maximize min(count2, count5). 
    # This is a multi-objective optimization problem.
    # Since we want to maximize the minimum, and the path is fixed (down/right),
    # we can use DP to store the maximum possible count of 5s for every possible count of 2s.
    # But given the constraints and the nature of trailing zeros, 
    # we actually need to track the maximum 5s for a given number of 2s.
    
    # Optimization: The number of factors of 2 or 5 in a single number is small (log2(10^9) ~ 30).
    # The total number of factors in a path is at most (m+n) * 30.
    # For a 100x100 grid, max factors ~ 6000.
    
    # Let's use a simpler DP approach: dp[r][c] = set of (count2, count5) pairs.
    # To keep it efficient, we only keep "Pareto optimal" pairs.
    # A pair (a, b) is better than (c, d) if a >= c and b >= d.
    
    dp: list[list[list[tuple[int, int]]]] = [[[] for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            c2, c5 = get_prime_counts(grid[r][c])
            
            if r == 0 and c == 0:
                dp[r][c] = [(c2, c5)]
                continue
            
            # Collect all possible (count2, count5) from top and left neighbors
            candidates = []
            if r > 0:
                candidates.extend(dp[r-1][c])
            if c > 0:
                candidates.extend(dp[r][c-1])
            
            # Add current cell's factors to all candidates
            new_pairs = []
            for p2, p5 in candidates:
                new_pairs.append((p2 + c2, p5 + c5))
            
            # Pruning: Keep only Pareto optimal pairs to prevent exponential growth
            # Sort by count2 descending, then count5 descending
            new_pairs.sort(key=lambda x: (-x[0], -x[1]))
            
            pruned = []
            max_5_so_far = -1
            for p2, p5 in new_pairs:
                # If this pair has more 5s than any pair with >= 2s seen so far, it's useful
                if p5 > max_5_so_far:
                    pruned.append((p2, p5))
                    max_5_so_far = p5
            dp[r][c] = pruned

    # The answer is the maximum min(count2, count5) in the last cell
    max_zeros = 0
    for p2, p5 in dp[rows-1][cols-1]:
        max_zeros = max(max_zeros, min(p2, p5))
        
    return max_zeros
