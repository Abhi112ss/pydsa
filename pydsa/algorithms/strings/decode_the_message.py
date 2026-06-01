METADATA = {
    "id": 2325,
    "name": "Decode the Message",
    "slug": "decode_the_message",
    "category": "string",
    "aliases": [],
    "tags": ["hash_map", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Decode a message using a substitution cipher derived from a key string.",
}


def solve(key: str, message: str) -> str:
    """Decode a message using a substitution cipher derived from a key string.

    Args:
        key: A string containing lowercase letters and spaces that defines the cipher.
        message: The encoded message consisting of lowercase letters and spaces.

    Returns:
        The decoded message where each letter is replaced according to the cipher.

    Examples:
        >>> solve("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv")
        'this is a secret'
        >>> solve("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lq")
        'the quick brown fox jumps over the lazy dog'
    """
    # Build mapping from each unique letter in key to successive letters starting from 'a'.
    mapping: dict[str, str] = {}
    next_char_code: int = ord('a')
    for character in key:
        if character == ' ':
            continue
        if character not in mapping:
            mapping[character] = chr(next_char_code)
            next_char_code += 1
            if next_char_code > ord('z'):  # safety check, though not needed per constraints
                break

    # Decode the message using the constructed mapping; preserve spaces.
    decoded_chars: list[str] = []
    for character in message:
        if character == ' ':
            decoded_chars.append(' ')
        else:
            decoded_chars.append(mapping[character])
    return ''.join(decoded_chars)