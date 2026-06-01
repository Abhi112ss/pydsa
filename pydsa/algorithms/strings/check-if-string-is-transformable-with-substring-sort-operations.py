METADATA = {
    "id": 1585,
    "name": "Check If String Is Transformable With Substring Sort Operations",
    "slug": "check_if_string_is_transformable_with_substring_sort_operations",
    "category": "string",
    "aliases": [],
    "tags": ["greedy", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if one string can be turned into another using substring sorting operations.",
}


def is_transformable(source: str, target: str) -> bool:
    """Check whether ``source`` can be transformed into ``target`` by repeatedly sorting
    any substring in non‑decreasing order.

    Args:
        source: The original string.
        target: The desired string after operations.

    Returns:
        True if the transformation is possible, False otherwise.

    Examples:
        >>> is_transformable("abc", "abc")
        True
        >>> is_transformable("abc", "bca")
        False
        >>> is_transformable("aabbcc", "abcabc")
        True
    """
    if len(source) != len(target):
        return False

    # diff[c] stores the net count of character ``chr(c + ord('a'))`` seen so far
    diff: list[int] = [0] * 26

    for index in range(len(source)):
        diff[ord(source[index]) - 97] += 1
        diff[ord(target[index]) - 97] -= 1

        # Verify that the cumulative surplus of smaller characters never becomes negative.
        cumulative_surplus = 0
        for char_index in range(26):
            cumulative_surplus += diff[char_index]
            if cumulative_surplus < 0:
                return False

    return True


def solve() -> None:
    """Read two strings from standard input and output ``true`` if the first can be
    transformed into the second using substring sort operations, otherwise output ``false``.

    Input format:
        The first line contains the string ``source``.
        The second line contains the string ``target``.

    Output format:
        A single line with either ``true`` or ``false``.
    """
    import sys

    data = sys.stdin.read().splitlines()
    if len(data) < 2:
        return
    source = data[0].strip()
    target = data[1].strip()
    result = is_transformable(source, target)
    sys.stdout.write(str(result).lower())