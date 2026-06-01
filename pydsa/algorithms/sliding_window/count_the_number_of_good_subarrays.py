METADATA = {
    "id": 2537,
    "name": "Count the Number of Good Subarrays",
    "slug": "count-the-number-of-good-subarrays",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of subarrays that contain at least k pairs of identical elements.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Counts the number of subarrays containing at least k pairs of identical elements.
    
    A pair is defined as two indices (i, j) such that i < j and nums[i] == nums[j].
    If an element appears 'count' times, it contributes count * (count - 1) // 2 pairs.

    Args:
        nums: A list of integers.
        k: The minimum number of pairs required.

    Returns:
        The total number of good subarrays.

    Examples:
        >>> solve([1, 1, 1, 1, 1], 3)
        6
        >>> solve([1, 2, 3, 1, 2, 3, 1, 2, 3], 2)
        10
    """
    if k == 0:
        # If k is 0, every single subarray is "good"
        n = len(nums)
        return n * (n + 1) // 2

    n = len(nums)
    total_good_subarrays = 0
    current_pairs = 0
    left = 0
    # Frequency map to track occurrences of elements in the current window
    counts = {}

    for right in range(n):
        # Add the new element to the window
        val = nums[right]
        # If the element was already present, adding one more increases 
        # the pair count by the current frequency of that element.
        # (e.g., if count is 2, adding a 3rd makes it 3 pairs: 2 + 1 = 3)
        current_count = counts.get(val, 0)
        current_pairs += current_count
        counts[val] = current_count + 1

        # Shrink the window from the left as long as the condition is met
        while current_pairs >= k:
            # If the window [left, right] is good, then all subarrays 
            # starting at 'left' and ending at any index from 'right' to 'n-1' are good.
            total_good_subarrays += (n - right)

            # Remove the element at 'left' and update pair count
            left_val = nums[left]
            counts[left_val] -= 1
            # Removing an element reduces the pair count by its new frequency
            current_pairs -= counts[left_val]
            left += 1

    return total_good_subarrays
