METADATA = {
    "id": 1332,
    "name": "Remove Palindromic Subsequences",
    "slug": "remove-palindromic-subsequences",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of steps to remove all characters from a string containing only 'a' and 'b' where each step removes a palindromic subsequence.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum number of steps to remove all characters from the string.
    
    Since the string only contains 'a' and 'b', any subsequence consisting 
    only of 'a's is a palindrome, and any subsequence consisting only of 'b's 
    is a palindrome. Therefore, the answer can only be 0 (empty string), 
    1 (if the whole string is a palindrome), or 2 (remove all 'a's then all 'b's).

    Args:
        s: A string containing only characters 'a' and 'b'.

    Returns:
        The minimum number of steps to remove all characters.

    Examples:
        >>> solve("ab")
        2
        >>> solve("aaa")
        1
        >>> solve("")
        0
    """
    if not s:
        return 0

    # Check if the string is a palindrome using two-pointer approach
    left_index = 0
    right_index = len(s) - 1
    is_palindrome = True
    
    while left_index < right_index:
        if s[left_index] != s[right_index]:
            is_palindrome = False
            break
        left_index += 1
        right_index -= 1

    # If the string is a palindrome, we can remove it in 1 step.
    # Otherwise, we can remove all 'a's in step 1 and all 'b's in step 2.
    return 1 if is_palindrome else 2
