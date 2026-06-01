METADATA = {
    "id": 3481,
    "name": "Apply Substitutions",
    "slug": "apply_substitutions",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n * k)",
    "space_complexity": "O(n)",
    "description": "Apply a series of range-based character substitutions to a string.",
}

def solve(s: str, substitutions: list[list[int | str]]) -> str:
    """
    Applies a series of substitutions to a given string. Each substitution 
    is defined by a range [start, end] and a character to replace the range with.

    Args:
        s: The initial input string.
        substitutions: A list of lists where each sub-list contains 
            [start_index, end_index, replacement_char].

    Returns:
        The resulting string after all substitutions have been applied.

    Examples:
        >>> solve("abcdef", [[0, 2, "z"], [3, 5, "y"]])
        'zzcdyy'
        >>> solve("hello", [[1, 3, "a"]])
        'haalo'
    """
    # Convert string to list for mutable operations
    char_list = list(s)
    n = len(char_list)

    for sub in substitutions:
        # Unpack the substitution parameters
        # Note: The problem implies end_index is inclusive based on typical range problems
        start_idx = int(sub[0])
        end_idx = int(sub[1])
        replacement_char = str(sub[2])

        # Ensure indices are within the bounds of the string
        actual_start = max(0, start_idx)
        actual_end = min(n - 1, end_idx)

        # Apply the substitution across the specified range
        # We iterate through the range and replace each character
        if actual_start <= actual_end:
            for i in range(actual_start, actual_end + 1):
                char_list[i] = replacement_char

    return "".join(char_list)
