METADATA = {
    "id": 405,
    "name": "Convert a Number to Hexadecimal",
    "slug": "convert_a_number_to_hexadecimal",
    "category": "Math",
    "aliases": [],
    "tags": ["bit_manipulation", "math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Convert a 32-bit signed integer to its hexadecimal string representation.",
}


def solve(num: int) -> str:
    """Convert a 32-bit signed integer to its hexadecimal representation.

    Args:
        num: The integer to convert. It may be negative; conversion follows
            two's complement for 32‑bit signed integers.

    Returns:
        A string containing the hexadecimal representation without leading zeros.
        For zero, returns "0". Hex digits are in lowercase.

    Examples:
        >>> solve(26)
        '1a'
        >>> solve(-1)
        'ffffffff'
        >>> solve(0)
        '0'
    """
    # Mapping from a 4‑bit value to its hexadecimal character.
    hex_chars = "0123456789abcdef"

    if num == 0:
        return "0"

    # For negative numbers, interpret as unsigned 32‑bit integer.
    if num < 0:
        num &= 0xffffffff

    hex_digits: list[str] = []
    while num != 0:
        # Extract the lowest 4 bits.
        digit_value = num & 0xF
        # Convert to corresponding hex character and store.
        hex_digits.append(hex_chars[digit_value])
        # Shift right by 4 bits to process the next group.
        num >>= 4

    # The digits were collected from least‑significant to most‑significant,
    # so reverse them to obtain the correct order.
    return "".join(reversed(hex_digits))