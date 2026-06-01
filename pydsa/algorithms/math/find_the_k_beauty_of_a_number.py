METADATA = {
    "id": 2269,
    "name": "Find the K-Beauty of a Number",
    "slug": "find_the_k_beauty_of_a_number",
    "category": "math",
    "aliases": [],
    "tags": ["math", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(log^2 n)",
    "space_complexity": "O(1)",
    "description": "Counts numbers up to num whose last k digits form a non‑zero divisor of the number.",
}


def solve(num: int, k: int) -> int:
    """Count the K‑beauty of a number.

    Args:
        num: The upper bound of the range (inclusive).
        k: The length of the suffix to consider.

    Returns:
        The count of integers i in the range [1, num] such that the integer
        formed by the last k digits of i is non‑zero and divides i.

    Examples:
        >>> solve(172, 2)
        16
        >>> solve(100000, 5)
        1
    """
    divisor = 10 ** k  # value to extract the last k digits
    count = 0

    for current in range(1, num + 1):
        suffix = current % divisor  # last k digits of current
        if suffix != 0 and current % suffix == 0:
            count += 1

    return count