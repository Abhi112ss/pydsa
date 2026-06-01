METADATA = {
    "id": 3147,
    "name": "Taking Maximum Energy From the Mystic Dungeon",
    "slug": "taking-maximum-energy-from-the-mystic-dungeon",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["graphs", "dfs", "dp"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum energy collected by traversing a dungeon from start to end using dynamic programming.",
}

def solve(energy: list[int], rooms: list[list[int]]) -> int:
    """
    Calculates the maximum energy that can be collected from the start to the end of the dungeon.

    The player starts at room 0 and must reach the last room. Each room has an energy value
    and a list of possible next rooms. If a player reaches a room with negative energy,
    the total energy becomes 0.

    Args:
        energy: A list of integers representing the energy in each room.
        rooms: A list of lists where rooms[i] contains the indices of rooms reachable from room i.

    Returns:
        The maximum energy collected upon reaching the last room.

    Examples:
        >>> solve([1, -2, 5], [[1], [2], []])
        4
        >>> solve([1, -2, 5], [[1], [], [2]])
        0
    """
    n = len(energy)
    # dp[i] stores the maximum energy that can be collected starting from room i to the end.
    # Initialize with a very small number to represent unvisited/unreachable states.
    dp = [-float('inf')] * n
    
    # Base case: The energy at the last room is just the energy of the last room itself.
    # However, if the last room's energy is negative, the player's energy effectively becomes 0.
    dp[n - 1] = max(0, energy[n - 1])

    # Iterate backwards from the second to last room to the first room.
    # This ensures that when we calculate dp[i], all possible next rooms dp[j] are already computed.
    for i in range(n - 2, -1, -1):
        max_next_energy = -float('inf')
        
        # Check all possible rooms reachable from the current room i.
        for next_room in rooms[i]:
            if dp[next_room] > max_next_energy:
                max_next_energy = dp[next_room]
        
        # If the current room can reach the end, calculate the energy.
        # If max_next_energy is -inf, it means the end is unreachable from this path.
        if max_next_energy != -float('inf'):
            # The energy at room i is the current room's energy plus the best energy from next rooms.
            # If the sum is negative, the player's energy becomes 0.
            dp[i] = max(0, energy[i] + max_next_energy)

    # The result is the maximum energy starting from room 0.
    # If room 0 cannot reach the end, the problem implies we return 0 or handle it via the DP.
    # Based on problem constraints, if dp[0] is still -inf, it means no path exists.
    return int(dp[0]) if dp[0] != -float('inf') else 0
