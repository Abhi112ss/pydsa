METADATA = {
    "id": 1249,
    "name": "Minimum Remove to Make Valid Parentheses",
    "slug": "minimum-remove-to-make-valid-parentheses",
    "category": "String",
    "aliases": [],
    "tags": ["stack", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Remove the minimum number of parentheses so that the resulting string is valid.",
}

def solve(s: str) -> str:
    """
    Removes the minimum number of parentheses to make the input string valid.

    A string is valid if:
    1. It is an empty string, or
    2. It can be written as AB (concatenation of two valid strings), or
    3. It can be written as (A) where A is a valid string.

    Args:
        s: The input string containing lowercase English letters and '(' or ')'.

    Returns:
        A string that is valid after removing the minimum number of parentheses.

    Examples:
        >>> solve("lee(t(c)o)de)")
        'lee(t(c)o)de'
        >>> solve("a)b(c)d")
        'ab(c)d'
        >>> solve("))((")
        ''
    """
    # Convert string to list because strings are immutable in Python
    char_list = list(s)
    # Stack to store indices of '(' that haven't been matched yet
    unmatched_open_indices = []
    # Set to store indices of characters that need to be removed
    indices_to_remove = set()

    for index, char in enumerate(char_list):
        if char == '(':
            unmatched_open_indices.append(index)
        elif char == ')':
            if unmatched_open_indices:
                # Found a matching pair, pop the last '(' index
                unmatched_open_indices.pop()
            else:
                # No matching '(' for this ')', mark for removal
                indices_to_remove.add(index)

    # Any '(' left in the stack are unmatched and must be removed
    for index in unmatched_open_indices:
        indices_to_remove.add(index)

    # Build the final string by skipping indices marked for removal
    result_chars = []
    for index, char in enumerate(char_list):
        if index not in indices_to_remove:
            result_chars.append(char)

    return "".join(result_chars)
