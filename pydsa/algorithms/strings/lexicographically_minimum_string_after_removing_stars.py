METADATA = {
    "id": 3170,
    "name": "Lexicographically Minimum String After Removing Stars",
    "slug": "lexicographically-minimum-string-after-removing-stars",
    "category": "String",
    "aliases": [],
    "tags": ["stack", "greedy", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Remove characters based on star positions to achieve the lexicographically smallest result.",
}

def solve(s: str) -> str:
    """
    Constructs the lexicographically minimum string by removing characters 
    indicated by stars. Each star removes the nearest available character 
    to its left.

    Args:
        s: The input string containing lowercase English letters and stars.

    Returns:
        The resulting string after all star operations are performed.

    Examples:
        >>> solve("leet**cod*e")
        'letce'
        >>> solve("abc*d*e")
        'ace'
    """
    # We use a stack to keep track of the indices of characters 
    # that have not been removed by a star.
    remaining_indices_stack: list[int] = []
    # A boolean array to mark which indices are removed.
    is_removed: list[bool] = [False] * len(s)

    for index, char in enumerate(s):
        if char == '*':
            # When a star is encountered, it removes the nearest 
            # available character to its left.
            if remaining_indices_stack:
                last_valid_index = remaining_indices_stack.pop()
                is_removed[last_valid_index] = True
        else:
            # If it's a character, add its index to the stack.
            remaining_indices_stack.append(index)

    # Build the final string using only the characters that were not marked as removed.
    result_chars: list[str] = []
    for index, char in enumerate(s):
        if char != '*' and not is_removed[index]:
            result_chars.append(char)

    return "".join(result_chars)
