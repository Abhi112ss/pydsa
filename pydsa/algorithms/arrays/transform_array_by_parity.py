METADATA = {
    "id": 3467,
    "name": "Transform Array by Parity",
    "slug": "transform_array_by_parity",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Rearrange the elements of an array such that all even numbers appear before all odd numbers.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Rearranges the array in-place so that all even integers come before all odd integers.

    Args:
        nums: A list of integers to be transformed.

    Returns:
        The transformed list where even numbers precede odd numbers.

    Examples:
        >>> solve([3, 1, 2, 4])
        [2, 4, 3, 1]
        >>> solve([1, 2, 3, 4, 5, 6])
        [2, 4, 6, 1, 3, 5]
    """
    left_pointer = 0
    right_pointer = len(nums) - 1

    # Use a two-pointer approach to partition the array
    while left_pointer < right_pointer:
        # Increment left pointer if the current element is already even
        if nums[left_pointer] % 2 == 0:
            left_pointer += 1
        # Decrement right pointer if the current element is already odd
        elif nums[right_pointer] % 2 != 0:
            right_pointer -= 1
        # If left is odd and right is even, swap them
        else:
            nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
            left_pointer += 1
            right_pointer -= 1

    return nums
