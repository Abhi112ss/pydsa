METADATA = {
    "id": 976,
    "name": "Largest Perimeter Triangle",
    "slug": "largest_perimeter_triangle",
    "category": "Math",
    "aliases": [],
    "tags": ["sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Return the largest perimeter of a triangle that can be formed from three lengths, or -1 if impossible.",
}


def solve(nums: list[int]) -> int:
    """Return the maximum perimeter of a non‑degenerate triangle.

    Args:
        nums: A list of positive integers representing side lengths.

    Returns:
        The largest possible perimeter formed by any three lengths in ``nums``.
        If no such triangle exists, returns -1.

    Examples:
        >>> solve([2, 1, 2])
        5
        >>> solve([1, 2, 1])
        -1
        >>> solve([3, 2, 3, 4])
        10
    """
    # Sort the side lengths so that we can check the largest candidates first.
    nums.sort()
    # Iterate from the largest side towards the smallest, checking each triplet.
    for index in range(len(nums) - 1, 1, -1):
        largest = nums[index]
        second_largest = nums[index - 1]
        third_largest = nums[index - 2]
        # Triangle inequality: sum of two smaller sides must exceed the largest side.
        if third_largest + second_largest > largest:
            return third_largest + second_largest + largest
    # No valid triangle found.
    return -1