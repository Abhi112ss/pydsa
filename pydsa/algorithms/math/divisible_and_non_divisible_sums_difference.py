METADATA = {
    "id": 2894,
    "name": "Divisible and Non-divisible Sums Difference",
    "slug": "divisible-and-non-divisible-sums-difference",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the absolute difference between the sum of elements divisible by a number 'num' and the sum of elements not divisible by it.",
}

def solve(nums: list[int], num: int) -> int:
    """
    Calculates the absolute difference between the sum of elements divisible by 'num'
    and the sum of elements not divisible by 'num'.

    Args:
        nums: A list of integers.
        num: The divisor used to check divisibility.

    Returns:
        The absolute difference between the two sums.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 2)
        3
        >>> solve([1, 3, 6, 8, 10], 3)
        14
    """
    divisible_sum = 0
    non_divisible_sum = 0

    for value in nums:
        # Check if the current element is divisible by the given number
        if value % num == 0:
            divisible_sum += value
        else:
            non_divisible_sum += value

    # Return the absolute difference as required by the problem
    return abs(divisible_sum - non_divisible_sum)
