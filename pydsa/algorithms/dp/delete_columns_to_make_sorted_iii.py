METADATA = {
    "id": 960,
    "name": "Delete Columns to Make Sorted III",
    "slug": "delete-columns-to-make-sorted-iii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "longest_increasing_subsequence"],
    "difficulty": "hard",
    "time_complexity": "O(n^2 * m)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of columns to delete so that the remaining columns are non-decreasing in every row.",
}

def solve(columns: list[str]) -> int:
    """
    Finds the minimum number of columns to delete so that every remaining 
    column is non-decreasing across all rows.

    The problem is equivalent to finding the Longest Increasing Subsequence (LIS) 
    of columns, where a column 'j' can follow column 'i' if for all rows 'r', 
    columns[r][i] <= columns[r][j].

    Args:
        columns: A list of strings where each string represents a row.

    Returns:
        The minimum number of columns to delete.

    Examples:
        >>> solve(["abc", "def"])
        0
        >>> solve(["ca", "bb", "ac"])
        1
    """
    if not columns or not columns[0]:
        return 0

    num_rows = len(columns)
    num_cols = len(columns[0])

    # dp[j] will store the length of the longest valid subsequence of columns ending at index j
    dp = [1] * num_cols

    for j in range(num_cols):
        for i in range(j):
            # Check if column i can precede column j in a non-decreasing sequence
            # This must hold true for every single row
            is_valid_transition = True
            for row_idx in range(num_rows):
                if columns[row_idx][i] > columns[row_idx][j]:
                    is_valid_transition = False
                    break
            
            # If valid, update the DP state for the longest subsequence ending at j
            if is_valid_transition:
                dp[j] = max(dp[j], dp[i] + 1)

    # The answer is total columns minus the length of the longest valid subsequence
    max_subsequence_length = max(dp) if dp else 0
    return num_cols - max_subsequence_length
