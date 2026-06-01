METADATA = {
    "id": 1763,
    "name": "Longest Nice Substring",
    "slug": "longest-nice-substring",
    "category": "String",
    "aliases": [],
    "tags": ["divide_and_conquer", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the longest substring where every letter appears in both uppercase and lowercase.",
}

def solve(s: str) -> str:
    """
    Finds the longest nice substring using a divide and conquer approach.
    
    A string is 'nice' if for every letter it contains, it contains both 
    its uppercase and lowercase forms.

    Args:
        s: The input string to analyze.

    Returns:
        The longest nice substring. If multiple exist, returns the first one found.
        If none exist, returns an empty string.

    Examples:
        >>> solve("YaceAE")
        "aceAE"
        >>> solve("Bb")
        "Bb"
        >>> solve("aAAb")
        "aAA"
    """
    if len(s) < 2:
        return ""

    # Create a set for O(1) lookup of characters present in the current substring
    char_set = set(s)

    # Iterate through the string to find a character that violates the 'nice' property
    for index, char in enumerate(s):
        # A character is 'bad' if its counterpart (upper/lower) is missing from the set
        if char.swapcase() not in char_set:
            # Divide: Split the string into two parts around the 'bad' character
            # and recursively find the longest nice substring in each part.
            left_part = solve(s[:index])
            right_part = solve(s[index + 1:])

            # Conquer: Return the longer of the two results. 
            # If lengths are equal, the left part is preferred (first occurrence).
            return left_part if len(left_part) >= len(right_part) else right_part

    # Base case: If no 'bad' characters were found, the entire current string is nice.
    return s
