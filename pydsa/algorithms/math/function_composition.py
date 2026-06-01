METADATA = {
    "id": 2629,
    "name": "Function Composition",
    "slug": "function_composition",
    "category": "math",
    "aliases": [],
    "tags": ["functional_programming"],
    "difficulty": "easy",
    "time_complexity": "O(k)",
    "space_complexity": "O(1)",
    "description": "Apply a list of linear functions to an input value in reverse order.",
}


def solve(functions: list[list[int]], x: int) -> int:
    """Apply a sequence of linear functions to an integer.

    Each function is represented as [a, b] meaning f(x) = a * x + b.
    The functions are applied from right to left (i.e., the last function
    in the list is applied first).

    Args:
        functions: A list of [a, b] pairs defining the functions.
        x: The initial integer input.

    Returns:
        The integer result after applying all functions.

    Examples:
        >>> solve([[2, 3], [4, 5]], 1)
        13
        # Explanation: Apply f1(x)=4*x+5 first: 4*1+5=9, then f0(x)=2*x+3: 2*9+3=21

        >>> solve([[1, 2], [3, 4], [5, 6]], 0)
        20
        # Apply functions in reverse: f2(0)=6, f1(6)=22, f0(22)=24
    """
    # Iterate over the functions in reverse order, updating the input value.
    for coefficient, constant in reversed(functions):
        x = coefficient * x + constant  # apply current linear function
    return x