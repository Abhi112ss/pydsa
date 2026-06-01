METADATA = {
    "id": 2011,
    "name": "Final Value of Variable After Performing Operations",
    "slug": "final_value_of_variable_after_performing_operations",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Simulate increment/decrement operations on a variable and return its final value.",
}


def solve(operations: list[str]) -> int:
    """Simulate the effect of a sequence of increment/decrement operations.

    Args:
        operations: A list of strings, each being one of "++X", "X++", "--X", or "X--".

    Returns:
        The integer value of the variable after performing all operations,
        starting from an initial value of 0.

    Examples:
        >>> solve(["++X", "X++", "--X"])
        1
        >>> solve(["X--", "X--", "X++"])
        -1
    """
    variable_value: int = 0

    for operation in operations:
        # The second character determines whether the operation is an increment or decrement.
        if operation[1] == '+':
            variable_value += 1
        else:
            variable_value -= 1

    return variable_value