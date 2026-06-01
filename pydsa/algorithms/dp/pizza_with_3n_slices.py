METADATA = {
    "id": 1388,
    "name": "Pizza With 3n Slices",
    "slug": "pizza-with-3n-slices",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Maximize the sum of slices picked by two players where each player picks n non-adjacent slices from a circular pizza of 3n slices.",
}

def solve(slices: list[int]) -> int:
    """
    Calculates the maximum sum of slices the first player can get.
    
    The problem is equivalent to picking n non-adjacent elements from a 
    circular array. Since the first and last elements are adjacent, we 
    split the problem into two linear cases:
    1. Exclude the last element (indices 0 to 3n-2).
    2. Exclude the first element (indices 1 to 3n-1).
    
    For each case, we use DP to find the maximum sum of n non-adjacent elements.
    The second player will always pick the remaining elements that maximize 
    the first player's outcome (effectively, the second player's optimal 
    strategy is to pick elements that leave the best possible set for the first player).
    Actually, the problem simplifies to: the first player wants to maximize 
    their sum, and the second player's picks are implicitly determined by 
    the non-adjacency rule. In the linear version, picking n non-adjacent 
    elements from 3n-1 elements is equivalent to a DP where we track 
    how many elements we have picked.

    Args:
        slices: A list of integers representing the number of slices in each piece.

    Returns:
        The maximum sum of slices the first player can obtain.

    Examples:
        >>> solve([1, 2, 3, 4])
        4
        >>> solve([1, 2, 3, 4, 5, 6])
        9
    """
    n_total = len(slices)
    n_to_pick = n_total // 3

    def max_non_adjacent_sum(arr: list[int], k: int) -> int:
        """
        Finds the maximum sum of k non-adjacent elements in a linear array.
        Uses DP: dp[i][j] is the max sum using j elements from the first i elements.
        """
        m = len(arr)
        if k == 0:
            return 0
        if m < 2 * k - 1:
            return 0

        # dp[i][j] = max sum using j elements from the first i elements of arr
        # To optimize space, we can use dp[j] but for clarity we use 2D or 
        # a slightly optimized version. Given n is small (up to 100), O(n^2) is fine.
        # dp[i][j] represents max sum using j elements from first i elements.
        # dp[i][j] = max(dp[i-1][j], dp[i-2][j-1] + arr[i-1])
        
        # We use a 2D array where dp[i][j] is max sum using j elements from first i elements
        dp = [[0] * (k + 1) for _ in range(m + 1)]

        for j in range(1, k + 1):
            # To pick j non-adjacent elements, we need at least 2j-1 elements
            for i in range(2 * j - 1, m + 1):
                # Option 1: Don't pick the current element arr[i-1]
                # Option 2: Pick the current element arr[i-1] and the best from i-2 elements
                pick_current = dp[i - 2][j - 1] + arr[i - 1]
                skip_current = dp[i - 1][j]
                dp[i][j] = max(pick_current, skip_current)
        
        return dp[m][k]

    # Case 1: Exclude the last element (allows picking index 0)
    # Case 2: Exclude the first element (allows picking index 3n-1)
    # This handles the circular constraint.
    case1 = max_non_adjacent_sum(slices[:-1], n_to_pick)
    case2 = max_non_adjacent_sum(slices[1:], n_to_pick)

    return max(case1, case2)
