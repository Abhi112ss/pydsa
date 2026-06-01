METADATA = {
    "id": 1362,
    "name": "Closest Divisors",
    "slug": "closest_divisors",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "square_root"],
    "difficulty": "easy",
    "time_complexity": "O(sqrt(n))",
    "space_complexity": "O(1)",
    "description": "Find two divisors of a number such that their sum is minimized.",
}

def solve(n: int) -> list[int]:
    """
    Finds two divisors of n such that their sum is minimized.

    The strategy is to start searching from the square root of n downwards.
    The first divisor found will be the one closest to the square root,
    which mathematically minimizes the sum of the pair (d, n/d).

    Args:
        n: A positive integer.

    Returns:
        A list containing two integers [d1, d2] such that d1 * d2 = n 
        and d1 + d2 is minimized.

    Examples:
        >>> solve(12)
        [3, 4]
        >>> solve(1)
        [1, 1]
        >>> solve(7)
        [1, 7]
    """
    # Start searching from the integer part of the square root downwards
    # This ensures we find the pair with the smallest difference first
    start_divisor = int(n**0.5)

    for divisor in range(start_divisor, 0, -1):
        # Check if the current number is a divisor
        if n % divisor == 0:
            # The pair is (divisor, n // divisor)
            # Since we start from sqrt(n) and go down, this pair 
            # minimizes the sum because the values are closest to each other.
            return [divisor, n // divisor]

    # Fallback (mathematically, 1 will always be found)
    return [1, n]
