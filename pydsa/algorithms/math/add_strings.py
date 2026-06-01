METADATA = {
    "id": 415,
    "name": "Add Strings",
    "slug": "add_strings",
    "category": "String",
    "aliases": [],
    "tags": ["two_pointer", "string"],
    "difficulty": "easy",
    "time_complexity": "O(max(n, m))",
    "space_complexity": "O(max(n, m))",
    "description": "Given two non-negative integers represented as strings, return their sum as a string without converting to integers directly.",
}


def solve(num1: str, num2: str) -> str:
    """Add two non-negative integers represented as strings without converting to integers.

    Simulates manual addition from right to left using two pointers and a carry variable.

    Args:
        num1: First non-negative integer as a string.
        num2: Second non-negative integer as a string.

    Returns:
        The sum of num1 and num2 as a string.

    Examples:
        >>> solve("11", "123")
        '134'
        >>> solve("456", "77")
        '533'
        >>> solve("0", "0")
        '0'
    """
    result = []
    carry = 0
    pointer1 = len(num1) - 1
    pointer2 = len(num2) - 1

    # Process digits from right to left until both strings are exhausted and no carry remains
    while pointer1 >= 0 or pointer2 >= 0 or carry:
        digit1 = int(num1[pointer1]) if pointer1 >= 0 else 0
        digit2 = int(num2[pointer2]) if pointer2 >= 0 else 0

        total = digit1 + digit2 + carry
        carry = total // 10
        result.append(str(total % 10))

        pointer1 -= 1
        pointer2 -= 1

    # Reverse to get the correct order since we built the result from least significant digit
    return ''.join(reversed(result))