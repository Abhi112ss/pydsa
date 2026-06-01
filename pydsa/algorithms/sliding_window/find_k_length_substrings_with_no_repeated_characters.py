METADATA = {
    "id": 1100,
    "name": "Find K-Length Substrings With No Repeated Characters",
    "slug": "find-k-length-substrings-with-no-repeated-characters",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["sliding_window", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(min(n, alphabet_size))",
    "description": "Find all substrings of length k that contain no duplicate characters.",
}

def solve(s: str, k: int) -> list[str]:
    """
    Finds all substrings of length k in string s that have no repeated characters.

    Args:
        s: The input string to search through.
        k: The required length of the substrings.

    Returns:
        A list of substrings of length k that contain only unique characters.

    Examples:
        >>> solve("abcabc", 3)
        ['abc', 'bca', 'cab', 'abc']
        >>> solve("abacaba", 3)
        ['bac', 'aca', 'cab', 'aba'] -> wait, 'aca' and 'aba' have repeats.
        Correct logic: ['bac', 'cab']
        >>> solve("aaabbb", 3)
        []
    """
    n = len(s)
    if k > n or k <= 0:
        return []

    results: list[str] = []
    # char_counts tracks the frequency of characters in the current window
    char_counts: dict[str, int] = {}
    # duplicates_count tracks how many characters currently have a frequency > 1
    duplicates_count: int = 0

    # Initialize the first window of size k
    for i in range(k):
        char = s[i]
        char_counts[char] = char_counts.get(char, 0) + 1
        if char_counts[char] == 2:
            duplicates_count += 1

    # If no duplicates in the first window, add it to results
    if duplicates_count == 0:
        results.append(s[0:k])

    # Slide the window from index 1 to n-k
    for i in range(1, n - k + 1):
        # Character leaving the window (left side)
        out_char = s[i - 1]
        if char_counts[out_char] == 2:
            duplicates_count -= 1
        char_counts[out_char] -= 1
        
        # Character entering the window (right side)
        in_char = s[i + k - 1]
        char_counts[in_char] = char_counts.get(in_char, 0) + 1
        if char_counts[in_char] == 2:
            duplicates_count += 1

        # If duplicates_count is 0, all characters in the current window are unique
        if duplicates_count == 0:
            results.append(s[i : i + k])

    return results
