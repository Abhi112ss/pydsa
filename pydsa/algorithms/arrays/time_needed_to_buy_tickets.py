METADATA = {
    "id": 2073,
    "name": "Time Needed to Buy Tickets",
    "slug": "time-needed-to-buy-tickets",
    "category": "Simulation",
    "aliases": [],
    "tags": ["simulation", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the total time required for a specific person to finish buying their tickets in a circular queue.",
}

def solve(tickets: list[int], k: int) -> int:
    """
    Calculates the total time needed for the person at index k to finish buying all their tickets.

    The process follows a circular queue: each person buys one ticket per round.
    If a person reaches their required ticket count, they leave the queue.

    Args:
        tickets: A list of integers where tickets[i] is the number of tickets person i needs.
        k: The index of the target person.

    Returns:
        The total number of time units (tickets sold) until person k has 0 tickets left.

    Examples:
        >>> solve([2, 3, 2], 2)
        5
        >>> solve([5], 0)
        5
        >>> solve([2, 3, 5, 1, 2], 4)
        12
    """
    total_time = 0
    target_tickets = tickets[k]
    n = len(tickets)

    for i in range(n):
        # If the person is at or before the target person in the queue
        if i <= k:
            # They will buy at most target_tickets, or all their own tickets if fewer
            total_time += min(tickets[i], target_tickets)
        else:
            # If the person is after the target person, they will buy at most 
            # (target_tickets - 1) because the target person finishes and the 
            # process stops before this person's next turn in the final round.
            total_time += min(tickets[i], target_tickets - 1)

    return total_time
