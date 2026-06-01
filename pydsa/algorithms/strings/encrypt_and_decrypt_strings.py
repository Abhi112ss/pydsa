METADATA = {
    "id": 2227,
    "name": "Encrypt and Decrypt Strings",
    "slug": "encrypt_and_decrypt_strings",
    "category": "string",
    "aliases": [],
    "tags": ["string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Encrypt a string by converting characters to ASCII codes, grouping, reversing, and decrypt it back.",
}


def encrypt(original: str, k: int) -> str:
    """Convert each character to its ASCII decimal representation, split into groups of size *k*,
    reverse each group, and concatenate the results.

    Args:
        original: The plain text string to encrypt.
        k: The size of each group for reversal.

    Returns:
        The encrypted string.

    Example:
        >>> encrypt("abc", 2)
        '21 31'  # actual output would be '21' + '31' reversed groups
    """
    # Convert characters to ASCII codes and concatenate them.
    ascii_digits = "".join(str(ord(ch)) for ch in original)

    # Split the concatenated digits into groups of length *k*.
    groups = [ascii_digits[i:i + k] for i in range(0, len(ascii_digits), k)]

    # Reverse each group and join them to form the encrypted string.
    return "".join(group[::-1] for group in groups)


def decrypt(encoded: str, k: int) -> str:
    """Reverse the encryption process: split the encoded string into groups of size *k*,
    reverse each group, then parse ASCII codes back into characters.

    Args:
        encoded: The encrypted string.
        k: The group size used during encryption.

    Returns:
        The original plain text string.

    Example:
        >>> decrypt("321", 2)
        'abc'
    """
    # Split the encoded string into groups of length *k*.
    groups = [encoded[i:i + k] for i in range(0, len(encoded), k)]

    # Reverse each group to recover the original digit sequence.
    digit_sequence = "".join(group[::-1] for group in groups)

    # Parse the digit sequence back into characters.
    i = 0
    n = len(digit_sequence)
    characters = []
    while i < n:
        # Try to read a 2‑digit ASCII code first.
        if i + 2 <= n:
            two_digit = int(digit_sequence[i:i + 2])
            if 65 <= two_digit <= 90 or 97 <= two_digit <= 122:
                characters.append(chr(two_digit))
                i += 2
                continue
        # Fallback to a 3‑digit ASCII code.
        three_digit = int(digit_sequence[i:i + 3])
        characters.append(chr(three_digit))
        i += 3
    return "".join(characters)


def solve() -> None:
    """Read operation, string, and integer *k* from standard input, perform encryption or decryption,
    and write the result to standard output.

    Input format:
        operation
        string
        k

    where *operation* is either "encrypt" or "decrypt".

    Example:
        Input:
            encrypt
            hello
            3
        Output:
            (encrypted string)
    """
    import sys

    lines = [line.rstrip("\n") for line in sys.stdin.readlines()]
    if len(lines) < 3:
        return

    operation = lines[0].strip().lower()
    string_input = lines[1]
    k = int(lines[2].strip())

    if operation == "encrypt":
        result = encrypt(string_input, k)
    else:
        result = decrypt(string_input, k)

    sys.stdout.write(result)