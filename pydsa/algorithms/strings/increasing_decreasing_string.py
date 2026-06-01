METADATA = {
    "id": 1370,
    "name": "Increasing Decreasing String",
    "slug": "increasing_decreasing_string",
    "category": "String",
    "aliases": [],
    "tags": ["strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Reorder characters by repeatedly picking the smallest then largest remaining characters.",
}


def _increasing_decreasing_string(s: str) -> str:
    """Return the string reordered by repeatedly taking the smallest then largest remaining characters.

    Args:
        s: Input string consisting of lowercase English letters.

    Returns:
        A new string arranged according to the increasing‑decreasing rule.

    Examples:
        >>> _increasing_decreasing_string("aaaabbbbcccc")
        'abccbaabccba'
        >>> _increasing_decreasing_string("rat")
        'art'
    """
    # Frequency array for 26 lowercase letters
    char_counts: list[int] = [0] * 26
    for ch in s:
        char_counts[ord(ch) - ord('a')] += 1

    result_chars: list[str] = []
    total_length: int = len(s)

    # Continue until all characters are placed
    while len(result_chars) < total_length:
        # Ascending pass: pick smallest available character
        for i in range(26):
            if char_counts[i] > 0:
                result_chars.append(chr(i + ord('a')))
                char_counts[i] -= 1
        # Descending pass: pick largest available character
        for i in range(25, -1, -1):
            if char_counts[i] > 0:
                result_chars.append(chr(i + ord('a')))
                char_counts[i] -= 1

    return "".join(result_chars)


def solve() -> None:
    """Read a string from standard input, apply the increasing‑decreasing ordering,
    and print the resulting string.

    Input format:
        A single line containing the string s.

    Output format:
        The reordered string.

    Example:
        Input:  rat
        Output: art
    """
    import sys

    input_data: str = sys.stdin.readline().strip()
    if not input_data:
        return
    ordered_string: str = _increasing_decreasing_string(input_data)
    sys.stdout.write(ordered_string)