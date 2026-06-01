METADATA = {
    "id": 276,
    "name": "Paint Fence",
    "slug": "paint_fence",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of ways to paint a fence with n posts and k colors such that no more than two adjacent posts have the same color.",
}

def solve(n: int, k: int) -> int:
    """
    Calculates the number of ways to paint a fence with n posts and k colors
    such that no more than two adjacent posts have the same color.

    Args:
        n: The number of posts in the fence.
        k: The number of available colors.

    Returns:
        The total number of valid ways to paint the fence.

    Examples:
        >>> solve(2, 2)
        4
        >>> solve(3, 2)
        6
    """
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return k
    
    # same[i] is the number of ways to paint post i the same color as post i-1.
    # diff[i] is the number of ways to paint post i a different color than post i-1.
    # For n=2:
    # same = k * 1 (post 1 and 2 are same color)
    # diff = k * (k-1) (post 1 and 2 are different colors)
    
    same = k
    diff = k * (k - 1)
    
    # Total ways for 2 posts
    total = same + diff
    
    # Iterate from the 3rd post to the n-th post
    for _ in range(3, n + 1):
        # To paint post i the same color as i-1, post i-1 must have been 
        # different from i-2 (to avoid 3 in a row) OR i-1 was the start of a pair.
        # Actually, the rule is: post i is same as i-1 ONLY if i-1 was different from i-2.
        # Therefore, same[i] = diff[i-1]
        # To paint post i different from i-1, i-1 could have been same or different.
        # Therefore, diff[i] = (same[i-1] + diff[i-1]) * (k - 1)
        
        prev_diff = diff
        prev_same = same
        
        # New 'same' ways: post i must be same as i-1, but i-1 must have been different from i-2
        same = prev_diff
        
        # New 'diff' ways: post i is different from i-1. i-1 could be anything.
        diff = (prev_same + prev_diff) * (k - 1)
        
        total = same + diff
        
    return total
