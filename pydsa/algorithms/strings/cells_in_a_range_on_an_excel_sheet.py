METADATA = {
    "id": 2194,
    "name": "Cells in a Range on an Excel Sheet",
    "slug": "cells-in-a-range-on-an-excel-sheet",
    "category": "String",
    "aliases": [],
    "tags": ["string", "math"],
    "difficulty": "easy",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Given two Excel cell addresses, return all cells in the range between them in lexicographical order.",
}

def solve(start: str, end: str) -> list[str]:
    """
    Returns all cells in the range between start and end in lexicographical order.

    Args:
        start: The starting cell address (e.g., "A1").
        end: The ending cell address (e.g., "B2").

    Returns:
        A list of strings representing all cells in the range.

    Examples:
        >>> solve("A1", "A3")
        ['A1', 'A2', 'A3']
        >>> solve("A1", "B2")
        ['A1', 'A2', 'B1', 'B2']
    """
    # Helper to split column letters and row numbers
    def parse_cell(cell: str) -> tuple[str, int]:
        column_part = ""
        row_part = ""
        for char in cell:
            if char.isalpha():
                column_part += char
            else:
                row_part += char
        return column_part, int(row_part)

    start_col, start_row = parse_cell(start)
    end_col, end_row = parse_cell(end)

    # Convert column letters to numbers (A=1, B=2, etc.) to facilitate iteration
    def col_to_int(col_str: str) -> int:
        num = 0
        for char in col_str:
            num = num * 26 + (ord(char) - ord('A') + 1)
        return num

    # Convert column numbers back to letters
    def int_to_col(n: int) -> str:
        result = []
        while n > 0:
            n, remainder = divmod(n - 1, 26)
            result.append(chr(ord('A') + remainder))
        return "".join(reversed(result))

    start_col_val = col_to_int(start_col)
    end_col_val = col_to_int(end_col)

    result = []
    
    # Iterate through columns first, then rows, to maintain lexicographical order
    # Lexicographical order for Excel cells: A1, A2, B1, B2...
    # This means we iterate through columns in the outer loop and rows in the inner loop
    for col_val in range(start_col_val, end_col_val + 1):
        current_col_str = int_to_col(col_val)
        for row_val in range(start_row, end_row + 1):
            result.append(f"{current_col_str}{row_val}")

    return result
