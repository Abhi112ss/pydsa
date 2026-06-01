METADATA = {
    "id": 67,
    "name": "Add Binary",
    "slug": "add-binary",
    "category": "algorithms",
    "aliases": [],
    "tags": ["string", "math", "bit_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(max(n, m))",
    "space_complexity": "O(max(n, m))",
    "description": "Given two binary strings, return their sum as a binary string.",
}

def solve(a: str, b: str) -> str:
    """
    Adds two binary strings and returns their sum as a binary string.
    
    Args:
        a: First binary string (e.g., "11")
        b: Second binary string (e.g., "1")
    
    Returns:
        Sum of the two binary strings (e.g., "100")
    
    Examples:
        >>> solve("11", "1")
        "100"
        >>> solve("1010", "1011")
        "10101"
    """
    # Initialize pointers at the end of each string and carry
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    result = []
    
    # Process digits from right to left
    while i >= 0 or j >= 0 or carry:
        # Get current digits (0 if pointer is out of bounds)
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0
        
        # Calculate sum and new carry
        total = digit_a + digit_b + carry
        carry = total // 2
        result.append(str(total % 2))
        
        # Move pointers left
        i -= 1
        j -= 1
    
    # Reverse result since we built it backwards
    return ''.join(result[::-1])