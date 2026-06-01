METADATA = {
    "id": 299,
    "name": "Bulls and Cows",
    "slug": "bulls-and-cows",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "counting", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given two strings of digits, count the number of bulls (exact matches) and cows (digit matches in wrong positions).",
}

def solve(secret: str, guess: str) -> list[int]:
    """
    Calculates the number of bulls and cows between two digit strings.

    A bull is a digit that is in the correct position in both strings.
    A cow is a digit that is in both strings but in a different position.

    Args:
        secret: The target digit string.
        guess: The guess digit string.

    Returns:
        A list of two integers [bulls, cows].

    Examples:
        >>> solve("1807", "7810")
        [1, 3]
        >>> solve("1123", "0111")
        [1, 1]
    """
    bulls = 0
    cows = 0
    
    # Frequency maps for digits that are not bulls
    # Since digits are 0-9, we can use fixed-size arrays of size 10
    secret_counts = [0] * 10
    guess_counts = [0] * 10

    for s_digit, g_digit in zip(secret, guess):
        if s_digit == g_digit:
            # Exact match found
            bulls += 1
        else:
            # Not a bull, track frequencies to identify cows later
            secret_counts[int(s_digit)] += 1
            guess_counts[int(g_digit)] += 1

    # A cow occurs when a digit exists in both non-bull sets.
    # The number of cows for a specific digit is the minimum of its 
    # occurrences in the remaining secret and guess strings.
    for i in range(10):
        cows += min(secret_counts[i], guess_counts[i])

    return [bulls, cows]
