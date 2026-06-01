METADATA = {
    "id": 922,
    "name": "Sort Array By Parity II",
    "slug": "sort-array-by-parity-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Rearrange the array such that even indices contain even numbers and odd indices contain odd numbers.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Args:
        nums: A list of integers.

    Returns:
        A list of integers where even indices have even numbers and odd indices have odd numbers.
    """
    even_pointer = 0
    odd_pointer = 1
    array_length = len(nums)

    while even_pointer < array_length and odd_pointer < array_length:
        if nums[even_pointer] % 2 == 0:
            even_pointer += 2
        elif nums[odd_pointer] % 2 != 0:
            odd_pointer += 2
        else:
            nums[even_pointer], nums[odd_pointer] = nums[odd_pointer], nums[even_pointer]
            even_pointer += 2
            odd_pointer += 2

    return nums