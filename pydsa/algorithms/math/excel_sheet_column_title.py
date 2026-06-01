METADATA = {
    "id": 168,
    "name": "Excel Sheet Column Title",
    "slug": "excel-sheet-column-title",
    "category": "math",
    "aliases": ["convert-to-title"],
    "tags": ["math", "string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Convert an integer to its corresponding Excel column title.",
}

def solve(column_number: int) -> str:
    """
    Converts an integer to its corresponding Excel column title.
    
    Args:
        column_number: Integer representing the column number (1-indexed).
        
    Returns:
        String representing the Excel column title.
        
    Examples:
        >>> solve(1)
        'A'
        >>> solve(28)
        'AB'
        >>> solve(701)
        'ZY'
    """
    result = ""
    while column_number > 0:
        # Convert to 0-based index: A=0, B=1, ..., Z=25
        column_number -= 1
        # Calculate current character and prepend to result
        result = chr(ord('A') + column_number % 26) + result
        # Move to next higher digit
        column_number //= 26
    return result