METADATA = {
    "id": 2310,
    "name": "Sum of Numbers With Units Digit K",
    "slug": "sum_of_numbers_with_units_digit_k",
    "category": "array",
    "aliases": [],
    "tags": ["math", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the sum of numbers whose units digit equals k.",
}


def solve(nums: list[int], k: int) -> int:
    """Calculate the sum of all numbers in ``nums`` whose units digit equals ``k``.

    Args:
        nums: List of integers to be examined.
        k: Target units digit (0 <= k <= 9).

    Returns:
        The sum of all integers in ``nums`` whose last digit is ``k``.
        If no such numbers exist, returns 0.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 3)
        3
        >>> solve([12, 23, 34, 45, 56], 2)
        12
        >>> solve([10, 20, 30], 5)
        0
    """
    total_sum = 0
    for number in nums:
        # Check if the units digit of the current number matches k
        if number % 10 == k:
            total_sum += number
    return total_sum