METADATA = {
    "id": 1910,
    "name": "Remove All Occurrences of a Substring",
    "slug": "remove-all-occurrences-of-a-substring",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "stack"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Repeatedly remove the first occurrence of a given substring from a string until it no longer exists.",
}

def solve(s: str, part: str) -> str:
    """
    Removes all occurrences of 'part' from 's' by repeatedly removing the first occurrence.

    Args:
        s: The original input string.
        part: The substring to be removed.

    Returns:
        The resulting string after all occurrences of 'part' are removed.

    Examples:
        >>> solve("daabcbaabcbc", "abc")
        >>> "dab"
        >>> solve("axxxxyyyybbb", "xy")
        >>> "aaabbb"
    """
    # We use a list as a stack to build the string character by character.
    # This allows us to check the end of the current built string efficiently.
    stack: list[str] = []
    part_len = len(part)
    
    for char in s:
        stack.append(char)
        
        # If the stack has enough characters, check if the suffix matches 'part'
        if len(stack) >= part_len:
            # Check if the last 'part_len' characters match the target substring
            # We use slicing on the list which is efficient for small part lengths
            if "".join(stack[-part_len:]) == part:
                # If a match is found, pop the characters belonging to 'part'
                for _ in range(part_len):
                    stack.pop()
                    
    return "".join(stack)
