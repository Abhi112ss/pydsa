METADATA = {
    "id": 2295,
    "name": "Replace Elements in an Array",
    "slug": "replace_elements_in_an_array",
    "category": "Array",
    "aliases": [],
    "tags": ["array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Replace each element with the greatest element to its right and set the last element to -1.",
}


def solve(nums: list[int]) -> list[int]:
    """Replace each element in the array with the greatest element among those to its right.

    Args:
        nums: List of integers.

    Returns:
        A new list where each element is replaced by the maximum value to its right,
        and the last element is set to -1.

    Examples:
        >>> solve([17,18,5,4,6,1])
        [18,6,6,6,1,-1]
        >>> solve([400])
        [-1]
    """
    # Initialize the running maximum as -1 because the last element should become -1.
    running_max = -1
    # Iterate from right to left, updating each element in place.
    for index in range(len(nums) - 1, -1, -1):
        original_value = nums[index]
        nums[index] = running_max          # Replace current element with the max seen so far.
        if original_value > running_max:   # Update running_max if the original value is larger.
            running_max = original_value
    return nums