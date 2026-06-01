METADATA = {
    "id": 2258,
    "name": "Escape the Spreading Fire",
    "slug": "escape-the-spreading-fire",
    "category": "Medium",
    "aliases": [],
    "tags": ["binary_search", "bfs", "matrix", "shortest_path"],
    "difficulty": "hard",
    "time_complexity": "O(m * n * log(m * n))",
    "space_complexity": "O(m * n)",
    "description": "Determine if a person can reach the exit before the fire reaches them, considering the fire spreads to adjacent cells every minute.",
}

from collections import deque

def solve(grid: list[list[int]]) -> bool:
    """
    Determines if a person can reach the exit (m-1, n-1) before the fire reaches it.

    Args:
        grid: A 2D grid where 0 is empty, 1 is obstacle, 2 is fire, and 3 is person.

    Returns:
        True if the person can reach the exit safely, False otherwise.

    Examples:
        >>> solve([[0,0,0],[0,0,0],[0,0,3]])
        True
    """
    rows = len(grid)
    cols = len(grid[0])
    
    fire_start = []
    person_start = None
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                fire_start.append((r, c))
            elif grid[r][c] == 3:
                person_start = (r, c)

    # Precompute fire arrival times for every cell using BFS
    fire_arrival = [[float('inf')] * cols for _ in range(rows)]
    fire_queue = deque(fire_start)
    for r, c in fire_start:
        fire_arrival[r][c] = 0
        
    while fire_queue:
        r, c = fire_queue.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 1:
                if fire_arrival[nr][nc] == float('inf'):
                    fire_arrival[nr][nc] = fire_arrival[r][c] + 1
                    fire_queue.append((nr, nc))

    def can_escape(time_limit: int) -> bool:
        """
        Checks if the person can reach the exit within a specific time limit.
        Note: The problem asks if there exists *any* time such that the person 
        reaches the exit before the fire, but the fire might reach the exit 
        at the same time as the person. The specific rule is: the person 
        can reach the exit at the same time as the fire ONLY if the person 
        reaches it first.
        """
        # Standard BFS to find if person can reach (rows-1, cols-1)
        # We use a simple BFS to find the shortest path for the person
        person_queue = deque([(person_start[0], person_start[1], 0)])
        visited = [[False] * cols for _ in range(rows)]
        visited[person_start[0]][person_start[1]] = True
        
        while person_queue:
            r, c, t = person_queue.popleft()
            
            if r == rows - 1 and c == cols - 1:
                # Special condition: if person reaches exit at the same time as fire,
                # they are only safe if the fire hasn't reached the exit yet or 
                # they arrive exactly when the fire does but the fire is not 'occupying' it.
                # Actually, the rule is: person can reach exit at time T if fire_arrival[exit] > T.
                # EXCEPT if the person reaches the exit at the exact same time as the fire, 
                # they are safe ONLY if the fire cannot reach the exit at that time.
                # Wait, the problem says: "the person can reach the exit at the same time 
                # as the fire, but the fire will reach the exit at the same time."
                # Re-reading: "the person can reach the exit at the same time as the fire, 
                # but the fire will reach the exit at the same time." 
                # This means if person_time == fire_time, it's only okay if it's the exit.
                # But the fire also spreads. The actual condition is:
                # If person reaches exit at time T, they are safe if fire_arrival[exit] > T
                # OR if fire_arrival[exit] == T and the fire reaches the exit from a direction
                # that doesn't block the person. Actually, the simplest way is:
                # If person reaches exit at time T, they are safe if fire_arrival[exit] > T
                # OR (fire_arrival[exit] == T and person reaches it via a path that is not 
                # immediately consumed).
                # The constraint is: person_time < fire_arrival[exit] OR 
                # (person_time == fire_arrival[exit] AND person reaches exit at the same time).
                # Let's refine: The person is safe if they reach (rows-1, cols-1) at time T
                # and fire_arrival[rows-1][cols-1] > T OR (fire_arrival[rows-1][cols-1] == T 
                # and the person reaches it).
                # Wait, the problem says: "the person can reach the exit at the same time 
                # as the fire, but the fire will reach the exit at the same time."
                # This is a bit ambiguous. Let's use the logic:
                # Person is safe if person_time < fire_arrival[exit] 
                # OR (person_time == fire_arrival[exit] AND person reaches exit).
                # Actually, the condition is: person_time < fire_arrival[exit] 
                # OR (person_time == fire_arrival[exit] AND the fire reaches the exit 
                # at the same time but the person is already there).
                # Let's use: person_time < fire_arrival[exit] OR (person_time == fire_arrival[exit] 
                # and the person reaches the exit).
                # Let's check the edge case: if fire_arrival[exit] is T, the person can 
                # reach it at T.
                return True

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                new_t = t + 1
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 1 and not visited[nr][nc]:
                    # Person can move to (nr, nc) if fire hasn't reached it yet
                    # If (nr, nc) is the exit, person can arrive at the same time as fire
                    if nr == rows - 1 and nc == cols - 1:
                        if fire_arrival[nr][nc] >= new_t:
                            return True
                    elif fire_arrival[nr][nc] > new_t:
                        visited[nr][nc] = True
                        person_queue.append((nr, nc, new_t))
        return False

    # The problem is actually simpler: we don't need binary search on time.
    # We just need to check if there is ANY path where person_time < fire_arrival[exit]
    # OR person_time == fire_arrival[exit] (only for the exit cell).
    # However, the person must not step into a cell that is ALREADY on fire.
    # So for any cell (r, c) that is NOT the exit, person_time < fire_arrival[r][c].
    # For the exit cell, person_time <= fire_arrival[r][c].
    
    # Let's re-implement the BFS with this logic.
    person_queue = deque([(person_start[0], person_start[1], 0)])
    visited = [[False] * cols for _ in range(rows)]
    visited[person_start[0]][person_start[1]] = True
    
    while person_queue:
        r, c, t = person_queue.popleft()
        
        if r == rows - 1 and c == cols - 1:
            return True
            
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            new_t = t + 1
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 1 and not visited[nr][nc]:
                # If it's the exit, person can arrive at the same time as fire
                if nr == rows - 1 and nc == cols - 1:
                    if fire_arrival[nr][nc] >= new_t:
                        return True
                # For any other cell, person must arrive strictly before fire
                elif fire_arrival[nr][nc] > new_t:
                    visited[nr][nc] = True
                    person_queue.append((nr, nc, new_t))
                    
    return False

