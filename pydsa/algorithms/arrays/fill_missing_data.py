METADATA = {
    "id": 2887,
    "name": "Fill Missing Data",
    "slug": "fill-missing-data",
    "category": "Data Manipulation",
    "aliases": [],
    "tags": ["pandas", "data_cleaning", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Replace all null values in a list with a specified replacement value.",
}

def solve(values: list[int | None], replacement: int) -> list[int]:
    """
    Replaces all None (null) entries in a list with a given replacement value.

    Args:
        values: A list of integers or None values.
        replacement: The integer value to use for filling missing entries.

    Returns:
        A new list where all None values have been replaced by the replacement value.

    Examples:
        >>> solve([1, None, 3, None], 0)
        [1, 0, 3, 0]
        >>> solve([None, None], -1)
        [-1, -1]
        >>> solve([1, 2, 3], 5)
        [1, 2, 3]
    """
    # Use a list comprehension to iterate through the list once.
    # If the element is None, use the replacement; otherwise, keep the original value.
    return [val if val is not None else replacement for val in values]
