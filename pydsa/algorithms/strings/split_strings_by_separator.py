METADATA = {
    "id": 2788,
    "name": "Split Strings by Separator",
    "slug": "split-strings-by-separator",
    "category": "String",
    "aliases": [],
    "tags": ["string", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Split a string into a list of substrings based on a given separator.",
}

def solve(s: str, delimiter: str) -> list[str]:
    """
    Splits the input string into a list of substrings using the provided delimiter.

    Args:
        s: The input string to be split.
        delimiter: The substring used as the separator.

    Returns:
        A list of substrings extracted from the original string.

    Examples:
        >>> solve("leetcode", "e")
        ['l', '', 'tc', 'od', '']
        >>> solve("apple", "p")
        ['a', '', 'le']
        >>> solve("hello", "z")
        ['hello']
    """
    if not delimiter:
        return [s]

    result: list[str] = []
    start_index: int = 0
    delimiter_length: int = len(delimiter)
    string_length: int = len(s)

    # Iterate through the string to find occurrences of the delimiter
    current_pos: int = 0
    while current_pos <= string_length - delimiter_length:
        # Check if the substring starting at current_pos matches the delimiter
        if s[current_pos : current_pos + delimiter_length] == delimiter:
            # Append the substring from the last split point to the start of the delimiter
            result.append(s[start_index:current_pos])
            # Move the pointer past the delimiter
            start_index = current_pos + delimiter_length
            current_pos = start_index
        else:
            current_pos += 1

    # Append the remaining part of the string after the last delimiter
    result.append(s[start_index:])
    
    return result
