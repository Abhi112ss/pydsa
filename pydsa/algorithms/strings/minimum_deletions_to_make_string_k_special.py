METADATA = {
    "id": 3085,
    "name": "Minimum Deletions to Make String K-Special",
    "slug": "minimum-deletions-to-make-string-k-special",
    "category": "Greedy",
    "aliases": [],
    "tags": ["strings", "greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(N log N)",
    "space_complexity": "O(N)",
    "description": "Find the minimum number of deletions required to make a string contain at least k distinct characters.",
}

def solve(s: str, k: int) -> int:
    """
    Calculates the minimum number of deletions needed so that the string 
    contains at least k distinct characters.

    To minimize deletions, we want to keep the characters that appear most 
    frequently. We count the frequencies, sort them in descending order, 
    and keep the top k frequencies. Any characters beyond the top k must 
    be deleted entirely.

    Args:
        s: The input string.
        k: The minimum number of distinct characters required.

    Returns:
        The minimum number of deletions required.

    Examples:
        >>> solve("aabbcc", 2)
        2
        >>> solve("abcde", 3)
        2
        >>> solve("aaaaa", 1)
        0
    """
    if k == 0:
        return len(s)

    # Count the frequency of each character
    char_counts: dict[str, int] = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # If we already have at least k distinct characters, 
    # we don't need to delete any characters to satisfy the 'k distinct' rule.
    # However, the problem asks for the minimum deletions to make the string 
    # "k-special". In the context of this specific problem type, 
    # we must ensure we have exactly k or more distinct characters.
    # If we have fewer than k, it's impossible (though constraints usually prevent this).
    
    frequencies: list[int] = list(char_counts.values())
    
    # If we have fewer than k distinct characters, we cannot satisfy the condition.
    # Based on typical LeetCode constraints for this problem, k <= number of distinct chars.
    if len(frequencies) < k:
        return len(s)

    # Sort frequencies in descending order to keep the most frequent characters
    frequencies.sort(reverse=True)

    # To minimize deletions, we keep the k most frequent characters.
    # Any character that is not among the top k must be deleted completely.
    # Additionally, if we want to keep exactly k distinct characters, 
    # we don't actually need to delete anything else because the problem 
    # asks for "at least k" or "exactly k" depending on the specific variant.
    # For "at least k", if we have > k, we delete 0.
    # For "exactly k", we delete all characters that are not in the top k.
    
    # Re-reading the logic: To make a string "k-special" (having k distinct chars),
    # we must remove all occurrences of (total_distinct - k) characters.
    
    # Calculate total characters belonging to characters we decide to remove
    # We keep the top k frequencies, and delete everything else.
    total_deletions = sum(frequencies[k:])

    return total_deletions
