METADATA = {
    "id": 1716,
    "name": "Calculate Money in Leetcode Bank",
    "slug": "calculate_money_in_leetcode_bank",
    "category": "math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate total money received after n days with weekly incremental pattern.",
}


def solve(n: int) -> int:
    """Calculate the total amount of money received after ``n`` days.

    Args:
        n: The number of days (1-indexed) for which money is accumulated.

    Returns:
        The total sum of money received over ``n`` days.

    Examples:
        >>> solve(4)
        10
        >>> solve(10)
        37
        >>> solve(1)
        1
    """
    # Number of complete weeks (each week has 7 days)
    full_weeks: int = n // 7
    # Remaining days after the last complete week
    remaining_days: int = n % 7

    # Sum of money for all complete weeks:
    #   week i (0‑based) contributes 7*i + 28 dollars.
    #   Use arithmetic series formula for Σ i.
    weeks_sum: int = 7 * full_weeks * (full_weeks - 1) // 2 + 28 * full_weeks

    # Sum of money for the remaining days:
    #   each remaining day adds full_weeks dollars plus its position (1‑based).
    remaining_sum: int = remaining_days * full_weeks + remaining_days * (remaining_days + 1) // 2

    return weeks_sum + remaining_sum