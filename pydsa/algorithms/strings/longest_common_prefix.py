METADATA = {
    "id": 14,
    "name": "Longest Common Prefix",
    "slug": "longest-common-prefix",
    "category": "String",
    "aliases": [],
    "tags": ["string"],
    "difficulty": "easy",
    "time_complexity": "O(S)",
    "space_complexity": "O(1)",
    "description": "Find the longest common prefix string amongst an array of strings.",
}

def solve(strs: list[str]) -> str:
    """
    Finds the longest common prefix among an array of strings using vertical scanning.

    Args:
        strs: A list of strings to evaluate.

    Returns:
        The longest common prefix string. If no common prefix exists, returns an empty string.

    Examples:
        >>> solve(["flower", "flow", "flight"])
        'fl'
        >>> solve(["dog", "racecar", "car"])
        ''
    """
    if not strs:
        return ""

    # Use the first string as the reference for comparison
    reference_string = strs[0]

    # Iterate through each character index of the reference string
    for index in range(len(reference_string)):
        current_char = reference_string[index]

        # Compare this character with the character at the same index in all other strings
        for i in range(1, len(strs)):
            # If we reach the end of one of the strings or find a mismatch
            if index == len(strs[i]) or strs[i][index] != current_char:
                # Return the substring of the reference up to the current index
                return reference_string[:index]

    # If the loop completes, the entire first string is the common prefix
    return reference_string
