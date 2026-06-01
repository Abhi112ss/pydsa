METADATA = {
    "id": 283,
    "name": "Move Zeroes",
    "slug": "move_zeroes",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "array_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.",
}

def solve(nums: list[int]) -> None:
    """
    Moves all zeros in the list to the end while maintaining the relative order of non-zero elements.

    Args:
        nums: A list of integers to be modified in-place.

    Returns:
        None
    """
    last_non_zero_index = 0

    for current_index in range(len(nums)):
        if nums[current_index] != 0:
            nums[last_non_zero_index], nums[current_index] = nums[current_index], nums[last_non_zero_index]
            last_non_zero_index += 1