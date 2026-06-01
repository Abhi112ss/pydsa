METADATA = {
    "id": 859,
    "name": "Buddy Strings",
    "slug": "buddy_strings",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "enumeration"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result equals B, otherwise return false.",
}

def solve(A: str, B: str) -> bool:
    """
    Determine if two strings are buddy strings.

    Two strings are buddy strings if you can swap exactly two characters in one string
    to make it equal to the other string.

    Args:
        A (str): The first string.
        B (str): The second string.

    Returns:
        bool: True if A and B are buddy strings, False otherwise.

    Examples:
        >>> solve("ab", "ba")
        True
        >>> solve("ab", "ab")
        False
        >>> solve("aa", "aa")
        True
        >>> solve("aaaaaaabc", "aaaaaaacb")
        True
        >>> solve("", "aa")
        False
    """
    if len(A) != len(B):
        return False

    # If A == B, we need at least one duplicate character to swap
    if A == B:
        # Check if there's any duplicate character in A
        seen = set()
        for char in A:
            if char in seen:
                return True
            seen.add(char)
        return False

    # Find indices where characters differ
    diff_indices = []
    for index in range(len(A)):
        if A[index] != B[index]:
            diff_indices.append(index)
            if len(diff_indices) > 2:
                return False

    # There must be exactly two differences
    if len(diff_indices) != 2:
        return False

    # Check if swapping makes them equal
    first, second = diff_indices
    return A[first] == B[second] and A[second] == B[first]