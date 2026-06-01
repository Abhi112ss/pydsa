METADATA = {
    "id": 844,
    "name": "Backspace String Compare",
    "slug": "backspace_string_compare",
    "category": "String",
    "aliases": [],
    "tags": ["two_pointer", "string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(1)",
    "description": "Given two strings s and t, return true if they are equal when both are typed into empty text editors, where '#' represents a backspace character.",
}

def solve(s: str, t: str) -> bool:
    """Compare two strings after processing backspace characters.

    Args:
        s: First input string containing lowercase letters and '#' characters.
        t: Second input string containing lowercase letters and '#' characters.

    Returns:
        True if both strings are equal after processing backspaces, False otherwise.

    Examples:
        >>> solve("ab#c", "ad#c")
        True
        >>> solve("ab##", "c#d#")
        True
        >>> solve("a#c", "b")
        False
    """
    # Use two pointers starting from the end of each string
    pointer_s = len(s) - 1
    pointer_t = len(t) - 1

    while pointer_s >= 0 or pointer_t >= 0:
        # Find next valid character in s (skip characters that would be deleted by backspaces)
        skip_s = 0
        while pointer_s >= 0:
            if s[pointer_s] == '#':
                skip_s += 1  # Found a backspace, need to skip more characters
                pointer_s -= 1
            elif skip_s > 0:
                skip_s -= 1  # This character gets deleted by a backspace
                pointer_s -= 1
            else:
                break  # Found a valid character

        # Find next valid character in t (skip characters that would be deleted by backspaces)
        skip_t = 0
        while pointer_t >= 0:
            if t[pointer_t] == '#':
                skip_t += 1  # Found a backspace, need to skip more characters
                pointer_t -= 1
            elif skip_t > 0:
                skip_t -= 1  # This character gets deleted by a backspace
                pointer_t -= 1
            else:
                break  # Found a valid character

        # Compare the valid characters found in both strings
        if pointer_s >= 0 and pointer_t >= 0:
            if s[pointer_s] != t[pointer_t]:
                return False
        elif pointer_s >= 0 or pointer_t >= 0:
            # One string has a valid character while the other doesn't
            return False

        # Move to the next character to process
        pointer_s -= 1
        pointer_t -= 1

    return True