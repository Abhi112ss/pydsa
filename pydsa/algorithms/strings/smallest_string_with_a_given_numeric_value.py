METADATA = {
    "id": 1663,
    "name": "Smallest String With A Given Numeric Value",
    "slug": "smallest_string_with_a_given_numeric_value",
    "category": "String",
    "aliases": [],
    "tags": ["greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return the lexicographically smallest string of length n with numeric value k.",
}


def solve(n: int, k: int) -> str:
    """Return the lexicographically smallest string of length ``n`` whose characters sum to ``k``.

    Args:
        n: Length of the desired string (1 ≤ n ≤ 10⁵).
        k: Desired total numeric value (n ≤ k ≤ 26·n).

    Returns:
        A string consisting of lowercase English letters that satisfies the constraints.

    Examples:
        >>> solve(3, 27)
        'aay'
        >>> solve(5, 73)
        'aaszz'
    """
    # Start with all 'a's; each contributes 1 to the sum.
    chars: list[str] = ["a"] * n
    remaining: int = k - n  # extra value needed beyond the baseline of all 'a's

    # Greedily distribute the remaining value from the end to keep lexicographic order minimal.
    for index in range(n - 1, -1, -1):
        if remaining == 0:
            break
        # Each position can increase by at most 25 (from 'a' to 'z').
        increase: int = min(25, remaining)
        chars[index] = chr(ord('a') + increase)
        remaining -= increase

    return "".join(chars)