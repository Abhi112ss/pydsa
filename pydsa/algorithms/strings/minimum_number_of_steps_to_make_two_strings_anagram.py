METADATA = {
    "id": 1347,
    "name": "Minimum Number of Steps to Make Two Strings Anagram",
    "slug": "minimum-number-of-steps-to-make-two-strings-an-anagram",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "counting", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of characters to replace in one string to make it an anagram of another string of the same length.",
}

def solve(s: str, t: str) -> int:
    """
    Calculates the minimum number of character replacements needed to make s an anagram of t.

    Args:
        s: The first input string.
        t: The second input string.

    Returns:
        The minimum number of steps (replacements) required.

    Examples:
        >>> solve("leetcode", "practice")
        5
        >>> solve("anagram", "mangaar")
        0
    """
    # Since the strings consist of lowercase English letters, 
    # we can use a fixed-size array of 26 to store character frequencies.
    # This ensures O(1) space complexity regardless of input length.
    char_counts = [0] * 26
    
    # Count occurrences of each character in string s
    for char in s:
        char_counts[ord(char) - ord('a')] += 1
        
    # Subtract occurrences of each character in string t
    for char in t:
        char_counts[ord(char) - ord('a')] -= 1
        
    # The number of steps is the sum of all positive differences.
    # A positive difference means string 's' has more of that character 
    # than string 't', requiring a replacement to match 't'.
    steps = 0
    for count in char_counts:
        if count > 0:
            steps += count
            
    return steps
