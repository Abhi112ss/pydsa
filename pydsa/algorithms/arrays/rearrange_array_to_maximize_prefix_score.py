METADATA = {
    "id": 2587,
    "name": "Rearrange Array to Maximize Prefix Score",
    "slug": "rearrange-array-to-maximize-prefix-score",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Rearrange two arrays to maximize the sum of absolute differences of their prefixes.",
}

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Rearranges the elements of nums1 and nums2 to maximize the prefix score.
    The prefix score is defined as the sum of |sum(nums1[:i]) - sum(nums2[:i])| for all i.

    To maximize the absolute difference at each step, we want to make the running 
    sums of the two arrays move in opposite directions as much as possible. 
    This is achieved by sorting one array in ascending order and the other in 
    descending order.

    Args:
        nums1: A list of integers.
        nums2: A list of integers.

    Returns:
        The maximum possible prefix score.

    Examples:
        >>> solve([4, 2, 5, 3], [2, 1, 3, 4])
        22
        >>> solve([1, 1, 1, 1], [1, 1, 1, 1])
        0
    """
    n = len(nums1)
    
    # Sort one array ascending and the other descending to maximize 
    # the divergence of their prefix sums.
    sorted_nums1 = sorted(nums1)
    sorted_nums2 = sorted(nums2, reverse=True)
    
    total_prefix_score = 0
    current_sum1 = 0
    current_sum2 = 0
    
    for i in range(n):
        # Update running prefix sums
        current_sum1 += sorted_nums1[i]
        current_sum2 += sorted_nums2[i]
        
        # Add the absolute difference of the current prefix sums to the total score
        total_prefix_score += abs(current_sum1 - current_sum2)
        
    return total_prefix_score
