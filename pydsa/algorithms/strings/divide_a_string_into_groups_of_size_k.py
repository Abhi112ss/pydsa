METADATA = {
    "id": 2138,
    "name": "Divide a String Into Groups of Size k",
    "slug": "divide_a_string_into_groups_of_size_k",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Divide a string into groups of size k, padding the final group with '*' if necessary.",
}


def solve(s: str, k: int) -> list[str]:
    """Divide a string into groups of size ``k`` and pad the last group with ``'*'`` if needed.

    Args:
        s: The input string to be divided.
        k: The desired size of each group; must be a positive integer.

    Returns:
        A list of substrings where each substring has length ``k``. The final substring
        is padded with ``'*'`` characters if the original string does not divide evenly.

    Examples:
        >>> solve("abcdefghi", 3)
        ['abc', 'def', 'ghi']
        >>> solve("abcdefghij", 3)
        ['abc', 'def', 'ghi', 'j**']
    """
    if k <= 0:
        raise ValueError("Group size k must be a positive integer")

    groups: list[str] = []
    string_length: int = len(s)

    # Iterate over the string in steps of k, extracting each group.
    for start_index in range(0, string_length, k):
        group: str = s[start_index:start_index + k]

        # If the extracted group is shorter than k, pad it with '*'.
        if len(group) < k:
            group += "*" * (k - len(group))

        groups.append(group)

    return groups