METADATA = {
    "id": 340,
    "name": "Longest Substring with At Most K Distinct Characters",
    "slug": "longest-substring-with-at-most-k-distinct-characters",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Find the length of the longest substring that contains at most k distinct characters.",
}

def solve(s: str, k: int) -> int:
    """
    Finds the length of the longest substring containing at most k distinct characters.

    Args:
        s: The input string.
        k: The maximum number of distinct characters allowed in the substring.

    Returns:
        The length of the longest substring meeting the criteria.

    Examples:
        >>> solve("eceba", 2)
        3
        >>> solve("aa", 1)
        2
    """
    if k == 0 or not s:
        return 0

    # Dictionary to store the frequency of characters in the current window
    char_frequency: dict[str, int] = {}
    max_length: int = 0
    left_pointer: int = 0

    # Iterate through the string with the right pointer
    for right_pointer in range(len(s)):
        current_char = s[right_pointer]
        char_frequency[current_char] = char_frequency.get(current_char, 0) + 1

        # If the number of distinct characters exceeds k, shrink the window from the left
        while len(char_frequency) > k:
            left_char = s[left_pointer]
            char_frequency[left_char] -= 1
            
            # If frequency drops to zero, remove the character from the map to reduce distinct count
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            
            left_pointer += 1

        # Update the maximum length found so far
        current_window_size = right_pointer - left_pointer + 1
        if current_window_size > max_length:
            max_length = current_window_size

    return max_length
