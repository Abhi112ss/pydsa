METADATA = {
    "id": 821,
    "name": "Shortest Distance to a Character",
    "slug": "shortest_distance_to_a_character",
    "category": "String",
    "aliases": [],
    "tags": ["two_pass", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return an array of distances from each character to the nearest occurrence of a given target character.",
}


def solve(s: str, target: str) -> list[int]:
    """Compute the shortest distance from each character in ``s`` to the nearest ``target`` character.

    Args:
        s: The input string consisting of lowercase English letters.
        target: A single character that is guaranteed to appear at least once in ``s``.

    Returns:
        A list of integers where the i‑th element is the minimum distance from ``s[i]`` to any occurrence of ``target``.

    Examples:
        >>> solve("loveleetcode", "e")
        [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
        >>> solve("aaab", "b")
        [3, 2, 1, 0]
    """
    n: int = len(s)
    distances: list[int] = [0] * n

    # First pass: left to right, track distance from the most recent target character.
    previous_target_index: int = -n  # sentinel far to the left
    for i in range(n):
        if s[i] == target:
            previous_target_index = i
        distances[i] = i - previous_target_index

    # Second pass: right to left, update with the smaller distance from the next target character.
    next_target_index: int = 2 * n  # sentinel far to the right
    for i in range(n - 1, -1, -1):
        if s[i] == target:
            next_target_index = i
        right_distance: int = next_target_index - i
        if right_distance < distances[i]:
            distances[i] = right_distance

    return distances