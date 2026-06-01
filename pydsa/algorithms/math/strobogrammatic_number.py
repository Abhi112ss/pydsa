METADATA = {
    "id": 246,
    "name": "Strobogrammatic Number",
    "slug": "strobogrammatic_number",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a numeric string looks the same when rotated 180 degrees.",
}


def solve(num: str) -> bool:
    """Check whether the given numeric string is strobogrammatic.

    Args:
        num: A string consisting of digits.

    Returns:
        True if the string reads the same after a 180-degree rotation, otherwise False.

    Examples:
        >>> solve("69")
        True
        >>> solve("88")
        True
        >>> solve("962")
        False
    """
    # Mapping of each digit to its rotated counterpart.
    rotation_map = {
        "0": "0",
        "1": "1",
        "6": "9",
        "8": "8",
        "9": "6",
    }

    left_index = 0
    right_index = len(num) - 1

    while left_index <= right_index:
        left_digit = num[left_index]
        right_digit = num[right_index]

        # If the left digit has no valid rotation or does not match the right digit, reject.
        if left_digit not in rotation_map or rotation_map[left_digit] != right_digit:
            return False

        left_index += 1
        right_index -= 1

    return True