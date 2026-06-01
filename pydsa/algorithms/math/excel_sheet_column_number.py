METADATA = {
    "id": 171,
    "name": "Excel Sheet Column Number",
    "slug": "excel-sheet-column-number",
    "category": "math",
    "aliases": [],
    "tags": ["math", "string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Convert an Excel column title to its corresponding column number.",
}

def solve(column_title: str) -> int:
    """
    Converts an Excel column title to its corresponding column number.

    Args:
        column_title: The column title string (e.g., "A", "AB", "ZY").

    Returns:
        The corresponding column number (e.g., 1, 28, 701).

    Examples:
        >>> solve("A")
        1
        >>> solve("AB")
        28
        >>> solve("ZY")
        701
    """
    result = 0
    # Process each character from left to right
    for char in column_title:
        # Convert character to value (A=1, B=2, ..., Z=26) and accumulate
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result