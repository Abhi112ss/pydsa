METADATA = {
    "id": 1540,
    "name": "Can Convert String in K Moves",
    "slug": "can-convert-string-in-k-moves",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a target string can be converted to a source string within k shifts, where each shift increases a character's value by 1 modulo 26.",
}

def solve(s: str, target: str, k: int) -> bool:
    """
    Determines if the target string can be formed from the source string 
    within k shifts. Each shift increments a character by 1 (wrapping 'z' to 'a').
    Each unique shift amount used can be reused infinitely many times.

    Args:
        s: The source string.
        target: The target string to convert to.
        k: The maximum number of unique shifts allowed.

    Returns:
        True if the conversion is possible within k unique shifts, False otherwise.

    Examples:
        >>> solve("abc", "bcd", 1)
        True
        >>> solve("abc", "bcd", 0)
        False
        >>> solve("abc", "bce", 2)
        True
    """
    # If lengths differ, conversion is impossible
    if len(s) != len(target):
        return False

    # Track which shift amounts (0-25) are required.
    # Since there are only 26 possible shifts, space is O(1).
    required_shifts = set()

    for char_s, char_t in zip(s, target):
        val_s = ord(char_s) - ord('a')
        val_t = ord(char_t) - ord('a')

        # Calculate the number of shifts needed to get from s to t.
        # (val_t - val_s) % 26 handles the wrap-around logic.
        shift = (val_t - val_s) % 26

        # If shift is 0, no movement is needed, so we don't count it as a move.
        if shift != 0:
            required_shifts.add(shift)

    # The problem states we can reuse the same shift amount infinitely.
    # Therefore, we only need to check if the number of unique non-zero 
    # shifts required is less than or equal to k.
    return len(required_shifts) <= k
