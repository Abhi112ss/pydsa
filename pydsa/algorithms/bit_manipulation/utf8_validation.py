METADATA = {
    "id": 393,
    "name": "UTF-8 Validation",
    "slug": "utf-8-validation",
    "category": "Simulation",
    "aliases": [],
    "tags": ["bit manipulation", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if an input array of integers represents a valid UTF-8 encoding.",
}

def solve(data: list[int]) -> bool:
    """
    Validates whether a given list of integers represents a valid UTF-8 encoding.

    Args:
        data: A list of integers where each integer represents a byte (0-255).

    Returns:
        True if the sequence is valid UTF-8, False otherwise.

    Examples:
        >>> solve([197, 130, 1])
        True
        >>> solve([235, 140, 4] )
        False
    """
    # Number of continuation bytes we are currently expecting
    continuation_bytes_to_follow = 0

    for byte in data:
        # We only care about the 8 least significant bits
        byte = byte & 0xFF

        if continuation_bytes_to_follow == 0:
            # Determine how many bytes the current UTF-8 character has
            # by checking the most significant bits of the leading byte.
            if (byte >> 7) == 0b0:
                # 1-byte character (0xxxxxxx)
                continuation_bytes_to_follow = 0
            elif (byte >> 5) == 0b110:
                # 2-byte character (110xxxxx)
                continuation_bytes_to_follow = 1
            elif (byte >> 4) == 0b1110:
                # 3-byte character (1110xxxx)
                continuation_bytes_to_follow = 2
            elif (byte >> 3) == 0b11110:
                # 4-byte character (11110xxx)
                continuation_bytes_to_follow = 3
            else:
                # Invalid leading byte (e.g., starts with 10xxxxxx or 11111xxx)
                return False
        else:
            # Check if the current byte is a valid continuation byte (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            continuation_bytes_to_follow -= 1

    # If we finished the loop but still expect continuation bytes, it's invalid
    return continuation_bytes_to_follow == 0
