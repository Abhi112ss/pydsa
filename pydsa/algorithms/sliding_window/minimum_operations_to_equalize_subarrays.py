METADATA = {
    "id": 3762,
    "name": "Minimum Operations to Equalize Subarrays",
    "slug": "minimum_operations_to_equalize_subarrays",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "prefix_sum", "frequency_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum operations to make all elements in a subarray equal by choosing a window size and an element value.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the minimum operations to make all elements in a subarray of length k equal.
    
    An operation consists of changing an element to any other value. To minimize 
    operations for a fixed window, we should change all elements to the most 
    frequent element currently in that window.

    Args:
        nums: A list of integers representing the array.
        k: The required length of the subarray.

    Returns:
        The minimum number of operations required.

    Examples:
        >>> solve([1, 2, 1, 3, 3, 3], 3)
        0
        >>> solve([1, 2, 3, 4, 5], 3)
        2
    """
    n = len(nums)
    if k <= 1:
        return 0

    # Since the problem implies a fixed window size k, we slide a window of size k.
    # To minimize operations, we maximize the frequency of the most frequent element.
    # Operations = k - max_frequency_in_window.
    
    # Note: The problem constraints/description usually imply elements are within a 
    # specific range. If elements are arbitrary, we use a hash map. 
    # If elements are small, we use a frequency array.
    # Given the O(1) space requirement in the prompt, we assume a bounded range 
    # or a fixed number of distinct elements.
    
    counts: dict[int, int] = {}
    max_freq = 0
    min_ops = k  # Initialize with worst case (all elements different)

    # Initialize the first window of size k
    for i in range(k):
        val = nums[i]
        counts[val] = counts.get(val, 0) + 1
        if counts[val] > max_freq:
            max_freq = counts[val]

    min_ops = k - max_freq

    # Slide the window from index k to n-1
    for i in range(k, n):
        # Element entering the window
        new_val = nums[i]
        counts[new_val] = counts.get(new_val, 0) + 1
        
        # Element leaving the window
        old_val = nums[i - k]
        counts[old_val] -= 1
        
        # Note: In a standard sliding window for max frequency, 
        # we don't easily decrement max_freq when an element leaves.
        # However, for a fixed window size k, we can re-calculate or 
        # use a frequency-of-frequencies approach to keep it O(1) per step.
        
        # Re-calculating max_freq for the current window. 
        # To keep this O(n) total, we use a frequency-of-frequencies map.
        # But for simplicity and given the prompt's hint, we track the max.
        # Let's implement the frequency-of-frequencies to ensure O(n).
        pass

    # Re-implementing with frequency-of-frequencies for true O(n)
    return _solve_optimized(nums, k)

def _solve_optimized(nums: list[int], k: int) -> int:
    """
    Optimized sliding window using frequency-of-frequencies to maintain max_freq in O(1).
    """
    n = len(nums)
    if k <= 1:
        return 0

    counts: dict[int, int] = {}  # val -> frequency
    freq_counts: dict[int, int] = {}  # frequency -> how many values have this frequency
    max_freq = 0

    def add(val: int):
        nonlocal max_freq
        old_f = counts.get(val, 0)
        new_f = old_f + 1
        counts[val] = new_f
        
        # Update frequency of frequencies
        if old_f > 0:
            freq_counts[old_f] -= 1
        freq_counts[new_f] = freq_counts.get(new_f, 0) + 1
        
        if new_f > max_freq:
            max_freq = new_f

    def remove(val: int):
        nonlocal max_freq
        old_f = counts[val]
        new_f = old_f - 1
        counts[val] = new_f
        
        # Update frequency of frequencies
        freq_counts[old_f] -= 1
        if new_f > 0:
            freq_counts[new_f] = freq_counts.get(new_f, 0) + 1
            
        # If the current max_freq has no more elements, decrement max_freq
        if freq_counts[max_freq] == 0:
            max_freq -= 1

    # Initial window
    for i in range(k):
        add(nums[i])
    
    min_ops = k - max_freq

    # Sliding
    for i in range(k, n):
        add(nums[i])
        remove(nums[i - k])
        min_ops = min(min_ops, k - max_freq)

    return min_ops
