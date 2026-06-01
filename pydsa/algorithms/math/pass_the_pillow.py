METADATA = {
    "id": 2582,
    "name": "Pass the Pillow",
    "slug": "pass_the_pillow",
    "category": "simulation",
    "aliases": [],
    "tags": ["math", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Return the person holding the pillow after a given number of seconds.",
}


def solve(n: int, time: int) -> int:
    """Return the index of the person holding the pillow after ``time`` seconds.

    The pillow starts at person 1 and moves to the right each second.
    When it reaches either end of the line (person ``n`` or person 1),
    the direction reverses.

    Args:
        n: The total number of people standing in a line (n >= 1).
        time: The number of seconds that have elapsed (time >= 0).

    Returns:
        The 1‑based index of the person holding the pillow after ``time`` seconds.

    Examples:
        >>> solve(4, 5)
        2
        >>> solve(1, 100)
        1
    """
    if n == 1:
        return 1

    cycle_length = 2 * (n - 1)  # full back‑and‑forth cycle
    position_in_cycle = time % cycle_length

    if position_in_cycle < n:
        # moving forward direction
        return position_in_cycle + 1
    else:
        # moving backward direction
        return 2 * n - position_in_cycle - 1
