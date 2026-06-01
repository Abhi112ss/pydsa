METADATA = {
    "id": 2648,
    "name": "Generate Fibonacci Sequence",
    "slug": "generate_fibonacci_sequence",
    "category": "math",
    "aliases": [],
    "tags": ["math", "dynamic_programming", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Generate a list containing the first n terms of the Fibonacci sequence.",
}

def solve(n: int) -> list[int]:
    """
    Generates the first n terms of the Fibonacci sequence.

    The Fibonacci sequence is defined as:
    F(0) = 0, F(1) = 1, and F(i) = F(i-1) + F(i-2) for i > 1.

    Args:
        n: The number of terms to generate.

    Returns:
        A list of integers representing the first n terms of the Fibonacci sequence.
        If n <= 0, returns an empty list.

    Examples:
        >>> solve(0)
        []
        >>> solve(1)
        [0]
        >>> solve(5)
        [0, 1, 1, 2, 3]
        >>> solve(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]

    # Initialize the sequence with the first two base cases
    fibonacci_sequence = [0, 1]

    # Iteratively build the sequence up to n terms
    # Each new term is the sum of the previous two terms
    for i in range(2, n):
        next_term = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence
