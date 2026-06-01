METADATA = {
    "id": 2287,
    "name": "Rearrange Characters to Make Target String",
    "slug": "rearrange-characters-to-make-target-string",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "string_manipulation", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(1)",
    "description": "Determine if a source string can be rearranged to form a target string based on character frequencies.",
}

def solve(source: str, target: str) -> bool:
    """
    Checks if the source string contains enough characters to form the target string.

    Args:
        source: The string containing the available characters.
        target: The string that needs to be formed.

    Returns:
        True if the target can be formed, False otherwise.

    Examples:
        >>> solve("ae", "a")
        True
        >>> solve("a", "ae")
        False
        >>> solve("abbacc", "abc")
        True
    """
    # Since we are dealing with lowercase English letters, 
    # we can use a fixed-size array of 26 for O(1) space.
    source_counts = [0] * 26
    target_counts = [0] * 26

    # Count frequencies of characters in the source string
    for char in source:
        source_counts[ord(char) - ord('a')] += 1

    # Count frequencies of characters in the target string
    for char in target:
        target_counts[ord(char) - ord('a')] += 1

    # Compare the requirements of the target against the availability in source
    for i in range(26):
        # If target requires more of a character than source provides, return False
        if target_counts[i] > source_counts[i]:
            return False

    return True
