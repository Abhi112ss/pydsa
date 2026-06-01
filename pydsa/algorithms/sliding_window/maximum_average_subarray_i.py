METADATA = {
    "id": 643,
    "name": "Maximum Average Subarray I",
    "slug": "maximum_average_subarray_i",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum average of any subarray of length k.",
}


def solve() -> None:
    """Read input, compute the maximum average of any subarray of length k, and print it.

    Args:
        None. The function reads from standard input.

    Returns:
        None. The result is printed to standard output.

    Input Format:
        The first line contains space‑separated integers representing the array `nums`.
        The second line contains a single integer `k`, the required subarray length.

    Output Format:
        A single floating‑point number representing the maximum average, printed with
        default Python formatting.

    Example:
        >>> # Input
        >>> # 1 12 -5 -6 50 3
        >>> # 4
        >>> # Output
        >>> # 12.75
    """
    import sys

    lines = [line.strip() for line in sys.stdin if line.strip()]
    if len(lines) < 2:
        return

    # Parse the array of integers.
    nums = [int(token) for token in lines[0].split()]
    # Parse the window size.
    k = int(lines[1])

    # Initialize the sum of the first window.
    current_sum = sum(nums[:k])
    max_sum = current_sum

    # Slide the window across the array, updating the sum in O(1) per step.
    for index in range(k, len(nums)):
        current_sum += nums[index] - nums[index - k]  # add new element, remove leftmost
        if current_sum > max_sum:
            max_sum = current_sum

    # Compute the maximum average.
    max_average = max_sum / k
    print(max_average)