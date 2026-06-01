METADATA = {
    "id": 446,
    "name": "Arithmetic Slices II - Subsequence",
    "slug": "arithmetic-slices-ii-subsequence",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "hash_map", "array"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the total number of arithmetic subsequences in an array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the total number of arithmetic subsequences in the given list.

    An arithmetic subsequence is a subsequence where the difference between 
    any two consecutive elements is constant. The length must be at least 3.

    Args:
        nums: A list of integers.

    Returns:
        The total count of arithmetic subsequences.

    Examples:
        >>> solve([2, 4, 6, 8, 10])
        7
        >>> solve([7, 7, 7, 7, 7])
        12
        >>> solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        50
    """
    n = len(nums)
    total_count = 0
    
    # dp[i] is a dictionary where key is the common difference 'diff'
    # and value is the number of arithmetic subsequences ending at index i 
    # with that difference. Note: these counts include subsequences of length 2.
    dp: list[dict[int, int]] = [{} for _ in range(n)]

    for current_index in range(n):
        for previous_index in range(current_index):
            # Calculate the common difference
            diff = nums[current_index] - nums[previous_index]
            
            # Get the number of existing subsequences ending at previous_index 
            # with the same difference.
            # If no such subsequence exists, count is 0.
            prev_count = dp[previous_index].get(diff, 0)
            
            # Every subsequence ending at previous_index with 'diff' can be 
            # extended by nums[current_index] to form a subsequence of length >= 3.
            # We add prev_count to the total result.
            total_count += prev_count
            
            # Update dp[current_index][diff]. 
            # We add (prev_count + 1) to the existing count.
            # The '+ 1' represents the new arithmetic subsequence of length 2 
            # formed by (nums[previous_index], nums[current_index]).
            dp[current_index][diff] = dp[current_index].get(diff, 0) + prev_count + 1

    return total_count
