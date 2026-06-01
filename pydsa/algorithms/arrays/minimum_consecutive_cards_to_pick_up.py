METADATA = {
    "id": 2260,
    "name": "Minimum Consecutive Cards to Pick Up",
    "slug": "minimum-consecutive-cards-to-pick-up",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "two_pointer", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of consecutive cards to pick up such that two cards with the same value are included.",
}

def solve(cards: list[int]) -> int:
    """
    Finds the minimum number of consecutive cards to pick up to get two cards of the same value.

    Args:
        cards: A list of integers representing the values on the cards.

    Returns:
        The minimum number of consecutive cards required. Returns -1 if no two cards 
        have the same value.

    Examples:
        >>> solve([8, 5, 2, 5, 3])
        4
        >>> solve([3, 4, 5, 3, 4, 5])
        4
        >>> solve([1, 2, 3, 4, 5])
        -1
    """
    # Map to store the most recent index encountered for each card value
    last_seen_index: dict[int, int] = {}
    
    # Initialize min_distance with a value larger than any possible result
    min_distance = float('inf')

    for current_index, card_value in enumerate(cards):
        if card_value in last_seen_index:
            # Calculate the distance between the current card and its previous occurrence
            # The number of cards picked up is (current_index - previous_index + 1)
            distance = current_index - last_seen_index[card_value] + 1
            if distance < min_distance:
                min_distance = distance
        
        # Update the map with the current index for future occurrences of this card
        last_seen_index[card_value] = current_index

    # If min_distance was never updated, no duplicates were found
    return int(min_distance) if min_distance != float('inf') else -1
