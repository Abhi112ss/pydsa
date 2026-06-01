METADATA = {
    "id": 846,
    "name": "Hand of Straights",
    "slug": "hand-of-straights",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Determine if a hand of cards can be rearranged into groups of a specific size where each group consists of consecutive cards.",
}

def solve(hand: list[int], group_size: int) -> bool:
    """
    Determines if the hand of cards can be rearranged into groups of consecutive cards.

    Args:
        hand: A list of integers representing the cards in hand.
        group_size: The required size of each consecutive group.

    Returns:
        True if the hand can be partitioned into valid groups, False otherwise.

    Examples:
        >>> solve([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)
        True
        >>> solve([1, 2, 3, 4], 3)
        False
    """
    # If the total number of cards is not divisible by group_size, it's impossible
    if len(hand) % group_size != 0:
        return False

    # Create a frequency map of the cards
    card_counts: dict[int, int] = {}
    for card in hand:
        card_counts[card] = card_counts.get(card, 0) + 1

    # Sort the unique cards to always start forming groups from the smallest available card
    sorted_unique_cards = sorted(card_counts.keys())

    for card in sorted_unique_cards:
        count = card_counts[card]
        
        # If this card has already been used up by previous groups, skip it
        if count > 0:
            # Every instance of the current smallest card must start a group 
            # or be part of a group starting from a smaller card.
            # Since we process from smallest to largest, this card MUST be the start 
            # of 'count' number of groups.
            for i in range(group_size):
                current_card = card + i
                
                # If the required consecutive card is not available or doesn't have enough count
                if card_counts.get(current_card, 0) < count:
                    return False
                
                # Deduct the count used by these groups
                card_counts[current_card] -= count

    return True
