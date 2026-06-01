METADATA = {
    "id": 3463,
    "name": "Check If Digits Are Equal in String After Operations II",
    "slug": "check-if-digits-are-equal-in-string-after-operations-ii",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if two strings result in the same sequence of digits after applying specific character transformation rules.",
}

def solve(s1: str, s2: str) -> bool:
    """
    Checks if the sequence of digits in s1 and s2 are identical after 
    applying the transformation rules.

    The transformation rule: A character is considered a 'digit' if it is 
    already a digit or if it can be transformed into one via specific operations.
    In this specific problem context, we extract all digits from both strings 
    and compare the resulting sequences.

    Args:
        s1: The first input string.
        s2: The second input string.

    Returns:
        True if the extracted digit sequences are equal, False otherwise.

    Examples:
        >>> solve("a1b2c", "12")
        True
        >>> solve("123", "12")
        False
    """
    n1 = len(s1)
    n2 = len(s2)
    
    ptr1 = 0
    ptr2 = 0
    
    # We use a two-pointer approach to traverse both strings simultaneously.
    # This avoids the O(n) space overhead of creating new strings/lists.
    while ptr1 < n1 and ptr2 < n2:
        # Advance ptr1 until we find a digit in s1
        while ptr1 < n1 and not s1[ptr1].isdigit():
            ptr1 += 1
            
        # Advance ptr2 until we find a digit in s2
        while ptr2 < n2 and not s2[ptr2].isdigit():
            ptr2 += 1
            
        # If both pointers are still within bounds, compare the digits found
        if ptr1 < n1 and ptr2 < n2:
            if s1[ptr1] != s2[ptr2]:
                return False
            ptr1 += 1
            ptr2 += 1
            
    # After the main loop, we must ensure no remaining digits exist in either string.
    # Skip any remaining non-digit characters in s1.
    while ptr1 < n1 and not s1[ptr1].isdigit():
        ptr1 += 1
        
    # Skip any remaining non-digit characters in s2.
    while ptr2 < n2 and not s2[ptr2].isdigit():
        ptr2 += 1
        
    # If both pointers reached the end of their respective strings, 
    # it means no extra digits were found.
    return ptr1 == n1 and ptr2 == n2