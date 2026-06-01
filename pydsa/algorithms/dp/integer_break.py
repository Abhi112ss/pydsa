METADATA = {
    "id": 343,
    "name": "Integer Break",
    "slug": "integer-break",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Break a positive integer n into the sum of at least two positive integers and maximize the product of those integers.",
}

def solve(n: int) -> int:
    """
    Maximizes the product of integers that sum up to n.

    The strategy is based on the mathematical principle that to maximize the product,
    we should use as many factors of 3 as possible. If the remainder is 1, we 
    combine it with a 3 to make 2 * 2 (since 3 * 1 < 2 * 2). If the remainder is 2,
    we simply use the 2.

    Args:
        n: The positive integer to break.

    Returns:
        The maximum product possible.

    Examples:
        >>> solve(2)
        1
        >>> solve(10)
        36
        >>> solve(5)
        6
    """
    # Base cases for n < 4 where the product is always less than n
    if n == 2:
        return 1
    if n == 3:
        return 2

    # For n >= 4, we use the greedy approach of extracting 3s.
    # We calculate how many 3s we can take.
    num_threes = n // 3
    remainder = n % 3

    # If remainder is 0, the product is 3^num_threes
    if remainder == 0:
        return 3 ** num_threes
    
    # If remainder is 1, we take (num_threes - 1) 3s and two 2s 
    # because 3 * 1 < 2 * 2.
    if remainder == 1:
        return (3 ** (num_threes - 1)) * 4
    
    # If remainder is 2, we take num_threes 3s and one 2.
    return (3 ** num_threes) * 2
