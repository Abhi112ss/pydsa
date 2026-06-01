METADATA = {
    "id": 841,
    "name": "Keys and Rooms",
    "slug": "keys-and-rooms",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "graph_traversal"],
    "difficulty": "medium",
    "time_complexity": "O(N + E)",
    "space_complexity": "O(N)",
    "description": "Determine if all rooms can be visited starting from room 0 using keys found in each room.",
}

def solve(rooms: list[list[int]]) -> bool:
    """
    Determines if all rooms in a building can be visited starting from room 0.

    Args:
        rooms: A list of lists where rooms[i] contains the keys found in room i.

    Returns:
        True if all rooms can be visited, False otherwise.

    Examples:
        >>> solve([[1], [2], [3], []])
        True
        >>> solve([[1, 3], [3, 0], [3], [0]])
        False
    """
    num_rooms = len(rooms)
    visited = set()
    # Use a stack for iterative Depth First Search (DFS)
    stack = [0]
    visited.add(0)

    while stack:
        current_room = stack.pop()
        
        # Explore all keys found in the current room
        for key in rooms[current_room]:
            if key not in visited:
                # If the key opens a room we haven't visited, mark it and add to stack
                visited.add(key)
                stack.append(key)

    # If the number of visited rooms equals the total number of rooms, return True
    return len(visited) == num_rooms
