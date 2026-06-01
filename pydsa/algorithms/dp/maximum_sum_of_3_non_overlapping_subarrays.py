METADATA = {
    "id": 689,
    "name": "Maximum Sum of 3 Non-Overlapping Subarrays",
    "slug": "maximum-sum-of-3-non-overlapping-subarrays",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "prefix_sum", "sliding_window"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find three non-overlapping subarrays of length k that yield the maximum total sum.",
}

def solve(nums: list[int], k: int) -> list[int]:
    """
    Finds the starting indices of three non-overlapping subarrays of length k 
    that maximize their total sum. If multiple solutions exist, returns the 
    lexicographically smallest one.

    Args:
        nums: A list of integers.
        k: The fixed length of each subarray.

    Returns:
        A list of three integers representing the starting indices of the subarrays.

    Examples:
        >>> solve([1, 2, 1, 2, 6, 7, 5, 1], 2)
        [0, 3, 5]
        >>> solve([1, 2, 1, 2, 1, 2, 1, 2, 1], 2)
        [0, 2, 4]
    """
    n = len(nums)
    # Calculate the sum of every possible subarray of length k
    # window_sums[i] is the sum of nums[i : i+k]
    window_sums = [0] * (n - k + 1)
    current_sum = sum(nums[:k])
    window_sums[0] = current_sum
    
    for i in range(1, n - k + 1):
        current_sum = current_sum - nums[i - 1] + nums[i + k - 1]
        window_sums[i] = current_sum

    num_windows = len(window_sums)
    
    # left_best[i] stores the starting index of the subarray with the max sum 
    # in the range [0, i]
    left_best = [0] * num_windows
    best_idx = 0
    for i in range(num_windows):
        if window_sums[i] > window_sums[best_idx]:
            best_idx = i
        left_best[i] = best_idx

    # right_best[i] stores the starting index of the subarray with the max sum 
    # in the range [i, num_windows - 1]
    right_best = [0] * num_windows
    best_idx = num_windows - 1
    for i in range(num_windows - 1, -1, -1):
        # Use >= to ensure we pick the smallest index in case of ties for the suffix
        # However, for the suffix, we want the smallest index, so if sums are equal,
        # we prefer the existing best_idx if it's smaller. 
        # Actually, iterating backwards, if window_sums[i] >= window_sums[best_idx],
        # updating best_idx to i will give the smallest index because we are moving left.
        if window_sums[i] >= window_sums[best_idx]:
            best_idx = i
        right_best[i] = best_idx

    max_total_sum = -1
    result = [0, 0, 0]

    # Iterate through all possible middle subarrays.
    # The middle subarray starts at index 'mid' and ends at 'mid + k - 1'.
    # The left subarray must end before 'mid' (index <= mid - k).
    # The right subarray must start after 'mid + k - 1' (index >= mid + k).
    for mid in range(k, num_windows - k):
        left_idx = left_best[mid - k]
        right_idx = right_best[mid + k]
        
        current_total = window_sums[left_idx] + window_sums[mid] + window_sums[right_idx]
        
        if current_total > max_total_sum:
            max_total_sum = current_total
            result = [left_idx, mid, right_idx]
            
    return result
