METADATA = {
    "id": 2177,
    "name": "Find Three Consecutive Integers That Sum to a Given Number",
    "slug": "find-three-consecutive-integers-that-sum-to-a-given-number",
    "category": "Array",
    "aliases": [],
    "tags": ["math", "sliding_window"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the starting index of three consecutive integers in an array that sum up to a target value.",
}

def solve(nums: list[int], target: int) -> int:
    """
    Finds the starting index of three consecutive integers that sum to the target.

    Args:
        nums: A list of integers.
        target: The target sum to find.

    Returns:
        The starting index of the triplet if found, otherwise -1.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 6)
        0
        >>> solve([1, 2, 3, 4, 5], 9)
        2
        >>> solve([1, 2, 3, 4, 5], 10)
        -1
    """
    # A triplet requires at least 3 elements
    n = len(nums)
    if n < 3:
        return -1

    # Initialize the sum of the first window of size 3
    current_window_sum = nums[0] + nums[1] + nums[2]

    # Check if the first window matches the target
    if current_window_sum == target:
        return 0

    # Slide the window across the array from index 1 to n-3
    for i in range(1, n - 2):
        # Update the window sum by subtracting the element leaving the window
        # and adding the new element entering the window
        current_window_sum = current_window_sum - nums[i - 1] + nums[i + 2]

        if current_window_sum == target:
            return i

    return -1
