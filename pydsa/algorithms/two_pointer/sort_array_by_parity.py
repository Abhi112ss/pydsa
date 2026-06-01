METADATA = {
    "id": 905,
    "name": "Sort Array By Parity",
    "slug": "sort_array_by_parity",
    "category": "Algorithms",
    "aliases": [],
    "tags": ["two_pointer", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given an integer array nums, move all even elements to the beginning followed by all odd elements.",
}

def solve(nums: list[int]) -> list[int]:
    """Sort array by parity using two pointers.

    Moves all even numbers to the front and odd numbers to the back in-place.

    Args:
        nums: List of integers to sort by parity.

    Returns:
        The modified list with evens first, then odds.

    Examples:
        >>> solve([3, 1, 2, 4])
        [4, 2, 1, 3]
        >>> solve([0])
        [0]
    """
    left = 0
    right = len(nums) - 1

    while left < right:
        # Move left pointer forward while it points to an even number
        while left < right and nums[left] % 2 == 0:
            left += 1
        # Move right pointer backward while it points to an odd number
        while left < right and nums[right] % 2 == 1:
            right -= 1
        # Swap the misplaced even (at right) and odd (at left) elements
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums