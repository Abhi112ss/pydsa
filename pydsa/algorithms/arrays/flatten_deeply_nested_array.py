METADATA = {
    "id": 2625,
    "name": "Flatten Deeply Nested Array",
    "slug": "flatten_deeply_nested_array",
    "category": "array",
    "aliases": [],
    "tags": ["recursion", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Flatten a nested list of integers into a single list.",
}


def solve() -> None:
    """
    Reads a nested list from standard input, flattens it, and prints the result.

    Args:
        None (input is read from stdin).

    Returns:
        None (the flattened list is printed to stdout).

    Example:
        Input:
            [1, [2, [3, 4], 5], 6]
        Output:
            [1, 2, 3, 4, 5, 6]
    """
    import sys
    import ast

    input_line: str = sys.stdin.readline().strip()
    if not input_line:
        print("[]")
        return

    # Parse the input string into a Python list; ast.literal_eval safely evaluates literals.
    nested_list: list = ast.literal_eval(input_line)

    flattened_result: list[int] = []

    def _flatten(item: object) -> None:
        """Recursively appends integers from nested structures to flattened_result."""
        if isinstance(item, list):
            # If the current item is a list, recurse into each element.
            for sub_item in item:
                _flatten(sub_item)
        else:
            # Base case: item is an integer (or any non-list element to be kept).
            flattened_result.append(item)  # type: ignore[arg-type]

    _flatten(nested_list)

    print(flattened_result)