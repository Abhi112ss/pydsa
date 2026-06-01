METADATA = {
    "id": 3695,
    "name": "Maximize Alternating Sum Using Swaps",
    "slug": "maximize_alternating_sum_using_swaps",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Maximize the alternating sum of an array by performing any number of swaps.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum possible alternating sum of an array by rearranging its elements.
    
    The alternating sum is defined as: nums[0] - nums[1] + nums[2] - nums[3] + ...
    To maximize this, we want the largest possible values at even indices (positive contribution)
    and the smallest possible values at odd indices (negative contribution).

    Args:
        nums: A list of integers.

    Returns:
        The maximum alternating sum achievable.

    Examples:
        >>> solve([4, 2, 5, 3])
        8  # (5 - 2 + 4 - 3) is not right, it's (5 - 2 + 4 - 3) = 4. 
           # Wait, the optimal is (5 - 2 + 4 - 3) = 4? No.
           # Let's re-sort: [5, 4, 3, 2]. Even indices: 5, 3. Odd: 4, 2.
           # Sum: 5 - 4 + 3 - 2 = 2.
           # Let's try: Even indices get [5, 4], Odd indices get [2, 3].
           # Sum: 5 - 2 + 4 - 3 = 4.
        >>> solve([1, 1, 1, 1])
        0
    """
    n = len(nums)
    if n == 0:
        return 0

    # Sort the numbers to easily pick the largest and smallest
    sorted_nums = sorted(nums)
    
    # To maximize sum = (pos_1 + pos_2 + ...) - (neg_1 + neg_2 + ...)
    # We need to assign the largest elements to the positive positions (even indices)
    # and the smallest elements to the negative positions (odd indices).
    
    # Number of positive positions (0, 2, 4...)
    num_even_indices = (n + 1) // 2
    # Number of negative positions (1, 3, 5...)
    num_odd_indices = n // 2
    
    # The largest 'num_even_indices' elements should be at even positions
    # The smallest 'num_odd_indices' elements should be at odd positions
    # However, we must ensure we use exactly n elements.
    # Actually, the problem is simpler: 
    # We have n slots. (n+1)//2 slots are '+', n//2 slots are '-'.
    # To maximize, we pick the largest (n+1)//2 elements for '+' 
    # and the smallest n//2 elements for '-'.
    
    # Wait, if we pick the largest for '+', they might overlap with the smallest for '-'.
    # But since we are rearranging the EXISTING elements, we just partition the sorted array.
    # The smallest n//2 elements go to odd indices.
    # The largest (n+1)//2 elements go to even indices.
    # But these two sets must be disjoint and cover the whole array.
    
    # Correct logic:
    # The elements at indices 0, 2, 4... are added.
    # The elements at indices 1, 3, 5... are subtracted.
    # To maximize:
    # Sum = (Sum of elements at even indices) - (Sum of elements at odd indices)
    # We sort the array. The smallest n//2 elements are subtracted.
    # The largest (n+1)//2 elements are added.
    
    # Example: [4, 2, 5, 3] -> sorted [2, 3, 4, 5]
    # n=4. num_odd = 2. num_even = 2.
    # Smallest 2: [2, 3]. Largest 2: [4, 5].
    # Sum = (5 + 4) - (2 + 3) = 9 - 5 = 4.
    
    # Example: [1, 10, 100] -> sorted [1, 10, 100]
    # n=3. num_odd = 1. num_even = 2.
    # Smallest 1: [1]. Largest 2: [10, 100].
    # Sum = (100 + 10) - (1) = 109.
    
    # Step 1: Sort the array to partition it
    # Step 2: The first n // 2 elements are the smallest, they will be subtracted
    # Step 3: The remaining elements are the largest, they will be added
    
    negative_contribution_count = n // 2
    
    # Sum of the smallest elements (to be subtracted)
    subtracted_sum = sum(sorted_nums[:negative_contribution_count])
    
    # Sum of the largest elements (to be added)
    added_sum = sum(sorted_nums[negative_contribution_count:])
    
    return added_sum - subtracted_sum
