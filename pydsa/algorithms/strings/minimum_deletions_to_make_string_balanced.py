METADATA = {
    "id": 1653,
    "name": "Minimum Deletions to Make String Balanced",
    "slug": "minimum-deletions-to-make-string-balanced",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "prefix_sum", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of deletions required to make a binary string balanced, where all '0's come before all '1's.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum number of deletions to make a binary string balanced.
    A string is balanced if all '0's appear before all '1's.

    Args:
        s: A string consisting of '0's and '1's.

    Returns:
        The minimum number of deletions required.

    Examples:
        >>> solve("01011")
        1
        >>> solve("0011")
        0
        >>> solve("111000")
        3
    """
    # We can solve this by iterating through the string and maintaining 
    # the count of '1's encountered so far. 
    # If we encounter a '0', we have two choices to maintain balance:
    # 1. Delete this '0'.
    # 2. Delete all '1's encountered before this '0'.
    
    deletions = 0
    ones_count = 0
    
    for char in s:
        if char == '1':
            # Keep track of '1's that might need to be deleted later
            ones_count += 1
        else:
            # We found a '0'. To keep the string balanced, we must either:
            # - Delete this '0' (increment deletions)
            # - Delete all previous '1's (the current ones_count)
            # We take the minimum of these two strategies.
            # The 'deletions' variable tracks the cost of removing '0's 
            # to match the current '1's count.
            deletions = min(deletions + 1, ones_count)
            
    return deletions
