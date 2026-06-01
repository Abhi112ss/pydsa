METADATA = {
    "id": 925,
    "name": "Long Pressed Name",
    "slug": "long_pressed_name",
    "category": "string",
    "aliases": [],
    "tags": ["string", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if typed could be a long‑pressed version of name.",
}


def solve(name: str, typed: str) -> bool:
    """Check whether `typed` can be produced by long‑pressing characters of `name`.

    Args:
        name: The original string without long presses.
        typed: The string that may contain long‑pressed characters.

    Returns:
        True if `typed` could be a long‑pressed version of `name`, otherwise False.

    Examples:
        >>> solve("alex", "aaleex")
        True
        >>> solve("saeed", "ssaaedd")
        False
        >>> solve("leelee", "lleeelee")
        True
    """
    index_name = 0
    index_typed = 0

    while index_typed < len(typed):
        # If characters match, advance both pointers.
        if index_name < len(name) and name[index_name] == typed[index_typed]:
            index_name += 1
            index_typed += 1
        # If current typed character repeats the previous typed character,
        # it is a long press; only advance typed pointer.
        elif index_typed > 0 and typed[index_typed] == typed[index_typed - 1]:
            index_typed += 1
        else:
            # Mismatch that cannot be explained by a long press.
            return False

    # All characters of `name` must be consumed for a valid match.
    return index_name == len(name)