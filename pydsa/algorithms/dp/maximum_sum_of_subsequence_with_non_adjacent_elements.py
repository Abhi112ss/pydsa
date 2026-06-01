METADATA = {
    "id": 3165,
    "name": "Maximum Sum of Subsequence With Non-adjacent Elements",
    "slug": "maximum-sum-of-subsequence-with-non-adjacent-elements",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum sum of a subsequence such that no two elements in the subsequence are adjacent in the original array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum sum of a subsequence where no two elements are adjacent.

    This is a classic variation of the 'House Robber' problem. For each element, 
    we decide whether to include it (which means we must skip the previous element) 
    or exclude it (which means we take the maximum sum found up to the previous element).

    Args:
        nums: A list of non-negative integers.

    Returns:
        The maximum sum of a non-adjacent subsequence.

    Examples:
        >>> solve([1, 2, 3, 1])
        4
        >>> solve([2, 7, 9, 3, 1])
        12
        >>> solve([5, 5, 10, 100, 10, 5])
        110
    """
    if not nums:
        return 0

    # prev_max represents the maximum sum excluding the element immediately before the current one.
    # curr_max represents the maximum sum including or excluding the element immediately before.
    prev_max = 0
    curr_max = 0

    for num in nums:
        # Option 1: Include the current number. 
        # If we include 'num', we must add it to the max sum that did not include the previous element.
        include_current = prev_max + num
        
        # Option 2: Exclude the current number.
        # If we exclude 'num', the max sum is simply the best we had at the previous step.
        exclude_current = curr_max
        
        # The new maximum at this step is the best of both options.
        new_max = max(include_current, exclude_current)
        
        # Update state for the next iteration:
        # prev_max becomes the old curr_max (the max sum up to the previous index).
        # curr_max becomes the new_max (the max sum up to the current index).
        prev_max = curr_max
        curr_max = new_max

    return curr_max