# The problem asks for a boolean. The logic above is O(M*N).
# The binary search mentioned in the prompt is actually for a different variation 
# or a way to handle the "can reach the exit at the same time" rule.
# But a single BFS with the correct condition is optimal.

def solve_final(grid: list[list[int]]) -> bool:
    """
    Optimal O(M*N) solution using BFS for fire and BFS for person.
    """
    rows, cols = len(grid), len(grid[0])
    fire_arrival = [[float('inf')] * cols for _ in range(rows)]
    fire_q = deque()
    person_start = None
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                fire_q.append((r, c))
                fire_arrival[r][c] = 0
            elif grid[r][c] == 3:
                person_start = (r, c)
                
    # 1. BFS for fire
    while fire_q:
        r, c = fire_q.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 1:
                if fire_arrival[nr][nc] == float('inf'):
                    fire_arrival[nr][nc] = fire_arrival[r][c] + 1
                    fire_q.append((nr, nc))
                    
    # 2. BFS for person
    person_q = deque([(person_start[0], person_start[1], 0)])
    visited = [[False] * cols for _ in range(rows)]
    visited[person_start[0]][person_start[1]] = True
    
    while person_q:
        r, c, t = person_q.popleft()
        
        if r == rows - 1 and c == cols - 1:
            return True
            
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            nt = t + 1
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 1 and not visited[nr][nc]:
                # If it's the exit, person can arrive at the same time as fire
                if nr == rows - 1 and nc == cols - 1:
                    if fire_arrival[nr][nc] >= nt:
                        return True
                # For any other cell, person must arrive strictly before fire
                elif fire_arrival[nr][nc] > nt:
                    visited[nr][nc] = True
                    person_q.append((nr, nc, nt))
                    
    return False

# Re-assigning solve to the correct implementation
solve = solve_final
