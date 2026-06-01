METADATA = {
    "id": 628,
    "name": "Maximum Product of Three Numbers",
    "slug": "maximum_product_of_three_numbers",
    "category": "array",
    "aliases": [],
    "tags": ["greedy", "math", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum product of any three numbers in an integer array.",
}


def solve(nums: list[int]) -> int:
    """Return the maximum product of any three numbers in the given list.

    Args:
        nums: A list of integers with length at least three.

    Returns:
        The largest possible product of three distinct elements from ``nums``.

    Examples:
        >>> solve([1, 2, 3])
        6
        >>> solve([1, -4, 3, -6, 7, 0])
        168
        >>> solve([-10, -10, 5, 2])
        500
    """
    import math

    # Initialize three largest values to negative infinity
    max1 = max2 = max3 = -math.inf
    # Initialize two smallest values to positive infinity
    min1 = min2 = math.inf

    for value in nums:
        # Update the three largest values
        if value > max1:
            max3 = max2
            max2 = max1
            max1 = value
        elif value > max2:
            max3 = max2
            max2 = value
        elif value > max3:
            max3 = value

        # Update the two smallest values
        if value < min1:
            min2 = min1
            min1 = value
        elif value < min2:
            min2 = value

    # The maximum product is either the product of the three largest numbers
    # or the product of the two smallest (most negative) numbers with the largest.
    product_using_largest = max1 * max2 * max3
    product_using_smallest = max1 * min1 * min2
    return max(product_using_largest, product_using_smallest)