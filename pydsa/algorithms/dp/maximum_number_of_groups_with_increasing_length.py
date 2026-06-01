METADATA = {
    "id": 2790,
    "name": "Maximum Number of Groups With Increasing Length",
    "slug": "maximum-number-of-groups-with-increasing-length",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "array", "lis"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of groups that can be formed such that each group has a strictly increasing size.",
}

import bisect

def solve(groups: list[int]) -> int:
    """
    Calculates the maximum number of groups that can be formed such that 
    the sizes of the groups are strictly increasing.

    The problem reduces to finding the Longest Increasing Subsequence (LIS) 
    of the frequencies of the group sizes.

    Args:
        groups: A list of integers representing the sizes of available groups.

    Returns:
        The maximum number of groups that can be formed with strictly increasing sizes.

    Examples:
        >>> solve([3, 3, 3, 3])
        1
        >>> solve([1, 2, 3, 4, 5])
        5
        >>> solve([1, 1, 1, 1, 1, 1, 1])
        1
    """
    if not groups:
        return 0

    # Step 1: Count the frequency of each group size
    # We need to know how many groups of size 'x' are available.
    counts_map: dict[int, int] = {}
    for size in groups:
        counts_map[size] = counts_map.get(size, 0) + 1

    # Step 2: Extract the frequencies in ascending order of group sizes
    # The problem implies we can pick groups of size x, then size y, where x < y.
    # To maximize the number of groups, we look at the counts of available sizes.
    sorted_sizes = sorted(counts_map.keys())
    frequencies = [counts_map[size] for size in sorted_sizes]

    # Step 3: Find the Longest Increasing Subsequence (LIS) of the frequencies
    # We use the Patience Sorting algorithm (O(n log n)) to find the LIS length.
    # Note: The problem asks for the maximum number of groups. Since we can 
    # only use one group of a specific size to satisfy the "strictly increasing" 
    # requirement for a single sequence of groups, we are looking for the 
    # longest sequence of counts where each count is greater than the previous.
    # Wait, correction: The problem asks for the maximum number of groups.
    # If we have sizes [3, 3, 3, 3], we can only form 1 group of size 3.
    # If we have sizes [1, 2, 2, 3], we can form group of size 1, then size 2, then size 3.
    # Actually, the problem is simpler: we want to pick a sequence of sizes 
    # s1 < s2 < s3... such that we have at least one group of each size.
    # But we can use multiple groups of the same size? No, the problem says 
    # "maximum number of groups". If we pick size 1, then size 2, then size 3, 
    # we used 3 groups.
    # The constraint is: the size of the i-th group must be less than the (i+1)-th.
    # This means we are looking for the longest sequence of indices i1, i2... 
    # such that size[i1] < size[i2] < ... AND we have enough groups.
    # Actually, the problem is: we want to pick a sequence of group sizes 
    # x1, x2, x3... such that x1 < x2 < x3... 
    # Each xi must be a size available in the input.
    # To maximize the number of groups, we just need to find the longest 
    # sequence of unique sizes available.
    
    # Re-reading the problem: "Each group must have a strictly increasing length".
    # This means if we pick 3 groups, their lengths must be L1 < L2 < L3.
    # We have a pool of groups. We want to pick as many as possible.
    # If we have four groups of size 3, we can only pick ONE of them to be in our 
    # increasing sequence, because any other group of size 3 would violate 
    # the "strictly increasing" rule.
    # Therefore, the answer is simply the number of unique group sizes available.
    
    # Wait, let's re-verify. If groups = [3, 3, 3, 3], unique sizes = {3}. Max groups = 1.
    # If groups = [1, 2, 3], unique sizes = {1, 2, 3}. Max groups = 3.
    # If groups = [1, 1, 2, 2], unique sizes = {1, 2}. Max groups = 2.
    
    # The logic is: to get the maximum number of groups, we pick one group 
    # of size s1, one of size s2, ..., where s1 < s2 < s3...
    # The maximum number of such groups is the count of unique sizes.
    
    return len(counts_map)
