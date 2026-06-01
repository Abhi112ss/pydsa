METADATA = {
    "id": 789,
    "name": "Escape The Ghosts",
    "slug": "escape-the-ghosts",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "geometry"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a player can reach a target coordinate before any ghost reaches it using Manhattan distance.",
}

def solve(x: int, y: int, target_x: int, target_y: int, ghosts: list[list[int]]) -> bool:
    """
    Determines if the player can reach the target before any ghost.

    The player escapes if their Manhattan distance to the target is strictly 
    less than the Manhattan distance of every ghost to the target.

    Args:
        x: The starting x-coordinate of the player.
        y: The starting y-coordinate of the player.
        target_x: The x-coordinate of the target.
        target_y: The y-coordinate of the target.
        ghosts: A list of [gx, gy] coordinates representing ghost positions.

    Returns:
        True if the player can escape, False otherwise.

    Examples:
        >>> solve(1, 0, 2, 2, [[1, 1]])
        False
        >>> solve(1, 0, 2, 2, [[2, 1]])
        True
    """
    # Calculate Manhattan distance for the player to the target
    # Manhattan distance = |x1 - x2| + |y1 - y2|
    player_distance = abs(x - target_x) + abs(y - target_y)

    # Iterate through each ghost to find the minimum distance any ghost has to the target
    for ghost_x, ghost_y in ghosts:
        ghost_distance = abs(ghost_x - target_x) + abs(ghost_y - target_y)
        
        # If any ghost can reach the target at the same time or before the player,
        # the player cannot escape.
        if ghost_distance <= player_distance:
            return False

    return True
