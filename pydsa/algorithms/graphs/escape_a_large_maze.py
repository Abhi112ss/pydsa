METADATA = {
    "id": 1036,
    "name": "Escape a Large Maze",
    "slug": "escape-a-large-maze",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "dfs", "matrix", "boundary"],
    "difficulty": "hard",
    "time_complexity": "O(b^2)",
    "space_complexity": "O(b^2)",
    "description": "Determine if a ball can escape a large maze containing a limited number of blocks.",
}

from collections import deque


def solve(blocked: list[list[int]], source: list[int], target: list[int]) -> bool:
    """
    Determines if a ball can escape a large maze given a set of blocked cells.

    The maze is effectively infinite, but the number of blocks is small.
    The ball can escape if and only if both the source and the target are 
    not enclosed by the blocks.

    Args:
        blocked: A list of [row, col] coordinates representing blocked cells.
        source: The starting [row, col] coordinate.
        target: The destination [row, col] coordinate.

    Returns:
        True if the target is reachable from the source, False otherwise.

    Examples:
        >>> solve([[1, 1], [1, 2], [1, 3], [2, 1], [3, 1]], [0, 0], [2, 2])
        False
        >>> solve([[1, 1], [1, 2], [1, 3], [2, 1], [3, 1]], [0, 0], [4, 4])
        True
    """
    blocked_set = {tuple(b) for b in blocked}
    
    # The maximum area a set of 'b' blocks can enclose is roughly (b+1)^2.
    # If the ball travels further than this, it is definitely not trapped.
    MAX_BOUND = len(blocked) + 2

    def is_trapped(start: tuple[int, int], goal: tuple[int, int]) -> bool:
        """
        Checks if the 'start' point is trapped within the blocks.
        If 'goal' is reached during BFS, it's not trapped (or at least reachable).
        """
        visited = {start}
        queue = deque([start])
        
        while queue:
            curr_r, curr_c = queue.popleft()
            
            # If we reach the target, it's not trapped in a way that prevents escape
            if (curr_r, curr_c) == goal:
                return False
            
            # If we move beyond the potential enclosure area, we are free
            if abs(curr_r) > MAX_BOUND or abs(curr_c) > MAX_BOUND:
                return False
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = curr_r + dr, curr_c + dc
                
                if (nr, nc) not in blocked_set and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        
        # If queue empties and we haven't escaped the boundary or hit goal, we are trapped
        return True

    # The ball can reach the target if and only if:
    # 1. The source is not trapped by blocks.
    # 2. The target is not trapped by blocks.
    # Note: We check if the source can reach the target OR escape the boundary.
    # However, the logic is simpler: if source can reach target, return True.
    # If source can reach the boundary, it's not trapped. 
    # If target is also not trapped, then source can reach target.
    
    # We use a modified BFS to see if source can reach target OR escape the boundary.
    def can_reach_target_or_escape(start: tuple[int, int], goal: tuple[int, int]) -> bool:
        visited = {start}
        queue = deque([start])
        
        while queue:
            curr_r, curr_c = queue.popleft()
            
            if (curr_r, curr_c) == goal:
                return True
            
            # If we escape the boundary, we are no longer trapped
            if abs(curr_r) > MAX_BOUND or abs(curr_c) > MAX_BOUND:
                return True
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = curr_r + dr, curr_c + dc
                if (nr, nc) not in blocked_set and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        return False

    # Step 1: Check if source can reach target or escape.
    # Step 2: Check if target can reach source or escape.
    # Actually, the condition is: source can reach target OR source can escape AND target can escape.
    # But if source can escape, it can reach any point that is also not trapped.
    # The most robust way:
    # 1. Can source reach target? (If yes, True)
    # 2. Can source reach boundary? (If no, False)
    # 3. Can target reach boundary? (If no, False)
    # 4. Otherwise, True.
    
    # Let's simplify:
    # If source can reach target, return True.
    # If source can reach boundary, check if target can reach boundary.
    
    # Check if source can reach target
    # We need a BFS that specifically looks for target OR boundary
    
    def bfs_check(start: tuple[int, int], target_node: tuple[int, int]) -> bool:
        visited = {start}
        queue = deque([start])
        while queue:
            r, c = queue.popleft()
            if (r, c) == target_node:
                return True
            if abs(r) > MAX_BOUND or abs(c) > MAX_BOUND:
                return True
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in blocked_set and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        return False

    # If source can reach target, it's True.
    # If source can reach boundary, we still need to ensure target isn't trapped.
    # If target can reach boundary, then they can both reach the "infinite" area.
    
    # Correct logic:
    # If source can reach target, return True.
    # If source can reach boundary AND target can reach boundary, return True.
    # Else return False.
    
    # However, if source can reach target, it's already covered by the "can reach target" check.
    # But the "can reach target" check might fail if target is inside a trap, 
    # even if source is outside.
    
    # Let's use the property: 
    # If source can reach target, return True.
    # If source can reach boundary, check if target can reach boundary.
    
    # Re-implementing BFS to be more specific:
    def can_reach(start: tuple[int, int], end: tuple[int, int]) -> bool:
        # This BFS returns True if start can reach end OR start can reach boundary
        visited = {start}
        queue = deque([start])
        while queue:
            r, c = queue.popleft()
            if (r, c) == end: return True
            if abs(r) > MAX_BOUND or abs(c) > MAX_BOUND: return True
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in blocked_set and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        return False

    # If source can reach target, return True.
    # If source can reach boundary, we must check if target can reach boundary.
    # If source cannot reach target AND cannot reach boundary, it's trapped.
    # If source can reach boundary, but target is trapped, return False.
    
    # Check if source can reach target
    # We need a BFS that ONLY returns True if target is reached.
    def reach_target_only(start: tuple[int, int], end: tuple[int, int]) -> bool:
        visited = {start}
        queue = deque([start])
        while queue:
            r, c = queue.popleft()
            if (r, c) == end: return True
            if abs(r) > MAX_BOUND or abs(c) > MAX_BOUND: return False
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in blocked_set and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        return False

    # Check if source can reach boundary
    def reach_boundary_only(start: tuple[int, int]) -> bool:
        visited = {start}
        queue = deque([start])
        while queue:
            r, c = queue.popleft()
            if abs(r) > MAX_BOUND or abs(c) > MAX_BOUND: return True
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in blocked_set and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        return False

    # Final Logic:
    # 1. If source can reach target, return True.
    # 2. If source can reach boundary AND target can reach boundary, return True.
    # 3. Otherwise, return False.
    
    # Optimization: If source can reach target, it's True.
    # If not, check if source can reach boundary. If it can, check if target can reach boundary.
    
    # We can combine this:
    # If source can reach target, return True.
    # If source can reach boundary, check if target can reach boundary.
    
    # Let's use the 'can_reach' function which checks for target OR boundary.
    # If can_reach(source, target) is True, it means we either hit target or escaped.
    # If we hit target, return True.
    # If we escaped, we still need to check if target is also not trapped.
    
    # Corrected logic:
    # 1. Can source reach target? If yes, return True.
    # 2. Can source reach boundary? If no, return False.
    # 3. Can target reach boundary? If yes, return True.
    # 4. Else, return False.

    # To avoid redundant BFS, we can check if source can reach target.
    # If it can, return True.
    # If it can't, it's either because target is trapped or source is trapped.
    # If source is trapped, it can't reach boundary.
    # If target is trapped, it can't reach boundary.
    
    # Let's use a single BFS for source to see if it hits target or boundary.
    # If it hits target, return True.
    # If it hits boundary, we then check if target can hit boundary.
    
    # Re-run BFS for source
    visited_source = {tuple(source)}
    queue_source = deque([tuple(source)])
    source_hit_target = False
    source_hit_boundary = False
    
    while queue_source:
        r, c = queue_source.popleft()
        if (r, c) == tuple(target):
            source_hit_target = True
            break
        if abs(r) > MAX_BOUND or abs(c) > MAX_BOUND:
            source_hit_boundary = True
            break
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) not in blocked_set and (nr, nc) not in visited_source:
                visited_source.add((nr, nc))
                queue_source.append((nr, nc))
                
    if source_hit_target:
        return True
    if not source_hit_boundary:
        return False
    
    # If source hit boundary, check if target can hit boundary
    visited_target = {tuple(target)}
    queue_target = deque([tuple(target)])
    while queue_target:
        r, c = queue_target.popleft()
        if abs(r) > MAX_BOUND or abs(c) > MAX_BOUND:
            return True
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) not in blocked_set and (nr, nc) not in visited_target:
                visited_target.add((nr, nc))
                queue_target.append((nr, nc))
                
    return False
