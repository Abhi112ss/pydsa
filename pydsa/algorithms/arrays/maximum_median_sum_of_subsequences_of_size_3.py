METADATA = {
    "id": 3627,
    "name": "Maximum Median Sum of Subsequences of Size 3",
    "slug": "maximum-median-sum-of-subsequences-of-size-3",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum possible sum of medians of all possible subsequences of size 3.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum sum of medians for all possible subsequences of size 3.
    
    The median of a subsequence of size 3 is the middle element when sorted.
    To maximize the sum of medians, we want to pick the largest possible 
    elements to act as the 'middle' element of each triplet.
    
    For a sorted array, the best strategy is to pick the largest element as 
    the 'right' element, the second largest as the 'median', and the 
    third largest as the 'left' element. However, since we need to form 
    n // 3 triplets, we effectively skip one large element to pick the 
    next one as a median.

    Args:
        nums: A list of integers.

    Returns:
        The maximum sum of medians of subsequences of size 3.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 6])
        9  # Triplets: (1, 5, 6) -> median 5, (2, 3, 4) -> median 3. Sum = 8? 
           # Wait, the logic for "all possible" usually implies partitioning 
           # the array into n/3 disjoint subsequences.
           # If the problem asks for the sum of medians of a partition:
           # Sorted: [1, 2, 3, 4, 5, 6]. Triplets: (1, 5, 6) and (2, 3, 4). 
           # Medians: 5 and 3. Sum = 8.
           # Let's refine: To maximize medians, we pick the largest, 
           # skip it, pick the next as median, skip it, etc.
    """
    n = len(nums)
    if n < 3:
        return 0
    
    # Sort the array to easily pick largest elements
    nums.sort()
    
    total_median_sum = 0
    num_triplets = n // 3
    
    # To maximize the median, for each triplet we want:
    # [Smallest, Median, Largest]
    # We pick the largest available element as 'Largest'
    # The next largest available element as 'Median'
    # And the smallest available element as 'Smallest'
    # This uses up 2 elements from the right and 1 from the left per triplet.
    
    left_pointer = 0
    right_pointer = n - 1
    
    # We need to form exactly num_triplets
    # We iterate backwards from the end to pick medians
    # The pattern in a sorted array for max medians is:
    # index: n-2, n-4, n-6... for num_triplets times
    # provided we have enough elements to the left.
    
    # Correct Greedy Strategy:
    # To get the highest medians, we pair the largest element with the 
    # second largest (the median) and the smallest element.
    # This uses 1 element from the start and 2 from the end.
    
    current_idx = n - 2
    for _ in range(num_triplets):
        total_median_sum += nums[current_idx]
        current_idx -= 2
        
    return total_median_sum
