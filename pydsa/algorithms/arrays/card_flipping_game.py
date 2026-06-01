METADATA = {
    "id": 822,
    "name": "Card Flipping Game",
    "slug": "card-flipping-game",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_set", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number that appears on only one side of any card.",
}

def solve(cards: list[list[int]]) -> int:
    """
    Finds the minimum number that appears on only one side of any card.

    A number is disqualified if it appears on both sides of the same card.
    The goal is to find the smallest number among those that are not disqualified.

    Args:
        cards: A list of lists, where each inner list represents a card with two numbers.

    Returns:
        The minimum number that is not disqualified.

    Examples:
        >>> solve([[1, 2], [2, 3], [3, 4]])
        1
        >>> solve([[1, 1], [2, 2]])
        -1
        >>> solve([[1, 2], [1, 3], [2, 3]])
        -1
    """
    disqualified = set()
    candidates = set()

    for card in cards:
        side_a = card[0]
        side_b = card[1]

        if side_a == side_b:
            # If both sides are the same, this number is disqualified
            disqualified.add(side_a)
        else:
            # If sides are different, both are potential candidates
            # unless they were previously marked as disqualified
            candidates.add(side_a)
            candidates.add(side_b)

    # A number is truly a candidate only if it was never disqualified
    # by being on both sides of any single card.
    valid_numbers = []
    for num in candidates:
        if num not in disqualified:
            valid_numbers.append(num)

    # Return the minimum valid number, or -1 if no valid numbers exist
    return min(valid_numbers) if valid_numbers else -1
