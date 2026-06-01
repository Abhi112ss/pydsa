METADATA = {
    "id": 1365,
    "name": "How Many Numbers Are Smaller Than the Current Number",
    "slug": "how_many_numbers_are_smaller_than_the_current_number",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Return an array where each element is the count of numbers smaller than it in the original array.",
}


def solve(nums: list[int]) -> list[int]:
    """Return the count of numbers smaller than each element.

    Args:
        nums: List of integers.

    Returns:
        A list where the value at each index i is the number of elements
        in nums that are strictly smaller than nums[i].

    Examples:
        >>> solve([8,1,2,2,3])
        [4, 0, 1, 1, 3]
        >>> solve([6,5,4,8])
        [2, 1, 0, 3]
    """
    # Create a sorted copy of the input to determine the rank of each value.
    sorted_nums = sorted(nums)

    # Map each unique value to its first occurrence index in the sorted list.
    first_occurrence: dict[int, int] = {}
    for index, value in enumerate(sorted_nums):
        if value not in first_occurrence:
            first_occurrence[value] = index

    # Build the result using the precomputed indices.
    result: list[int] = [first_occurrence[value] for value in nums]
    return result