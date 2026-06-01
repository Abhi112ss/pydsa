METADATA = {
    "id": 2535,
    "name": "Difference Between Element Sum and Digit Sum of an Array",
    "slug": "difference_between_element_sum_and_digit_sum_of_an_array",
    "category": "math",
    "aliases": [],
    "tags": ["math", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n * log(max(nums)))",
    "space_complexity": "O(1)",
    "description": "Compute the difference between the sum of array elements and the sum of their digits.",
}


def solve(nums: list[int]) -> int:
    """Calculate the difference between the element sum and digit sum of an array.

    Args:
        nums: A list of non‑negative integers.

    Returns:
        The integer difference (element sum minus digit sum).

    Examples:
        >>> solve([1, 15, 6, 3])
        9
        >>> solve([0, 100, 23])
        80
    """
    total_element_sum = 0
    total_digit_sum = 0

    for number in nums:
        total_element_sum += number  # add the whole number to element sum

        # compute digit sum of the current number
        remaining = number
        while remaining > 0:
            total_digit_sum += remaining % 10
            remaining //= 10

    return total_element_sum - total_digit_sum