METADATA = {
    "id": 3409,
    "name": "Longest Subsequence With Decreasing Adjacent Difference",
    "slug": "longest_subsequence_with_decreasing_adjacent_difference",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "subsequence"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the length of the longest subsequence where the absolute difference between adjacent elements is strictly decreasing.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest subsequence where the absolute difference 
    between consecutive elements is strictly decreasing.

    Args:
        nums: A list of integers representing the input sequence.

    Returns:
        The length of the longest subsequence satisfying the condition.

    Examples:
        >>> solve([10, 5, 8, 2, 1])
        4
        # Subsequence [10, 5, 8, 2] -> diffs: |10-5|=5, |5-8|=3, |8-2|=6 (Not decreasing)
        # Subsequence [10, 8, 5, 2] -> diffs: |10-8|=2, |8-5|=3 (Not decreasing)
        # Subsequence [10, 5, 2] -> diffs: |10-5|=5, |5-2|=3 (Decreasing)
    """
    n = len(nums)
    if n <= 2:
        return n

    # dp[i][diff] stores the length of the longest subsequence ending at index i
    # where the last difference was 'diff'.
    # Since diff can be up to 10^5 (based on typical constraints), 
    # we use a list of dictionaries to save space for sparse differences.
    # However, for O(n^2) complexity, we iterate through all previous indices.
    
    # dp[i] is a dictionary where key = last_diff, value = max_length
    dp: list[dict[int, int]] = [{} for _ in range(n)]
    max_len = 1

    for i in range(n):
        # Every single element is a subsequence of length 1
        # But the condition requires "adjacent difference", so we start building from pairs.
        for j in range(i):
            current_diff = abs(nums[i] - nums[j])
            
            # Base case: a subsequence of length 2 (nums[j], nums[i])
            # This subsequence has one difference: current_diff.
            # We initialize it with length 2.
            if current_diff not in dp[i] or dp[i][current_diff] < 2:
                dp[i][current_diff] = 2
            
            # Transition: Look at subsequences ending at j
            # We need the previous difference (prev_diff) to be > current_diff
            for prev_diff, length in dp[j].items():
                if prev_diff > current_diff:
                    # If the condition holds, we extend the subsequence
                    new_length = length + 1
                    if current_diff not in dp[i] or dp[i][current_diff] < new_length:
                        dp[i][current_diff] = new_length
            
            max_len = max(max_len, dp[i][current_diff])

    return max_len

# Note: The problem description implies a specific constraint on the difference.
# If the problem implies the difference must be strictly decreasing:
# diff_1 > diff_2 > diff_3 ...
# The DP state dp[i][last_diff] = max length ending at i with last_diff is correct.
