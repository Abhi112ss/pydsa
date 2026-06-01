METADATA = {
    "id": 3545,
    "name": "Minimum Deletions for At Most K Distinct Characters",
    "slug": "minimum_deletions_for_at_most_k_distinct_characters",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "greedy", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of deletions required to make a string contain at most k distinct characters.",
}

def solve(s: str, k: int) -> int:
    """
    Calculates the minimum number of deletions needed to ensure the remaining 
    string contains at most k distinct characters.

    The problem is equivalent to finding the longest substring that contains 
    at most k distinct characters and subtracting its length from the total 
    length of the string.

    Args:
        s: The input string.
        k: The maximum number of distinct characters allowed.

    Returns:
        The minimum number of deletions required.

    Examples:
        >>> solve("eceba", 2)
        2
        >>> solve("aaabbb", 1)
        3
        >>> solve("abcde", 3)
        2
    """
    if k <= 0:
        return len(s)
    
    n = len(s)
    max_substring_len = 0
    char_frequency = {}
    left_pointer = 0

    # Use a sliding window to find the longest substring with <= k distinct characters
    for right_pointer in range(n):
        current_char = s[right_pointer]
        char_frequency[current_char] = char_frequency.get(current_char, 0) + 1

        # If distinct characters exceed k, shrink the window from the left
        while len(char_frequency) > k:
            left_char = s[left_pointer]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            left_pointer += 1

        # Update the maximum length found so far
        current_window_size = right_pointer - left_pointer + 1
        if current_window_size > max_substring_len:
            max_substring_len = current_window_size

    # Minimum deletions = Total length - Longest valid substring length
    return n - max_substring_len
