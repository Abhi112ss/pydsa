METADATA = {
    "id": 2854,
    "name": "Rolling Average Steps",
    "slug": "rolling_average_steps",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the rolling average of a sequence using a sliding window of size k.",
}

def solve(nums: list[int], k: int) -> list[float]:
    """
    Calculates the rolling average of elements in nums using a sliding window of size k.

    Args:
        nums: A list of integers representing the sequence.
        k: The size of the sliding window.

    Returns:
        A list of floats representing the rolling averages.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 3)
        [2.0, 3.0, 4.0]
        >>> solve([10, 20, 30], 1)
        [10.0, 20.0, 30.0]
    """
    if not nums or k <= 0 or k > len(nums):
        return []

    result: list[float] = []
    current_window_sum: float = 0.0

    # Initialize the first window sum
    for i in range(k):
        current_window_sum += nums[i]
    
    # Append the first average
    result.append(current_window_sum / k)

    # Slide the window across the array
    for i in range(k, len(nums)):
        # Add the new element entering the window and subtract the one leaving
        current_window_sum += nums[i] - nums[i - k]
        result.append(current_window_sum / k)

    return result
