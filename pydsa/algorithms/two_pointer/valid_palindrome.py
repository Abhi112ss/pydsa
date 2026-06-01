METADATA = {
    "id": 125,
    "name": "Valid Palindrome",
    "slug": "valid-palindrome",
    "category": "String",
    "aliases": [],
    "tags": ["two_pointer", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a string is a palindrome, considering only alphanumeric characters and ignoring cases.",
}

def solve(s: str) -> bool:
    """
    Determines if a string is a palindrome after converting all uppercase letters 
    into lowercase letters and removing all non-alphanumeric characters.

    Args:
        s: The input string to check.

    Returns:
        True if the string is a palindrome, False otherwise.

    Examples:
        >>> solve("A man, a plan, a canal: Panama")
        True
        >>> solve("race a car")
        False
        >>> solve(" ")
        True
    """
    left_index = 0
    right_index = len(s) - 1

    while left_index < right_index:
        # Move left pointer forward if current character is not alphanumeric
        while left_index < right_index and not s[left_index].isalnum():
            left_index += 1
        
        # Move right pointer backward if current character is not alphanumeric
        while left_index < right_index and not s[right_index].isalnum():
            right_index -= 1

        # Compare characters in a case-insensitive manner
        if s[left_index].lower() != s[right_index].lower():
            return False
        
        left_index += 1
        right_index -= 1

    return True
