METADATA = {
    "id": 1281,
    "name": "Subtract the Product and Sum of Digits of an Integer",
    "slug": "subtract_the_product_and_sum_of_digits_of_an_integer",
    "category": "math",
    "aliases": [],
    "tags": ["math", "digits"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Return the difference between the product and sum of the digits of the given integer.",
}


def solve(n: int) -> int:
    """Calculate product of digits minus sum of digits.

    Args:
        n: A non‑negative integer.

    Returns:
        The value of (product of all decimal digits of n) minus (sum of those digits).

    Examples:
        >>> solve(234)
        15
        >>> solve(4421)
        21
    """
    product_of_digits = 1
    sum_of_digits = 0

    # Process each digit using modulo and integer division.
    while n > 0:
        digit = n % 10
        product_of_digits *= digit
        sum_of_digits += digit
        n //= 10

    return product_of_digits - sum_of_digits