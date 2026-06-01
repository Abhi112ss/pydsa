METADATA = {
    "id": 1304,
    "name": "Find N Unique Integers Sum up to Zero",
    "slug": "find-n-unique-integers-sum-up-to-zero",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Construct an array of n unique integers such that their sum is equal to zero.",
}

def solve(n: int) -> list[int]:
    """
    Constructs an array of n unique integers that sum up to zero.

    The strategy is to pick symmetric pairs (i, -i) for as many pairs as possible.
    If n is odd, we include 0 in the set to maintain the zero sum and uniqueness.

    Args:
        n: The number of unique integers required.

    Returns:
        A list of n unique integers that sum to zero.

    Examples:
        >>> solve(5)
        [-2, -1, 0, 1, 2]
        >>> solve(4)
        [-2, -1, 1, 2]
    """
    result: list[int] = []

    # If n is odd, adding 0 allows us to use symmetric pairs for the remaining n-1 elements
    if n % 2 != 0:
        result.append(0)

    # Generate pairs of (i, -i) until we reach n elements
    # We iterate up to n // 2 to get the required number of pairs
    for i in range(1, (n // 2) + 1):
        result.append(i)
        result.append(-i)

    return result
