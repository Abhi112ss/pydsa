METADATA = {
    "id": 1921,
    "name": "Eliminate Maximum Number of Monsters",
    "slug": "eliminate-maximum-number-of-monsters",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "priority_queue", "heap"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Determine the maximum number of monsters you can eliminate by attacking one monster per second before they reach your position.",
}

import heapq

def solve(position: int, monsters: list[int]) -> int:
    """
    Calculates the maximum number of monsters that can be eliminated.

    The strategy is to always attack the monster that is closest to reaching 
    the position (the one with the smallest time value). We use a min-heap 
    to efficiently retrieve the monster with the minimum time.

    Args:
        position: The current position of the player.
        monsters: A list of integers representing the positions of the monsters.

    Returns:
        The maximum number of monsters that can be eliminated.

    Examples:
        >>> solve(10, [1, 5, 10])
        2
        >>> solve(10, [1, 2, 3])
        3
        >>> solve(10, [1, 1, 1])
        3
    """
    # Calculate the time it takes for each monster to reach the player
    # time_to_reach = position - monster_position
    arrival_times = []
    for monster_pos in monsters:
        arrival_times.append(position - monster_pos)

    # Use a min-heap to always target the monster arriving soonest
    heapq.heapify(arrival_times)

    seconds_passed = 0
    monsters_eliminated = 0

    while arrival_times:
        # The monster that will reach us earliest
        earliest_arrival = heapq.heappop(arrival_times)

        # If the monster reaches us before or at the current time, we lose
        if earliest_arrival <= seconds_passed:
            break

        # Otherwise, we successfully eliminate this monster
        monsters_eliminated += 1
        seconds_passed += 1

    return monsters_eliminated
