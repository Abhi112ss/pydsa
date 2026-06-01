METADATA = {
    "id": 6,
    "name": "Zigzag Conversion",
    "slug": "zigzag-conversion",
    "category": "String",
    "aliases": [],
    "tags": ["string", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given a string, write it in a zigzag pattern on a given number of rows and then read it line by line.",
}

def solve(s: str, numRows: int) -> str:
    """
    Converts a string into a zigzag pattern across a specified number of rows.

    Args:
        s: The input string to be converted.
        numRows: The number of rows to use for the zigzag pattern.

    Returns:
        The string read row by row from the zigzag pattern.

    Examples:
        >>> solve("PAYPALISHIRING", 3)
        'PAHNAPLSIIGYIR'
        >>> solve("PAYPALISHIRING", 4)
        'PINALSIGYAHRPI'
        >>> solve("A", 1)
        'A'
    """
    # Edge case: If numRows is 1 or string is shorter than rows, no zigzagging is possible
    if numRows == 1 or numRows >= len(s):
        return s

    # Initialize a list of strings, one for each row
    rows: list[str] = [""] * numRows
    current_row = 0
    going_down = False

    # Iterate through each character in the string
    for char in s:
        rows[current_row] += char
        
        # If we reach the top or bottom row, reverse the direction
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        
        # Move to the next row based on current direction
        current_row += 1 if going_down else -1

    # Concatenate all rows to form the final result
    return "".join(rows)
