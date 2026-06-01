METADATA = {
    "id": 1703,
    "name": "Minimum Adjacent Swaps for K Consecutive Ones",
    "slug": "minimum-adjacent-swaps-for-k-consecutive-ones",
    "category": "Greedy",
    "aliases": [],
    "tags": ["sliding_window", "greedy", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of adjacent swaps to group k consecutive ones together.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the minimum number of adjacent swaps to make k consecutive ones.

    The problem is equivalent to finding a window of k indices of '1's such that
    the cost to move them to a contiguous block centered around their median 
    is minimized.

    Args:
        nums: A list of integers containing only 0s and 1s.
        k: The number of consecutive ones required.

    Returns:
        The minimum number of adjacent swaps required.

    Examples:
        >>> solve([1, 0, 0, 1, 0, 0, 1], 3)
        4
        >>> solve([1, 1, 1, 1, 1], 3)
        0
    """
    # Extract the indices of all positions where nums[i] is 1
    one_indices = [i for i, val in enumerate(nums) if val == 1]
    n = len(one_indices)
    
    # If we need k ones and we have exactly k, or k is 1, no swaps needed
    if k <= 1:
        return 0

    # To handle the 'consecutive' requirement, we transform the indices.
    # If we want to move indices [p1, p2, p3] to be consecutive, say [x, x+1, x+2],
    # the cost is sum(|pi - (x + i)|).
    # This is equivalent to sum(|(pi - i) - x|).
    # This transforms the problem into finding the median of the modified indices.
    modified_indices = [one_indices[i] - i for i in range(n)]
    
    # Precompute prefix sums of modified_indices to calculate window sums in O(1)
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + modified_indices[i]
        
    min_swaps = float('inf')
    
    # Use a sliding window of size k over the modified_indices
    for i in range(n - k + 1):
        # The window of k indices is from index i to i + k - 1
        left = i
        right = i + k - 1
        mid = (left + right) // 2
        
        # The optimal 'x' (the target starting position in modified space) 
        # is the median of the current window.
        median_val = modified_indices[mid]
        
        # Calculate sum of absolute differences:
        # Sum_{j=left}^{right} |modified_indices[j] - median_val|
        # Split into two parts: elements <= median and elements > median
        
        # Part 1: Elements from left to mid (all <= median_val)
        # Sum = (median_val * count) - sum(elements)
        left_count = mid - left + 1
        left_sum = prefix_sums[mid + 1] - prefix_sums[left]
        cost_left = (median_val * left_count) - left_sum
        
        # Part 2: Elements from mid + 1 to right (all >= median_val)
        # Sum = sum(elements) - (median_val * count)
        right_count = right - mid
        right_sum = prefix_sums[right + 1] - prefix_sums[mid + 1]
        cost_right = right_sum - (median_val * right_count)
        
        current_swaps = cost_left + cost_right
        if current_swaps < min_swaps:
            min_swaps = current_swaps
            
    return int(min_swaps)
