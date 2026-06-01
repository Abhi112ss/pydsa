METADATA = {
    "id": 3507,
    "name": "Minimum Pair Removal to Sort Array I",
    "slug": "minimum-pair-removal-to-sort-array-i",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of pairs to remove such that the remaining elements form a non-decreasing array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of pairs to remove to make the remaining array sorted.
    
    The problem asks for the minimum number of removals. Since each removal takes 
    two elements, minimizing removals is equivalent to maximizing the number 
    of elements kept in a non-decreasing sequence. However, the problem 
    constraint is specifically about removing *pairs*. 
    
    The optimal strategy is to find the longest non-decreasing subsequence 
    that can be formed by elements that were NOT part of a removed pair. 
    Actually, the problem simplifies to: how many elements can we keep?
    If we keep $K$ elements, we must have removed $(N - K)$ elements. 
    Since we remove in pairs, $(N - K)$ must be even.
    
    Wait, the standard interpretation of "Minimum Pair Removal to Sort" 
    usually implies we want to find the largest subset of indices $\{i_1, i_2, ... i_k\}$ 
    such that $nums[i_1] \le nums[i_2] \le ... \le nums[i_k]$ and the number 
    of elements removed $(n - k)$ is even.
    
    Args:
        nums: A list of integers.

    Returns:
        The minimum number of pairs to remove.

    Examples:
        >>> solve([1, 3, 2, 4])
        1
        >>> solve([1, 2, 3])
        0
        >>> solve([5, 4, 3, 2, 1])
        2
    """
    n = len(nums)
    if n == 0:
        return 0

    # To find the Longest Non-Decreasing Subsequence (LNDS)
    # We use the standard O(n log n) patience sorting approach.
    tails = []
    
    for x in nums:
        # Binary search for the first element > x to maintain non-decreasing property
        # bisect_right finds the insertion point to maintain order
        import bisect
        idx = bisect.bisect_right(tails, x)
        
        if idx < len(tails):
            tails[idx] = x
        else:
            tails.append(x)
            
    max_kept = len(tails)
    
    # We need to remove elements in pairs. 
    # Let k be the number of elements we keep.
    # The number of elements removed is (n - k).
    # This must be even, so (n - k) % 2 == 0.
    # If (n - k) is odd, we must reduce k by 1 to make (n - k) even.
    
    if (n - max_kept) % 2 != 0:
        max_kept -= 1
        
    # The number of pairs removed is (n - max_kept) // 2
    return (n - max_kept) // 2
