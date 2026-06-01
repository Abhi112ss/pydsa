METADATA = {
    "id": 2094,
    "name": "Finding 3-Digit Even Numbers",
    "slug": "finding_3_digit_even_numbers",
    "category": "array",
    "aliases": [],
    "tags": ["math", "enumeration"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Return all distinct three‑digit even numbers that can be formed using the given digits.",
}


def solve(digits: list[int]) -> list[int]:
    """Generate all distinct three‑digit even numbers using the supplied digits.

    Args:
        digits: A list of integers where each integer is a single digit (0‑9).
                Digits may contain duplicates and each digit can be used at most
                as many times as it appears in this list.

    Returns:
        A sorted list of three‑digit even integers that can be constructed from
        the given digits without exceeding their available counts.

    Examples:
        >>> solve([2, 1, 3, 0])
        [102, 120, 130, 132, 210, 230, 302, 312]
        >>> solve([0, 2, 1, 3])
        [102, 120, 130, 132, 210, 230, 302, 312]
    """
    from collections import Counter

    digit_counts = Counter(digits)
    result: list[int] = []

    # Enumerate every three‑digit number; constant upper bound (900 checks)
    for number in range(100, 1000):
        # Skip odd numbers early
        if number % 2 != 0:
            continue

        # Extract individual digits
        hundreds = number // 100
        tens = (number // 10) % 10
        units = number % 10

        # Build a counter for the digits of the current number
        needed = Counter([hundreds, tens, units])

        # Verify that the needed digits do not exceed the available counts
        if all(needed[d] <= digit_counts.get(d, 0) for d in needed):
            result.append(number)

    return result