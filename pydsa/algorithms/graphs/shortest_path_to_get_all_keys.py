METADATA = {
    "id": 864,
    "name": "Shortest Path to Get All Keys",
    "slug": "shortest-path-to-get-all-keys",
    "category": "Breadth-First Search",
    "aliases": [],
    "tags": ["bfs", "bitmask", "shortest_path"],
    "difficulty": "hard",
    "time_complexity": "O(R * C * 2^K)",
    "space_complexity": "O(R * C * 2^K)",
    "description": "Find the shortest path in a grid to collect all keys, considering obstacles and locked doors.",
}

from collections import deque

def solve(grid: list[str]) -> int:
    """
    Finds the shortest path to collect all keys in a grid using BFS with bitmasking.

    Args:
        grid: A list of strings representing the grid. 
              '.' is empty, '#' is wall, '@' is start, 
              '*' is lock, 'a'-'f' are keys.

    Returns:
        The minimum number of steps to collect all keys, or -1 if impossible.

    Examples:
        >>> solve(["@.a.#".split()[0], ".b.%.a"]) # Simplified example logic
        # Actual example from LeetCode:
        >>> solve(["@.a.#", ".b.%.a"]) # Not valid input format, see below
        >>> solve(["@.a.#", ".b.%.a"]) 
    """
    rows = len(grid)
    cols = len(grid[0])
    
    start_pos = (0, 0)
    total_keys = 0
    
    # Pre-process grid to find start position and total number of keys
    for r in range(rows):
        for c in range(cols):
            char = grid[r][c]
            if char == '@':
                start_pos = (r, c)
            elif 'a' <= char <= 'f':
                total_keys += 1
                
    # Target bitmask: if there are 3 keys, target is (1 << 3) - 1 = 0b111
    target_mask = (1 << total_keys) - 1
    
    # Queue stores: (row, col, current_keys_mask, distance)
    queue = deque([(start_pos[0], start_pos[1], 0, 0)])
    
    # Visited set stores: (row, col, current_keys_mask)
    # This allows revisiting a cell if we have a different set of keys
    visited = set([(start_pos[0], start_pos[1], 0)])
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        r, c, mask, dist = queue.popleft()
        
        # If we have collected all keys, return the distance immediately
        if mask == target_mask:
            return dist
            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # Check boundaries and walls
            if 0 <= nr < rows and 0 <= nc < cols:
                cell = grid[nr][nc]
                
                if cell == '#':
                    continue
                
                new_mask = mask
                
                # If it's a key, update the bitmask
                if 'a' <= cell <= 'f':
                    key_index = ord(cell) - ord('a')
                    new_mask |= (1 << key_index)
                
                # If it's a lock, check if we have the corresponding key
                if 'A' <= cell <= 'F':
                    lock_index = ord(cell) - ord('A')
                    if not (mask & (1 << lock_index)):
                        continue
                
                # If this state (position + key set) hasn't been visited, add to queue
                if (nr, nc, new_mask) not in visited:
                    visited.add((nr, nc, new_mask))
                    queue.append((nr, nc, new_mask, dist + 1))
                    
    return -1
