METADATA = {
    "id": 1927,
    "name": "Sum Game",
    "slug": "sum_game",
    "category": "math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine the winner of the sum game based on parity of sums.",
}


def solve(num: str) -> str:
    """Determine the winner of the Sum Game.

    Args:
        num: A string consisting of digits and '?' characters, length is even.

    Returns:
        "Alice" if Alice can force a win, otherwise "Bob".

    Examples:
        >>> solve("25??")
        'Bob'
        >>> solve("?3295???")
        'Alice'
    """
    half_length: int = len(num) // 2

    left_sum: int = 0
    right_sum: int = 0
    left_q: int = 0
    right_q: int = 0

    # Count sums and question marks in each half
    for index, ch in enumerate(num):
        if index < half_length:
            if ch == "?":
                left_q += 1
            else:
                left_sum += int(ch)
        else:
            if ch == "?":
                right_q += 1
            else:
                right_sum += int(ch)

    # If the number of '?' is equal on both sides, equality of sums decides
    if left_q == right_q:
        return "Alice" if left_sum == right_sum else "Bob"

    # Otherwise, check the parity condition derived from optimal play
    diff: int = left_sum - right_sum
    # Alice wins iff diff * 2 equals 9 times the imbalance of '?' (right - left)
    if diff * 2 == 9 * (right_q - left_q):
        return "Alice"
    return "Bob"