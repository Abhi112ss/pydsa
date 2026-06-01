METADATA = {
    "id": 3766,
    "name": "Minimum Operations to Make Binary Palindrome",
    "slug": "minimum-operations-to-make-binary-palindrome",
    "category": "String",
    "aliases": [],
    "tags": ["two_pointer", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the minimum number of character flips required to make a binary string a palindrome.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum number of operations (flips) to make a binary string a palindrome.
    
    An operation consists of changing a '0' to a '1' or a '1' to a '0'. To make a 
    string a palindrome, the character at index i must match the character at 
    index n - 1 - i.

    Args:
        s: A string consisting of '0's and '1's.

    Returns:
        The minimum number of flips required to make the string a palindrome.

    Examples:
        >>> solve("1011")
        1
        >>> solve("0000")
        0
        >>> solve("110")
        1
    """
    left_index = 0
    right_index = len(s) - 1
    mismatch_count = 0

    # Use two pointers to compare characters from both ends moving towards the center
    while left_index < right_index:
        # If characters at symmetric positions do not match, one flip is required
        if s[left_index] != s[right_index]:
            mismatch_count += 1
        
        left_index += 1
        right_index -= 1

    return mismatch_count
