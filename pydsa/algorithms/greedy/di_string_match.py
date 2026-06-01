METADATA = {
    "id": 942,
    "name": "DI String Match",
    "slug": "di_string_match",
    "category": "array",
    "aliases": [],
    "tags": ["two_pointer", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return a permutation that satisfies the given DI string constraints.",
}


def solve(s: str) -> list[int]:
    """Generate a permutation of numbers 0..n that matches a DI string.

    Args:
        s: A string consisting only of characters 'I' (increase) and 'D' (decrease).

    Returns:
        A list of length len(s) + 1 containing a permutation of the integers
        from 0 to len(s) such that for each index i:
        - if s[i] == 'I', then result[i] < result[i + 1]
        - if s[i] == 'D', then result[i] > result[i + 1]

    Examples:
        >>> solve("IDID")
        [0, 4, 1, 3, 2]
        >>> solve("III")
        [0, 1, 2, 3]
        >>> solve("DD")
        [2, 1, 0]
    """
    low = 0
    high = len(s)
    result: list[int] = []

    # Iterate through the DI string, choosing the smallest or largest
    # remaining number based on the current character.
    for char in s:
        if char == "I":
            result.append(low)
            low += 1
        else:  # char == "D"
            result.append(high)
            high -= 1

    # One number remains after processing all characters.
    result.append(low)  # low == high at this point
    return result