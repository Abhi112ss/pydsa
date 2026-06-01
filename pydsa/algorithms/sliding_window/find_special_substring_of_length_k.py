METADATA = {
    "id": 3456,
    "name": "Find Special Substring of Length K",
    "slug": "find-special-substring-of-length-k",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find if there exists a substring of length K that satisfies specific character frequency constraints using a sliding window.",
}

def solve(s: str, k: int, target_char: str, target_count: int) -> bool:
    """
    Determines if there is a substring of length k that contains exactly 
    target_count occurrences of target_char.

    Args:
        s: The input string to search within.
        k: The required length of the substring.
        target_char: The specific character to count.
        target_count: The exact number of target_char required in the substring.

    Returns:
        True if such a substring exists, False otherwise.

    Examples:
        >>> solve("abacaba", 3, "a", 2)
        True
        >>> solve("abacaba", 3, "a", 3)
        False
    """
    n = len(s)
    if k > n:
        return False

    # current_count tracks the number of target_char in the current window
    current_count = 0

    # Initialize the first window of size k
    for i in range(k):
        if s[i] == target_char:
            current_count += 1

    # Check if the first window satisfies the condition
    if current_count == target_count:
        return True

    # Slide the window from index 1 to n - k
    for i in range(k, n):
        # Add the new character entering the window
        if s[i] == target_char:
            current_count += 1
        
        # Remove the character that is leaving the window
        if s[i - k] == target_char:
            current_count -= 1

        # Check the condition for the current window
        if current_count == target_count:
            return True

    return False
