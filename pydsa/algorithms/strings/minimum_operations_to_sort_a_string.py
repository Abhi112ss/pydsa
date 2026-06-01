METADATA = {
    "id": 3863,
    "name": "Minimum Operations to Sort a String",
    "slug": "minimum-operations-to-sort-a-string",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting", "permutation"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of operations to sort a string by moving elements to any position.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum number of operations to sort a string.
    An operation consists of picking any character and moving it to any position.
    The minimum number of operations is equivalent to (Total Length - Length of Longest Non-Decreasing Subsequence).
    However, since we are dealing with characters and the goal is a sorted string, 
    the problem is equivalent to finding the Longest Non-Decreasing Subsequence (LNDS) 
    of the characters in their current order.

    Args:
        s: The input string to be sorted.

    Returns:
        The minimum number of operations required to sort the string.

    Examples:
        >>> solve("bac")
        2
        >>> solve("aabbc")
        0
        >>> solve("dcba")
        3
    """
    if not s:
        return 0

    # Convert string to list of integers (ASCII values) for easier processing
    nums = [ord(char) for char in s]
    n = len(nums)

    # To find the minimum operations to sort, we need to find the 
    # Longest Non-Decreasing Subsequence (LNDS). 
    # The elements in the LNDS are already in the correct relative order 
    # and do not need to be moved.
    
    # tails[i] will store the smallest tail of all non-decreasing subsequences of length i+1
    tails = []

    for x in nums:
        # We use binary search to find the insertion point to maintain the non-decreasing property.
        # bisect_right is used because we want a non-decreasing subsequence (allows duplicates).
        
        import bisect
        idx = bisect.bisect_right(tails, x)
        
        if idx < len(tails):
            # If x can replace an existing tail to make it smaller, do so.
            tails[idx] = x
        else:
            # If x is greater than or equal to all current tails, extend the subsequence.
            tails.append(x)

    # The length of tails is the length of the Longest Non-Decreasing Subsequence.
    lnds_length = len(tails)

    # Minimum operations = Total elements - elements that stay in place (LNDS)
    return n - lnds_length
