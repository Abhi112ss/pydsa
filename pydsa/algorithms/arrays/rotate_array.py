METADATA = {
    "id": 189,
    "name": "Rotate Array",
    "slug": "rotate_array",
    "category": "Algorithms",
    "aliases": ["Rotate Array"],
    "tags": ["array", "two_pointers", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Rotates an array to the right by k steps using in-place reversals.",
}


def solve(nums: list[int], k: int) -> None:
    """
    Rotates the input array in-place to the right by k steps.

    Args:
        nums: The list of integers to rotate.
        k: The number of steps to rotate to the right.

    Returns:
        None: Modifies nums in-place.

    Examples:
        >>> arr = [1, 2, 3, 4, 5, 6, 7]
        >>> solve(arr, 3)
        >>> arr
        [5, 6, 7, 1, 2, 3, 4]
    """
    if not nums:
        return

    n = len(nums)
    # Normalize k in case k > n
    k %= n
    if k == 0:
        return

    def reverse_subrange(start: int, end: int) -> None:
        """Helper to reverse elements in nums from start to end inclusive."""
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse the entire array
    # [1, 2, 3, 4, 5, 6, 7] -> [7, 6, 5, 4, 3, 2, 1]
    reverse_subrange(0, n - 1)

    # Step 2: Reverse the first k elements
    # [7, 6, 5, 4, 3, 2, 1] -> [5, 6, 7, 4, 3, 2, 1]
    reverse_subrange(0, k - 1)

    # Step 3: Reverse the remaining n-k elements
    # [5, 6, 7, 4, 3, 2, 1] -> [5, 6, 7, 1, 2, 3, 4]
    reverse_subrange(k, n - 1)