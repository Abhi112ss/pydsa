METADATA = {
    "id": 1720,
    "name": "Decode XORed Array",
    "slug": "decode-xored-array",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Reconstruct an array given its XORed version and the first element.",
}

def solve(start_val: int, encoded: list[int]) -> list[int]:
    """
    Decodes an array where each element (starting from the second) is the XOR 
    of the previous element and the original element at that position.

    The relationship is: encoded[i] = decoded[i-1] ^ decoded[i].
    Using XOR properties: if a ^ b = c, then a ^ c = b.
    Therefore: decoded[i] = encoded[i-1] ^ decoded[i-1].
    Wait, the problem states: encoded[i] = decoded[i-1] ^ decoded[i].
    Actually, the problem definition is: encoded[i] = decoded[i-1] ^ decoded[i] 
    for i > 0. So decoded[i] = encoded[i] ^ decoded[i-1] is incorrect.
    Let's re-read: encoded[i] = decoded[i-1] ^ decoded[i].
    So, decoded[i] = encoded[i] ^ decoded[i-1] is actually correct.
    Wait, the problem says: encoded[i] = decoded[i-1] ^ decoded[i].
    Let's trace:
    decoded[0] = start_val
    encoded[1] = decoded[0] ^ decoded[1] => decoded[1] = encoded[1] ^ decoded[0]
    Wait, the index in encoded is 1-based relative to decoded? 
    No, encoded[i] = decoded[i-1] ^ decoded[i].
    Example: decoded = [1, 2, 3], encoded = [1, 1^2, 2^3] = [1, 3, 1].
    Wait, the problem says encoded[i] = decoded[i-1] ^ decoded[i] for i > 0.
    And encoded[0] is not used? No, the problem says:
    encoded[i] = decoded[i-1] ^ decoded[i] for i > 0.
    And decoded[0] = start_val.
    The length of encoded is the same as decoded.
    Example: decoded = [1, 2, 3], encoded = [1, 1^2, 2^3] = [1, 3, 1].
    Wait, the example in LeetCode: startVal = 1, encoded = [1, 3, 1].
    decoded[0] = 1.
    encoded[1] = decoded[0] ^ decoded[1] => 3 = 1 ^ decoded[1] => decoded[1] = 1 ^ 3 = 2.
    encoded[2] = decoded[1] ^ decoded[2] => 1 = 2 ^ decoded[2] => decoded[2] = 2 ^ 1 = 3.
    Result: [1, 2, 3].

    Args:
        start_val: The first element of the decoded array.
        encoded: The XORed array.

    Returns:
        The fully decoded array.

    Examples:
        >>> solve(1, [1, 3, 1])
        [1, 2, 3]
        >>> solve(5, [5, 12, 10])
        [5, 9, 3]
    """
    n = len(encoded)
    decoded = [0] * n
    decoded[0] = start_val

    # We iterate through the encoded array starting from index 1.
    # Since encoded[i] = decoded[i-1] ^ decoded[i], 
    # it follows that decoded[i] = encoded[i] ^ decoded[i-1].
    for i in range(1, n):
        decoded[i] = encoded[i] ^ decoded[i - 1]

    return decoded
