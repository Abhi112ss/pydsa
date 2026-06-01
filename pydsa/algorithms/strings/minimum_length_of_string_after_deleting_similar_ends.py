METADATA = {
    "id": 1750,
    "name": "Minimum Length of String After Deleting Similar Ends",
    "slug": "minimum-length-of-string-after-deleting-similar-ends",
    "category": "String",
    "aliases": [],
    "tags": ["two_pointer", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum length of a string after repeatedly removing identical characters from both ends.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum length of the string after repeatedly removing 
    identical characters from both ends.

    Args:
        s: The input string.

    Returns:
        The length of the remaining string after all possible deletions.

    Examples:
        >>> solve("caaaac")
        0
        >>> solve("aabaa")
        3
        >>> solve("abcd")
        4
    """
    left_index = 0
    right_index = len(s) - 1

    # Continue as long as the pointers haven't crossed or met
    while left_index < right_index:
        # If the characters at both ends are different, no more deletions possible
        if s[left_index] != s[right_index]:
            break
        
        target_char = s[left_index]
        
        # Shrink from the left side
        while left_index <= right_index and s[left_index] == target_char:
            left_index += 1
            
        # Shrink from the right side
        # Note: We check left_index <= right_index to handle cases where 
        # the entire remaining substring consists of the same character
        while right_index >= left_index and s[right_index] == target_char:
            right_index -= 1

    # The remaining length is the distance between the pointers
    # If pointers crossed, length is 0
    return max(0, right_index - left_index + 1)
