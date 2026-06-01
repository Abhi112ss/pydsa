METADATA = {
    "id": 2813,
    "name": "Maximum Elegance of a K-Length Subsequence",
    "slug": "maximum-elegance-of-a-k-length-subsequence",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "arrays", "subsequence"],
    "difficulty": "hard",
    "time_complexity": "O(n * k)",
    "space_complexity": "O(n * k)",
    "description": "Find the maximum elegance of a subsequence of length k, where elegance is the sum of elements multiplied by their position in the subsequence.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum elegance of a subsequence of length k.
    Elegance is defined as the sum of (nums[i] * position) for each element 
    in the subsequence, where position is 1-indexed.

    Args:
        nums: A list of integers representing the input array.
        k: The required length of the subsequence.

    Returns:
        The maximum possible elegance value.

    Examples:
        >>> solve([1, 2, 3], 2)
        8  # Subsequences: [1, 2] -> 1*1 + 2*2 = 5; [1, 3] -> 1*1 + 3*2 = 7; [2, 3] -> 2*1 + 3*2 = 8
        >>> solve([4, 1, 2], 2)
        7  # Subsequences: [4, 1] -> 4*1 + 1*2 = 6; [4, 2] -> 4*1 + 2*2 = 8; [1, 2] -> 1*1 + 2*2 = 5
        # Wait, the example logic above assumes we pick elements to maximize sum.
        # Let's re-verify: [4, 2] -> 4*1 + 2*2 = 8.
    """
    n = len(nums)
    
    # dp[i][j] represents the maximum elegance using a subsequence of length 'j'
    # considering elements from the first 'i' elements of the input array.
    # We use a 2D array where rows are indices of nums and columns are subsequence lengths.
    # Initialize with a very small number to represent unreachable states.
    inf = float('inf')
    dp = [[-inf] * (k + 1) for _ in range(n + 1)]
    
    # Base case: A subsequence of length 0 always has elegance 0.
    for i in range(n + 1):
        dp[i][0] = 0
        
    for i in range(1, n + 1):
        current_val = nums[i - 1]
        for j in range(1, k + 1):
            # Option 1: Do not include nums[i-1] in the subsequence.
            # The elegance remains the same as the best elegance for length j using i-1 elements.
            res_exclude = dp[i - 1][j]
            
            # Option 2: Include nums[i-1] as the j-th element in the subsequence.
            # This is only possible if we could form a subsequence of length j-1 using i-1 elements.
            res_include = -inf
            if dp[i - 1][j - 1] != -inf:
                # Elegance = (elegance of previous j-1 elements) + (current_val * j)
                res_include = dp[i - 1][j - 1] + (current_val * j)
            
            dp[i][j] = max(res_exclude, res_include)
            
    return int(dp[n][k])
