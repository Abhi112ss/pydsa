METADATA = {
    "id": 219,
    "name": "Contains Duplicate II",
    "slug": "contains_duplicate_ii",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "sliding_window"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(min(n, k))",
    "description": "Given an integer array and an integer k, return true if there are two distinct indices i and j such that nums[i] == nums[j] and abs(i - j) <= k.",
}


def solve(nums: list[int], k: int) -> bool:
    """Determine whether two equal elements exist within k distance of each other.

    Uses a sliding window hash set of size at most k + 1. As we iterate through
    the array, we maintain only the last k elements in the set. If a duplicate
    is found within the window, return True immediately.

    Args:
        nums: List of integers to check for nearby duplicates.
        k: Maximum allowed distance between two equal elements.

    Returns:
        True if there exist two distinct indices i and j such that
        nums[i] == nums[j] and abs(i - j) <= k; False otherwise.

    Examples:
        >>> solve([1, 2, 3, 1], 3)
        True
        >>> solve([1, 0, 1, 1], 1)
        True
        >>> solve([1, 2, 3, 1, 2, 3], 2)
        False
    """
    if k <= 0:
        return False

    window: set[int] = set()

    for index, value in enumerate(nums):
        # If the value is already in the window, a duplicate within distance k exists
        if value in window:
            return True

        # Add current value to the sliding window
        window.add(value)

        # Maintain window size at most k by removing the element k steps behind
        if len(window) > k:
            window.remove(nums[index - k])

    return False