METADATA = {
    "id": 1433,
    "name": "Check If a String Can Break Another String",
    "slug": "check-if-a-string-can-break-another-string",
    "category": "String",
    "aliases": [],
    "tags": ["sorting", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Determine if one string can completely break another string by checking if its sorted characters are consistently greater than or equal to the other's sorted characters.",
}

def solve(x: str, y: str) -> bool:
    """
    Checks if string x can break string y or if string y can break string x.
    
    A string x breaks string y if, after sorting both, every character in x 
    is greater than or equal to the corresponding character in y.

    Args:
        x: The first input string.
        y: The second input string.

    Returns:
        True if x breaks y or y breaks x, False otherwise.

    Examples:
        >>> solve("abc", "aaa")
        True
        >>> solve("abc", "def")
        True
        >>> solve("abc", "abd")
        False
    """
    # Convert strings to sorted lists of characters to allow element-wise comparison
    sorted_x = sorted(list(x))
    sorted_y = sorted(list(y))
    
    n = len(sorted_x)
    
    # Flags to track if x breaks y or y breaks x
    x_breaks_y = True
    y_breaks_x = True
    
    for i in range(n):
        # If at any point x[i] < y[i], x cannot break y
        if sorted_x[i] < sorted_y[i]:
            x_breaks_y = False
        
        # If at any point y[i] < x[i], y cannot break x
        if sorted_y[i] < sorted_x[i]:
            y_breaks_x = False
            
        # Optimization: if neither can break the other, exit early
        if not x_breaks_y and not y_breaks_x:
            return False
            
    return x_breaks_y or y_breaks_x
