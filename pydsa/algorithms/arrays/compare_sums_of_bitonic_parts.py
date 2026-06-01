METADATA = {
    "id": 3909,
    "name": "Compare Sums of Bitonic Parts",
    "slug": "compare-sums-of-bitonic-parts",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "arrays", "bitonic"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the peak of a bitonic array and compare the sums of the increasing and decreasing parts.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the difference between the sum of the increasing part and 
    the decreasing part of a bitonic array.

    A bitonic array is an array that strictly increases to a peak and then 
    strictly decreases.

    Args:
        nums: A list of integers representing a bitonic sequence.

    Returns:
        The difference (sum_increasing - sum_decreasing).

    Examples:
        >>> solve([1, 3, 5, 4, 2])
        3  # (1+3+5) - (4+2) = 9 - 6 = 3
        >>> solve([1, 2, 3])
        6  # (1+2+3) - (0) = 6
    """
    n = len(nums)
    if n == 0:
        return 0

    # Find the peak index using binary search for O(log n) or linear scan for O(n).
    # Since we need to sum elements anyway, a linear scan is O(n) and simple.
    peak_index = 0
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            peak_index = i
        else:
            # Once the sequence stops increasing, we found the peak
            break

    # Calculate sum of the increasing part (from index 0 to peak_index inclusive)
    increasing_sum = 0
    for i in range(peak_index + 1):
        increasing_sum += nums[i]

    # Calculate sum of the decreasing part (from peak_index + 1 to end)
    decreasing_sum = 0
    for i in range(peak_index + 1, n):
        decreasing_sum += nums[i]

    return increasing_sum - decreasing_sum
