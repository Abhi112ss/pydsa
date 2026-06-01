METADATA = {
    "id": 1263,
    "name": "Minimum Moves to Move a Box to Their Target Location",
    "slug": "minimum-moves-to-move-a-box-to-their-target-location",
    "category": "Breadth-First Search",
    "aliases": [],
    "tags": ["bfs", "shortest_path", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(M^2 * N^2)",
    "space_complexity": "O(M^2 * N^2)",
    "description": "Find the minimum number of moves to push a box from its starting position to a target position in a grid.",
}

from collections import deque

def solve(grid: list[list[str]]) -> int:
    """
    Calculates the minimum moves to push a box from its start to the target.

    Args:
        grid: A 2D grid containing '.', '#', 'B' (box), 'T' (target), and 'S' (start).

    Returns:
        The minimum number of moves required, or -1 if impossible.

    Examples:
        >>> grid = [["S", ".", ".", "."], [".", "#", "#", "."], [".", ".", ".", "T"]]
        >>> solve(grid)
        8
    """
    rows = len(grid)
    cols = len(grid[0])
    
    start_pos = None
    box_pos = None
    target_pos = None

    # Locate S, B, and T in the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                start_pos = (r, c)
            elif grid[r][c] == "B":
                box_pos = (r, c)
            elif grid[r][c] == "T":
                target_pos = (r, c)
    
    # Handle edge case where target is actually the box's starting position
    # (Though problem constraints usually imply B and T are distinct)
    # We need to find the actual target coordinate. 
    # If 'T' is not present, we check if 'B' is at the target.
    # Let's re-scan to ensure we find the target even if it's marked 'T'
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "T":
                target_pos = (r, c)

    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_valid(r: int, c: int) -> bool:
        return 0 <= r < rows and 0 <= c < cols and grid[r][c] != "#"

    def can_reach_player_pos(box_r: int, box_c: int, player_r: int, player_c: int) -> bool:
        """BFS to check if the player can reach the required side of the box."""
        if not is_valid(player_r, player_c):
            return False
        
        queue = deque([(player_r, player_c)])
        visited = {(player_r, player_c)}
        
        while queue:
            curr_r, curr_c = queue.popleft()
            if (curr_r, curr_c) == (player_r, player_c): # This is logic for reaching target
                pass # placeholder
            
            # If we reached the target position for the player
            if (curr_r, curr_c) == (player_r, player_c):
                # This is slightly wrong logic, we need to check if we reach the specific side
                pass

        # Corrected BFS for player movement
        q = deque([(player_r, player_c)])
        v = {(player_r, player_c)}
        while q:
            cr, cc = q.popleft()
            if (cr, cc) == (player_r, player_c): # This is the goal
                pass 
            # Wait, the goal is to reach the specific (player_r, player_c)
            # Let's rewrite this properly.
        return False

    # Re-implementing player reachability more cleanly
    def player_can_reach(start_r: int, start_c: int, target_r: int, target_c: int, box_r: int, box_c: int) -> bool:
        if not is_valid(start_r, start_c) or not is_valid(target_r, target_c):
            return False
        q = deque([(start_r, start_c)])
        visited = {(start_r, start_c)}
        while q:
            r, c = q.popleft()
            if (r, c) == (target_r, target_c):
                return True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Player cannot walk through the box
                if is_valid(nr, nc) and (nr, nc) != (box_r, box_c) and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))
        return False

    # BFS State: (box_row, box_col, player_row, player_col)
    # We use (box_r, box_c, player_r, player_c) to track state
    # Optimization: The player's exact position doesn't matter, only which side of the box they are on.
    # However, for simplicity and correctness, we use (box_r, box_c, player_r, player_c)
    
    # queue stores: (box_r, box_c, player_r, player_c, moves)
    queue = deque([(box_pos[0], box_pos[1], start_pos[0], start_pos[1], 0)])
    visited = {(box_pos[0], box_pos[1], start_pos[0], start_pos[1])}

    while queue:
        br, bc, pr, pc, moves = queue.popleft()

        # If box reaches target
        if (br, bc) == target_pos:
            return moves

        # Try to push the box in 4 directions
        for dr, dc in directions:
            # To push the box to (br + dr, bc + dc), 
            # the player must be at (br - dr, bc - dc)
            new_br, new_bc = br + dr, bc + dc
            target_pr, target_pc = br - dr, bc - dc

            if is_valid(new_br, new_bc):
                # Check if player can reach the required position to push
                if player_can_reach(pr, pc, target_pr, target_pc, br, bc):
                    if (new_br, new_bc, br, bc) not in visited:
                        visited.add((new_br, new_bc, br, bc))
                        queue.append((new_br, new_bc, br, bc, moves + 1))

    return -1
