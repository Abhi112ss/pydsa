METADATA = {
    "id": 1496,
    "name": "Path Crossing",
    "slug": "path-crossing",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash table", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if a path defined by a sequence of moves crosses itself by tracking visited coordinates in a hash set.",
}

def solve(moves: list[str]) -> bool:
    """
    Determines if the path described by the moves crosses itself.

    Args:
        moves: A list of strings where each string is 'N', 'S', 'E', or 'W'.

    Returns:
        True if the path crosses itself, False otherwise.

    Examples:
        >>> solve(["N", "S"])
        True
        >>> solve(["N", "E", "S", "W"])
        True
        >>> solve(["N", "E", "W"])
        True
        >>> solve(["N", "E", "S"])
        False
    """
    # Current position starting at the origin
    current_x, current_y = 0, 0
    
    # Use a set to store visited coordinates for O(1) average lookup
    # We store them as tuples (x, y) which are hashable
    visited_coordinates = {(current_x, current_y)}

    # Mapping directions to coordinate changes
    direction_map = {
        "N": (0, 1),
        "S": (0, -1),
        "E": (1, 0),
        "W": (-1, 0)
    }

    for move in moves:
        dx, dy = direction_map[move]
        current_x += dx
        current_y += dy

        # If the new coordinate is already in the set, the path has crossed
        if (current_x, current_y) in visited_coordinates:
            return True
        
        # Otherwise, add the new coordinate to the set of visited locations
        visited_coordinates.add((current_x, current_y))

    return False
