METADATA = {
    "id": 3836,
    "name": "Maximum Score Using Exactly K Pairs",
    "slug": "maximum-score-using-exactly-k-pairs",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum score by selecting exactly k non-overlapping pairs from an array, where the score is the sum of absolute differences of the pairs.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum score possible by selecting exactly k non-overlapping pairs.
    The score is defined as the sum of the absolute differences of the elements in each pair.

    Args:
        nums: A list of integers.
        k: The number of pairs to select.

    Returns:
        The maximum possible sum of absolute differences for k pairs.

    Examples:
        >>> solve([1, 10, 5, 20], 2)
        24
        >>> solve([1, 2, 3, 4, 5], 2)
        6
    """
    n = len(nums)
    # To maximize the difference |a - b|, we want to pair elements that are far apart.
    # However, the problem constraints on "non-overlapping" usually imply 
    # we are picking indices. In the context of maximizing sum of differences 
    # for k pairs, sorting allows us to pick the largest available gaps.
    nums.sort()

    # The problem asks for exactly k pairs. To maximize the sum of differences,
    # we should pick the largest possible differences. 
    # In a sorted array, the largest differences are found by pairing 
    # the smallest elements with the largest elements (e.g., nums[n-1]-nums[0]).
    # However, if the pairs must be "non-overlapping" in terms of indices,
    # we are essentially picking 2k distinct indices.
    
    # To maximize sum(nums[high] - nums[low]), we want the k largest values 
    # to be the 'high' parts and the k smallest values to be the 'low' parts.
    # This is possible as long as 2k <= n.
    
    # Step 1: Identify the k smallest elements and k largest elements.
    # Since the array is sorted, these are the first k and last k elements.
    
    # Step 2: Calculate the sum of the k largest elements minus the sum of the k smallest.
    # This works because (nums[n-1] - nums[0]) + (nums[n-2] - nums[1]) ... 
    # is the maximum possible sum for k disjoint pairs.
    
    max_score = 0
    for i in range(k):
        max_score += nums[n - 1 - i] - nums[i]
        
    return max_score
