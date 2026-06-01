METADATA = {
    "id": 2841,
    "name": "Maximum Sum of Almost Unique Subarray",
    "slug": "maximum-sum-of-almost-unique-subarray",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum sum of a subarray containing at most one occurrence of each element.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum sum of a subarray where each element appears at most once.

    Args:
        nums: A list of integers.

    Returns:
        The maximum sum of an 'almost unique' subarray.

    Examples:
        >>> solve([1, 2, 1, 2, 1, 3, 5, 1])
        10
        >>> solve([4, 2, 4, 5, 6])
        17
    """
    max_sum = 0
    current_sum = 0
    left = 0
    # Frequency map to track occurrences of elements in the current window
    counts = {}

    for right in range(len(nums)):
        current_val = nums[right]
        current_sum += current_val
        counts[current_val] = counts.get(current_val, 0) + 1

        # If the current element is a duplicate, shrink the window from the left
        # until the duplicate is removed.
        while counts[current_val] > 1:
            left_val = nums[left]
            current_sum -= left_val
            counts[left_val] -= 1
            # Clean up dictionary to keep space complexity optimal
            if counts[left_val] == 0:
                del counts[left_val]
            left += 1

        # Update the global maximum sum found so far
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum
