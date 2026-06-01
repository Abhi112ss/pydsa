METADATA = {
    "id": 1616,
    "name": "Split Two Strings to Make Palindrome",
    "slug": "split_two_strings_to_make_palindrome",
    "category": "string",
    "aliases": [],
    "tags": ["strings", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if swapping prefixes of two equal‑length strings can form a palindrome.",
}


def _is_palindrome(sub: str, left: int, right: int) -> bool:
    """Check if sub[left:right+1] is a palindrome."""
    while left < right:
        if sub[left] != sub[right]:
            return False
        left += 1
        right -= 1
    return True


def _can_form_palindrome(first: str, second: str) -> bool:
    """
    Check whether a palindrome can be formed by taking a prefix from `first`
    and a suffix from `second`.

    Args:
        first: The string providing the left part of the candidate palindrome.
        second: The string providing the right part of the candidate palindrome.

    Returns:
        True if a palindrome can be formed, False otherwise.
    """
    n = len(first)
    left, right = 0, n - 1

    # Move pointers inward while characters match across the two strings.
    while left < right and first[left] == second[right]:
        left += 1
        right -= 1

    # If pointers have crossed, the combined string is already a palindrome.
    if left >= right:
        return True

    # Otherwise, one of the remaining substrings must be a palindrome.
    # Check the substring from `first` and the substring from `second`.
    return _is_palindrome(first, left, right) or _is_palindrome(second, left, right)


def solve() -> None:
    """
    Reads two equal‑length strings from standard input and prints
    `True` if a palindrome can be formed by swapping prefixes, otherwise `False`.

    Example:
        Input:
            abc
            def
        Output:
            False
    """
    import sys

    data = sys.stdin.read().splitlines()
    if len(data) < 2:
        return
    a = data[0].strip()
    b = data[1].strip()

    result = _can_form_palindrome(a, b) or _can_form_palindrome(b, a)
    sys.stdout.write(str(result))