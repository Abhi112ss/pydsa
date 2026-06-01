METADATA = {
    "id": 3261,
    "name": "Count Substrings That Satisfy K-Constraint II",
    "slug": "count-substrings-that-satisfy-k-constraint-ii",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "two_pointer"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of substrings where the number of characters with frequency greater than k is at most k.",
}

def solve(numbers: list[int], k: int) -> int:
    """
    Counts the number of substrings where the number of elements with frequency 
    greater than k is at most k.

    Args:
        numbers: A list of integers representing the sequence.
        k: The threshold for frequency and the maximum allowed number of 
           elements exceeding that threshold.

    Returns:
        The total count of valid substrings.

    Examples:
        >>> solve([1, 1, 2, 2, 2], 1)
        6
        # Valid substrings: [1], [1], [2], [2], [2], [1, 1] is invalid (1 occurs twice > 1)
        # Wait, the constraint is: count of elements with freq > k is <= k.
        # In [1, 1, 2, 2, 2] with k=1:
        # [1]: freq(1)=1 <= 1. Count of elements with freq > 1 is 0. 0 <= 1. OK.
        # [1, 1]: freq(1)=2 > 1. Count of elements with freq > 1 is 1. 1 <= 1. OK.
        # [1, 1, 2]: freq(1)=2, freq(2)=1. Count of elements with freq > 1 is 1. 1 <= 1. OK.
        # [1, 1, 2, 2]: freq(1)=2, freq(2)=2. Count of elements with freq > 1 is 2. 2 > 1. NOT OK.
    """
    n = len(numbers)
    counts = {}
    # bad_elements_count tracks how many distinct numbers currently have frequency > k
    bad_elements_count = 0
    left = 0
    total_substrings = 0

    for right in range(n):
        num = numbers[right]
        counts[num] = counts.get(num, 0) + 1
        
        # If this number just crossed the threshold k, increment bad_elements_count
        if counts[num] == k + 1:
            bad_elements_count += 1
            
        # If we have more than k elements violating the constraint, shrink the window
        while bad_elements_count > k:
            left_num = numbers[left]
            # If this number was a 'bad' element and is about to drop below threshold
            if counts[left_num] == k + 1:
                bad_elements_count -= 1
            
            counts[left_num] -= 1
            left += 1
            
        # All substrings ending at 'right' and starting from any index in [left, right] are valid
        # The number of such substrings is the length of the current window
        total_substrings += (right - left + 1)

    return total_substrings
