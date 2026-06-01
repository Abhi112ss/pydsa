METADATA = {
    "id": 390,
    "name": "Elimination Game",
    "slug": "elimination-game",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "simulation", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the last remaining number in a sequence after repeated elimination from left and right alternatingly.",
}

def solve(n: int) -> int:
    """
    Finds the last remaining number in a sequence from 1 to n after alternating 
    eliminations from the left and right.

    Args:
        n: The upper bound of the initial sequence [1, 2, ..., n].

    Returns:
        The last remaining number in the sequence.

    Examples:
        >>> solve(9)
        6
        >>> solve(1)
        1
        >>> solve(10)
        2
    """
    # head represents the first element of the current sequence.
    # step represents the distance between elements in the current sequence.
    # remaining represents the count of elements left in the sequence.
    head = 1
    step = 1
    remaining = n
    left_to_right = True

    while remaining > 1:
        # We update the head if:
        # 1. We are moving from left to right (the first element is always removed).
        # 2. We are moving from right to left AND the number of elements is odd 
        #    (the first element is also removed in this case).
        if left_to_right or (remaining % 2 == 1):
            head += step

        # After each pass, the number of elements is halved.
        remaining //= 2
        # The distance between elements doubles each round.
        step *= 2
        # Alternate the direction for the next round.
        left_to_right = not left_to_right

    return head
