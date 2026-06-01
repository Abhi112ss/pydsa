METADATA = {
    "id": 3694,
    "name": "Distinct Points Reachable After Substring Removal",
    "slug": "distinct_points_reachable_after_substring_removal",
    "category": "algorithms",
    "aliases": [],
    "tags": ["strings", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Count distinct end points reachable after removing any contiguous substring of moves.",
}


def solve() -> None:
    """Read a string of moves and print the number of distinct points reachable.

    Args:
        None (reads from standard input).

    Returns:
        None (prints the result).

    Example:
        >>> import sys, io
        >>> sys.stdin = io.StringIO("LRUD")
        >>> solve()
        5
    """
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return
    moves: str = data[0]

    # Mapping from move character to coordinate delta.
    delta = {
        'L': (-1, 0),
        'R': (1, 0),
        'U': (0, 1),
        'D': (0, -1),
    }

    n: int = len(moves)

    # Prefix positions: position after processing first i characters.
    prefix: list[tuple[int, int]] = [(0, 0)] * (n + 1)
    for i in range(n):
        dx, dy = delta[moves[i]]
        px, py = prefix[i]
        prefix[i + 1] = (px + dx, py + dy)

    # Suffix positions: position after processing characters from i to end,
    # assuming we start at the origin.
    suffix: list[tuple[int, int]] = [(0, 0)] * (n + 1)
    for i in range(n - 1, -1, -1):
        dx, dy = delta[moves[i]]
        sx, sy = suffix[i + 1]
        suffix[i] = (dx + sx, dy + sy)

    reachable: set[tuple[int, int]] = set()
    # For each possible removal substring [i, j), combine prefix[i] with suffix[j].
    for i in range(n + 1):
        px, py = prefix[i]
        for j in range(i, n + 1):
            sx, sy = suffix[j]
            reachable.add((px + sx, py + sy))

    print(len(reachable))
