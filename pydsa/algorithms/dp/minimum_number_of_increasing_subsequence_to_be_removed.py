METADATA = {
    "id": 3231,
    "name": "Minimum Number of Increasing Subsequences to Be Removed",
    "slug": "minimum-number-of-increasing-subsequences-to-be-removed",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "arrays", "dilworth's theorem"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of increasing subsequences needed to cover all elements in an array using Dilworth's Theorem.",
}

import bisect

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of increasing subsequences needed to cover the array.
    
    According to Dilworth's Theorem, the minimum number of increasing subsequences 
    required to cover a sequence is equal to the length of the longest 
    non-increasing subsequence.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest non-increasing subsequence.

    Examples:
        >>> solve([3, 1, 4, 2])
        2
        >>> solve([1, 2, 3, 4])
        1
        >>> solve([4, 3, 2, 1])
        4
    """
    if not nums:
        return 0

    # To find the Longest Non-Increasing Subsequence (LNIS), 
    # we can transform the problem. A non-increasing subsequence 
    # in 'nums' is equivalent to a non-decreasing subsequence 
    # in the reversed array, or we can process the array and 
    # maintain a list for the 'patience sorting' approach.
    
    # However, a simpler way to find LNIS is to find the 
    # Longest Non-Decreasing Subsequence of the array after 
    # multiplying all elements by -1, or by using a modified 
    # binary search on a tails array.
    
    # Let's use the tails approach for Longest Non-Increasing Subsequence:
    # We want to find a subsequence where a[i] >= a[j] for i < j.
    # This is equivalent to finding the Longest Non-Decreasing Subsequence 
    # on the reversed array.
    
    reversed_nums = nums[::-1]
    
    # tails[i] will store the smallest tail of all non-decreasing 
    # subsequences of length i + 1.
    tails: list[int] = []
    
    for x in reversed_nums:
        # bisect_right finds the insertion point to maintain order 
        # while allowing duplicate values (non-decreasing).
        idx = bisect.bisect_right(tails, x)
        
        if idx < len(tails):
            tails[idx] = x
        else:
            tails.append(x)
            
    # The length of the tails array is the length of the 
    # Longest Non-Decreasing Subsequence of the reversed array,
    # which is the Longest Non-Increasing Subsequence of the original.
    return len(tails)
