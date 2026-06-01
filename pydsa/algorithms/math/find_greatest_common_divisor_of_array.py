METADATA = {
    "id": 1979,
    "name": "Find Greatest Common Divisor of Array",
    "slug": "find_greatest_common_divisor_of_array",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(n log(max_val))",
    "space_complexity": "O(1)",
    "description": "Return the greatest common divisor of the minimum and maximum numbers in the array.",
}


def solve(nums: list[int]) -> int:
    """Compute the greatest common divisor (GCD) of the smallest and largest values in an array.

    Args:
        nums: A list of positive integers.

    Returns:
        The GCD of the minimum and maximum elements in ``nums``.

    Examples:
        >>> solve([2, 5, 6, 9, 10])
        2
        >>> solve([7, 5, 6, 8, 3])
        1
    """
    # Find the minimum and maximum values in a single pass.
    minimum_value = nums[0]
    maximum_value = nums[0]
    for number in nums[1:]:
        if number < minimum_value:
            minimum_value = number
        elif number > maximum_value:
            maximum_value = number

    # Compute GCD using Euclidean algorithm (via math.gcd for clarity).
    import math

    return math.gcd(minimum_value, maximum_value)