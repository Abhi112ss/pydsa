METADATA = {
    "id": 728,
    "name": "Self Dividing Numbers",
    "slug": "self_dividing_numbers",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n * log(max_val))",
    "space_complexity": "O(1)",
    "description": "Return all self‑dividing numbers in the interval [left, right].",
}


def solve(left: int, right: int) -> list[int]:
    """Find all self‑dividing numbers within a given inclusive range.

    Args:
        left: The lower bound of the interval (inclusive).
        right: The upper bound of the interval (inclusive).

    Returns:
        A list of integers that are self‑dividing and lie between left and right.

    Examples:
        >>> solve(1, 22)
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
        >>> solve(47, 85)
        [48, 55, 66, 77]
    """
    def is_self_dividing(number: int) -> bool:
        """Check whether a number is self‑dividing.

        A self‑dividing number is divisible by each of its digits and contains no zero digit.
        """
        temp = number
        while temp > 0:
            digit = temp % 10
            # If digit is zero or number not divisible by digit, it's not self‑dividing
            if digit == 0 or number % digit != 0:
                return False
            temp //= 10
        return True

    result: list[int] = []
    for current in range(left, right + 1):
        if is_self_dividing(current):
            result.append(current)  # add self‑dividing number to result list
    return result