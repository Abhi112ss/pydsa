METADATA = {
    "id": 2410,
    "name": "Maximum Matching of Players With Trainers",
    "slug": "maximum-matching-of-players-with-trainers",
    "category": "Greedy",
    "aliases": [],
    "tags": ["two_pointer", "greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n + m log m)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of players that can be matched with trainers such that each player's skill is less than or equal to the trainer's capacity.",
}

def solve(players: list[int], trainers: list[int]) -> int:
    """
    Finds the maximum number of players that can be matched with trainers.

    The strategy uses a greedy approach: sort both arrays and use two pointers
    to match the smallest available player with the smallest possible trainer
    that meets their skill requirement.

    Args:
        players: A list of integers representing the skill levels of players.
        trainers: A list of integers representing the capacities of trainers.

    Returns:
        The maximum number of players that can be matched with trainers.

    Examples:
        >>> solve([4, 7, 9], [8, 2, 5, 8])
        2
        >>> solve([1, 1], [1, 1])
        2
    """
    # Sort both arrays to enable the greedy two-pointer approach
    players.sort()
    trainers.sort()

    player_index = 0
    trainer_index = 0
    matches_count = 0

    # Iterate through both lists using two pointers
    while player_index < len(players) and trainer_index < len(trainers):
        # If the current trainer can accommodate the current player
        if players[player_index] <= trainers[trainer_index]:
            matches_count += 1
            # Move to the next player since this one is matched
            player_index += 1
            # Move to the next trainer since this one is used
            trainer_index += 1
        else:
            # Current trainer is too weak for the current player, 
            # try the next (larger) trainer
            trainer_index += 1

    return matches_count
