METADATA = {
    "id": 950,
    "name": "Reveal Cards In Increasing Order",
    "slug": "reveal-cards-in-increasing-order",
    "category": "Simulation",
    "aliases": [],
    "tags": ["queue", "simulation", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Arrange cards in an array such that when revealed in a specific pattern, they appear in increasing order.",
}

from collections import deque

def solve(deck: list[int]) -> list[int]:
    """
    Arranges the cards in an array such that following the reveal process 
    results in the cards being in increasing order.

    The reveal process is:
    1. Take the top card and reveal it.
    2. Take the next top card and move it to the bottom of the deck.

    Args:
        deck: A list of integers representing the cards.

    Returns:
        A list of integers representing the optimal initial arrangement.

    Examples:
        >>> solve([17,13,10,2,5])
        [2, 13, 5, 17, 10]
        >>> solve([7,7,7,7])
        [7, 7, 7, 7]
    """
    n = len(deck)
    if n == 0:
        return []

    # Sort the deck to know the order in which cards must be revealed
    sorted_deck = sorted(deck)
    
    # We use a queue to simulate the indices of the result array.
    # This allows us to map the sorted cards to the correct positions 
    # by mimicking the "reveal and move to back" process.
    index_queue = deque(range(n))
    result = [0] * n

    for card in sorted_deck:
        # 1. The first available index in the queue is where the current 
        # smallest card must go (the "reveal" step).
        target_index = index_queue.popleft()
        result[target_index] = card
        
        # 2. If there are still indices left, the next index in the queue 
        # is moved to the back (the "move to bottom" step).
        if index_queue:
            index_queue.append(index_queue.popleft())

    return result
