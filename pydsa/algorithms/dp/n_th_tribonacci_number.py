METADATA = {
    "id": 1137,
    "name": "N-th Tribonacci Number",
    "slug": "n-th-tribonacci-number",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["recursion", "dynamic_programming", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the n-th term of the Tribonacci sequence where each term is the sum of the three preceding terms.",
}

def solve(n: int) -> int:
    """
    Calculates the n-th Tribonacci number using an iterative approach.

    The Tribonacci sequence is defined as:
    T0 = 0, T1 = 1, T2 = 1, and Tn = Tn-1 + Tn-2 + Tn-3 for n >= 3.

    Args:
        n: The index of the Tribonacci number to retrieve.

    Returns:
        The n-th Tribonacci number.

    Examples:
        >>> solve(0)
        0
        >>> solve(1)
        1
        >>> solve(4)
        2
        >>> solve(25)
        1389537
    """
    # Base cases for the first three elements of the sequence
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    # Initialize the first three terms: T0, T1, T2
    t0, t1, t2 = 0, 1, 1

    # Iterate from index 3 up to n
    for _ in range(3, n + 1):
        # The next term is the sum of the previous three
        next_term = t0 + t1 + t2
        
        # Shift the window forward: T0 becomes T1, T1 becomes T2, T2 becomes next_term
        t0, t1, t2 = t1, t2, next_term

    return t2
