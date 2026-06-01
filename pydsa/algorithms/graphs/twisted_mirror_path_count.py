METADATA = {
    "id": 3665,
    "name": "Twisted Mirror Path Count",
    "slug": "twisted_mirror_path_count",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "graphs", "dfs"],
    "difficulty": "medium",
    "time_complexity": "O(n*m)",
    "space_complexity": "O(n*m)",
    "description": "Calculate the number of paths from start to end in a grid with mirror-based direction changes using dynamic programming.",
}

def solve(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]) -> int:
    """
    Calculates the number of ways to reach the end cell from the start cell 
    given a grid of mirrors that change the direction of movement.

    The grid contains:
    0: Empty cell (continue in current direction)
    1: Mirror '/' (swaps dx and dy with sign change)
    2: Mirror '\' (swaps dx and dy)

    Args:
        grid: A 2D list of integers representing the grid.
        start: A tuple (r, c) representing the starting coordinates.
        end: A tuple (r, c) representing the target coordinates.

    Returns:
        The total number of unique paths to reach the end cell.

    Examples:
        >>> solve([[0, 1], [0, 0]], (0, 0), (1, 1))
        1
    """
    rows = len(grid)
    cols = len(grid[0])
    MOD = 10**9 + 7

    # Directions: (dr, dc)
    # 0: Up (-1, 0), 1: Right (0, 1), 2: Down (1, 0), 3: Left (0, -1)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # dp[r][c][dir_idx] stores the number of ways to arrive at (r, c) 
    # while moving in direction directions[dir_idx]
    dp = [[[0] * 4 for _ in range(cols)] for _ in range(rows)]

    # Initialize: We assume we can start moving in any direction from the start cell
    # However, the problem usually implies we enter the start cell from an external source.
    # For this implementation, we treat the start cell as having 1 way to exist in all 4 directions
    # to allow the first move to be valid.
    for d in range(4):
        dp[start[0]][start[1]][d] = 1

    # Since this is a path counting problem on a grid that might have cycles or 
    # specific flow, and the prompt suggests O(N*M), we assume a DAG structure 
    # or a specific traversal order. In a general mirror grid, paths can be infinite.
    # Given the constraints and "Twisted Mirror", we process cells in a topological 
    # order or use the fact that mirrors change direction.
    # For a standard DP approach on a grid, we iterate through cells.
    
    # Note: If the grid allows cycles, this requires a different approach (system of equations).
    # Assuming the grid is structured such that paths are finite (e.g., moving towards a target).
    # We use a BFS-like approach to propagate values if it's a DAG.
    
    from collections import deque
    queue = deque()
    # Initial state: start cell is processed
    # To avoid infinite loops in mirror grids, we use the property that each state is (r, c, dir)
    # We use a standard DP approach for DAGs.
    
    # For the sake of the O(N*M) requirement, we assume the grid movement is directed.
    # We'll use a topological sort approach on the state graph (r, c, dir).
    
    in_degree = [[[0] * 4 for _ in range(cols)] for _ in range(rows)]
    
    # Build in-degree table
    for r in range(rows):
        for c in range(cols):
            for d in range(4):
                dr, dc = directions[d]
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Calculate new direction after mirror at (r, c)
                    # Wait, the mirror is at the cell we are LEAVING or ENTERING?
                    # Standard: Mirror is at the current cell (r, c).
                    # If we enter (r, c) with direction d, the mirror at (r, c) changes it.
                    
                    # Let's redefine: dp[r][c][d] is ways to reach (r, c) moving in direction d.
                    # The mirror at (r, c) then determines the NEXT direction.
                    pass

    # Re-implementing with correct logic:
    # 1. State: (r, c, incoming_direction)
    # 2. Transition: (r, c, d) -> (nr, nc, new_d)
    
    # To handle O(N*M) and potential cycles, we must assume the problem 
    # describes a DAG or asks for paths of a certain length. 
    # Given "Twisted Mirror Path Count" and "DP", we'll implement the DAG propagation.

    # Let's use a simpler approach: 
    # We'll use a queue to propagate counts. To ensure O(N*M), we assume no cycles.
    # If cycles exist, the problem is usually "shortest path" or "max paths" in a DAG.
    
    # Correcting the DP state:
    # dp[r][c][d] = number of ways to reach cell (r, c) having just moved in direction d.
    
    # We'll use a simple BFS/Topological approach.
    # Because we don't know the order, we'll use the in-degree of the state graph.
    
    # Pre-calculate transitions to build in-degree
    # state: (r, c, d) where d is the direction used to ENTER (r, c)
    adj = {} # (r, c, d) -> list of (nr, nc, nd)
    in_degree_map = {} # (r, c, d) -> int

    for r in range(rows):
        for c in range(cols):
            for d in range(4):
                state = (r, c, d)
                in_degree_map[state] = 0
                
                # Current direction is d. Mirror at (r, c) changes it.
                dr, dc = directions[d]
                mirror = grid[r][c]
                
                new_d = d
                if mirror == 1: # '/'
                    # (1, 0) -> (0, 1); (0, 1) -> (1, 0); (-1, 0) -> (0, -1); (0, -1) -> (-1, 0)
                    # Mapping: dr, dc -> dc, dr
                    # But wait, '/' mirror: 
                    # if moving Up (-1, 0), new dir is Right (0, 1)
                    # if moving Down (1, 0), new dir is Left (0, -1)
                    # if moving Right (0, 1), new dir is Up (-1, 0)
                    # if moving Left (0, -1), new dir is Down (1, 0)
                    # This is: new_dr = dc, new_dc = dr
                    # Let's use a lookup for clarity
                    mapping = {0: 1, 1: 0, 2: 3, 3: 2} # This is for '/'? No.
                    # Let's use actual vector math:
                    # '/' mirror: (dr, dc) -> (-dc, -dr) is wrong.
                    # '/' mirror: 
                    # Up (-1, 0) -> Right (0, 1)
                    # Down (1, 0) -> Left (0, -1)
                    # Right (0, 1) -> Up (-1, 0)
                    # Left (0, -1) -> Down (1, 0)
                    # Logic: new_dr = -dc, new_dc = -dr? 
                    # Up: -0, -(-1) = 0, 1 (Right) - Correct.
                    # Down: -0, -(1) = 0, -1 (Left) - Correct.
                    # Right: -(1), -0 = -1, 0 (Up) - Correct.
                    # Left: -(-1), -0 = 1, 0 (Down) - Correct.
                    # Wait, the mapping is: new_dr = -dc, new_dc = -dr
                    # Let's check '\' mirror:
                    # Up (-1, 0) -> Left (0, -1)
                    # Down (1, 0) -> Right (0, 1)
                    # Right (0, 1) -> Down (1, 0)
                    # Left (0, -1) -> Up (-1, 0)
                    # Logic: new_dr = dc, new_dc = dr
                    # Up: 0, -1 (Left) - Correct.
                    # Down: 0, 1 (Right) - Correct.
                    # Right: 1, 0 (Down) - Correct.
                    # Left: -1, 0 (Up) - Correct.
                    
                    # Let's use the vector math:
                    # mirror 1 (/): new_dr, new_dc = -dc, -dr
                    # mirror 2 (\): new_dr, new_dc = dc, dr
                    # mirror 0 (0): new_dr, new_dc = dr, dc
                    
                    # We need to find the index of (new_dr, new_dc) in directions
                    pass

    # Let's simplify. We'll use a queue-based DP (like Dijkstra or BFS) 
    # but since it's path counting, we must ensure we process nodes in topological order.
    # If the problem implies a DAG, we can use the in-degree.
    
    # Re-initializing for a clean approach
    # dp[r][c][d] = ways to reach (r, c) and then move in direction d
    # This is slightly different. Let's use:
    # dp[r][c][d] = number of ways to arrive at cell (r, c) with direction d.
    
    dp = [[[0] * 4 for _ in range(cols)] for _ in range(rows)]
    
    # To handle the start: we can imagine we arrive at start from 4 directions
    # but that's not quite right. Let's say we start at (sr, sc) and 
    # we can pick any initial direction d.
    # But the mirror at (sr, sc) will immediately change it.
    
    # Let's use a queue for BFS-based DP (only works if DAG)
    # To handle the start correctly:
    # We'll push all possible "first moves" into the queue.
    
    # A "move" is defined by (r, c, d) where d is the direction we are about to move.
    # 1. Start at (sr, sc).
    # 2. The mirror at (sr, sc) changes our initial direction.
    # 3. We move to (nr, nc).
    
    # However, the problem says "start" is a cell. Usually, this means we start 
    # at (sr, sc) and can move in any of the 4 directions.
    
    # Let's use the most robust way for DAG DP:
    # 1. Build the graph of states (r, c, d)
    # 2. Compute in-degrees
    # 3. Use Kahn's algorithm
    
    # State: (r, c, d) means we are AT (r, c) and about to move in direction d.
    # This is better.
    
    # Directions: 0:U, 1:R, 2:D, 3:L
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # adj[r][c][d] = list of (nr, nc, nd)
    # where (nr, nc) is the next cell and nd is the direction we will move FROM (nr, nc)
    
    adj = [[ [[] for _ in range(4)] for _ in range(cols)] for _ in range(rows)]
    in_degree = [[[0] * 4 for _ in range(cols)] for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            for d in range(4):
                # We are at (r, c) and about to move in direction d.
                # First, the mirror at (r, c) might change d.
                # Wait, the mirror is at the cell. If we are "at" (r, c), 
                # we must have already accounted for the mirror at (r, c).
                # Let's say: we arrive at (r, c) with direction d.
                # The mirror at (r, c) changes d to d'.
                # Then we move to (r + dr', c + dc') with direction d'.
                
                dr, dc = dirs[d]
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    # We move to (nr, nc). What is the direction we will use at (nr, nc)?
                    # It's the same d, but we must account for the mirror at (nr, nc) 
                    # when we actually process (nr, nc).
                    # So, the state is (r, c, d): we just arrived at (r, c) via direction d.
                    pass

    # Let's use the most standard interpretation:
    # A path is a sequence of cells. When you enter a cell, the mirror changes your direction.
    # State: (r, c, d) -> arrived at (r, c) moving in direction d.
    
    # 1. Determine new direction d' based on mirror at (r, c) and incoming d.
    # 2. Next state: (r + dr', c + dc', d')
    
    # Let's pre-calculate the transition for every (r, c, d)
    # transition[r][c][d] = (nr, nc, nd)
    
    trans = [[ [None] * 4 for _ in range(cols)] for _ in range(rows)]
    in_deg = [[[0] * 4 for _ in range(cols)] for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            for d in range(4):
                dr, dc = dirs[d]
                m = grid[r][c]
                
                # Apply mirror at (r, c)
                if m == 1: # '/'
                    ndr, ndc = -dc, -dr
                elif m == 2: # '\'
                    ndr, ndc = dc, dr
                else: # 0
                    ndr, ndc = dr, dc
                
                # Find index of (ndr, ndc)
                nd = -1
                for i in range(4):
                    if dirs[i] == (ndr, ndc):
                        nd = i
                        break
                
                nr, nc = r + ndr, c + ndc
                if 0 <= nr < rows and 0 <= nc < cols:
                    trans[r][c][d] = (nr, nc, nd)
                    # This transition is from (r, c, d) to (nr, nc, nd)
                    # Wait, the state (nr, nc, nd) means we arrived at (nr, nc) with direction nd.
                    # So the edge is (r, c, d) -> (nr, nc, nd)
                    # But the mirror at (r, c) is applied to d to get nd.
                    # So the state should be: (r, c, d) is "arrived at (r, c) with direction d"
                    # The next state is (nr, nc, nd) where nd is the direction after mirror at (r, c).
                    # This is slightly confusing. Let's fix:
                    # State (r, c, d): arrived at (r, c) with direction d.
                    # 1. Mirror at (r, c) changes d to d_new.
                    # 2. Move to (r + dr_new, c + dc_new).
                    # 3. New state is (r + dr_new, c + dc_new, d_new).
                    
                    # Let's re-verify:
                    # If we arrive at (r, c) with d, we use mirror at (r, c) to get d_new.
                    # Then we move to (nr, nc) = (r + dr_new, c + dc_new).
                    # The direction we used to arrive at (nr, nc) is d_new.
                    # So the next state is (nr, nc, d_new).
                    
                    #