METADATA = {
    "id": 2302,
    "name": "Count Subarrays With Score Less Than K",
    "slug": "count-subarrays-with-score-less-than-k",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of contiguous subarrays where the product of the sum and the length is strictly less than k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Counts the number of contiguous subarrays where (sum of subarray * length of subarray) < k.

    Args:
        nums: A list of positive integers.
        k: The threshold value for the score.

    Returns:
        The total count of subarrays satisfying the condition.

    Examples:
        >>> solve([2, 1, 4, 3, 5], 10)
        4
        >>> solve([1, 1, 1], 1)
        0
    """
    total_count = 0
    current_sum = 0
    left_pointer = 0
    n = len(nums)

    # Use a sliding window approach with two pointers
    for right_pointer in range(n):
        current_sum += nums[right_pointer]
        
        # Calculate current score: sum * length
        # length is (right_pointer - left_pointer + 1)
        # While the score is >= k, shrink the window from the left
        while left_pointer <= right_pointer and current_sum * (right_pointer - left_pointer + 1) >= k:
            current_sum -= nums[left_pointer]
            left_pointer += 1
        
        # If the window is valid, all subarrays ending at right_pointer 
        # and starting from any index between left_pointer and right_pointer are valid.
        # The number of such subarrays is exactly the current window length.
        if current_sum * (right_pointer - left_pointer + 1) < k:
            total_count += (right_pointer - left_pointer + 1)

    return total_count
