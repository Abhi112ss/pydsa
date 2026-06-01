METADATA = {
    "id": 2968,
    "name": "Apply Operations to Maximize Frequency Score",
    "slug": "apply-operations-to-maximize-frequency-score",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "sorting", "prefix_sum"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Maximize the frequency score by choosing a pivot and applying operations to elements on either side.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum frequency score by choosing a pivot index and 
    applying operations to elements to make them equal to the pivot or 
    the next largest value.

    Args:
        nums: A list of integers representing the initial frequencies.
        k: The maximum total operations allowed.

    Returns:
        The maximum possible frequency score.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 2)
        4
        >>> solve([1, 1, 1, 1], 1)
        4
    """
    n = len(nums)
    if n == 0:
        return 0
    
    # Sort to allow sliding window/prefix sum approach
    nums.sort()
    
    # prefix_sums[i] stores the sum of nums[0...i-1]
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        
    # left_max[i] stores the max frequency achievable using elements from index 0 to i
    # where the pivot is nums[i]
    left_max = [0] * n
    left_ptr = 0
    for right_ptr in range(n):
        # Use sliding window to find the largest range [left_ptr, right_ptr] 
        # such that we can make all elements equal to nums[right_ptr]
        # Cost = (count * target_value) - sum_of_elements
        while (right_ptr - left_ptr + 1) * nums[right_ptr] - (prefix_sums[right_ptr + 1] - prefix_sums[left_ptr]) > k:
            left_ptr += 1
        
        current_freq = right_ptr - left_ptr + 1
        if right_ptr > 0:
            left_max[right_ptr] = max(left_max[right_ptr - 1], current_freq)
        else:
            left_max[right_ptr] = current_freq

    # right_max[i] stores the max frequency achievable using elements from index i to n-1
    # where the pivot is nums[i]
    right_max = [0] * n
    right_ptr = n - 1
    for left_ptr in range(n - 1, -1, -1):
        # Use sliding window to find the largest range [left_ptr, right_ptr]
        # such that we can make all elements equal to nums[left_ptr]
        # Cost = (count * target_value) - sum_of_elements
        while (right_ptr - left_ptr + 1) * nums[left_ptr] - (prefix_sums[right_ptr + 1] - prefix_sums[left_ptr]) > k:
            right_ptr -= 1
            
        current_freq = right_ptr - left_ptr + 1
        if left_ptr < n - 1:
            right_max[left_ptr] = max(right_max[left_ptr + 1], current_freq)
        else:
            right_max[left_ptr] = current_freq

    # The total score for a pivot at index i is:
    # (elements made equal to nums[i] from the left) + (elements made equal to nums[i] from the right) - 1
    # We subtract 1 because nums[i] is counted in both left_max and right_max
    max_score = 0
    for i in range(n):
        # left_max[i] includes the element at i, right_max[i] includes the element at i
        # To avoid double counting the pivot itself:
        l_val = left_max[i]
        r_val = right_max[i]
        
        # However, the problem asks for the sum of frequencies. 
        # If we pick nums[i] as the pivot, we can take the best configuration 
        # ending at i (from left) and the best configuration starting at i (from right).
        # Since both include index i, we subtract 1.
        max_score = max(max_score, l_val + r_val - 1)
        
    return max_score
