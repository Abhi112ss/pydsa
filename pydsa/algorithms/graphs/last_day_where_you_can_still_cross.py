METADATA = {
    "id": 1970,
    "name": "Last Day Where You Can Still Cross",
    "slug": "last-day-where-you-can-still-cross",
    "category": "Union Find",
    "aliases": [],
    "tags": ["union_find", "greedy", "disjoint_set_union"],
    "difficulty": "medium",
    "time_complexity": "O(n * alpha(n))",
    "space_complexity": "O(n)",
    "description": "Find the last day you can cross a river by connecting adjacent ice blocks using Union-Find.",
}

class UnionFind:
    """A standard Disjoint Set Union (DSU) implementation with path compression and union by rank."""
    
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            return True
        return False

def solve(grid: list[list[int]]) -> int:
    """
    Finds the last day you can still cross the river.
    
    The strategy is to treat the ice blocks as nodes in a graph. We process 
    the days in reverse (from the last day to the first). On each day, 
    we add the ice blocks that appear on that day and connect them to 
    their adjacent ice blocks. We stop as soon as the top row is connected 
    to the bottom row.

    Args:
        grid: A 2D list of integers where grid[r][c] is the day ice appears at (r, c).

    Returns:
        The last day you can still cross the river. If you can never cross, returns -1.

    Examples:
        >>> solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        1
        >>> solve([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        3
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # We use two virtual nodes: 
    # index 'rows * cols' represents the top boundary (above row 0)
    # index 'rows * cols + 1' represents the bottom boundary (below row rows-1)
    TOP_VIRTUAL = rows * cols
    BOTTOM_VIRTUAL = rows * cols + 1
    dsu = UnionFind(rows * cols + 2)
    
    # Group coordinates by the day they appear
    # max_day can be up to 10^9, but we only care about days present in the grid
    day_to_coords = {}
    max_day = 0
    for r in range(rows):
        for c in range(cols):
            day = grid[r][c]
            if day not in day_to_coords:
                day_to_coords[day] = []
            day_to_coords[day].append((r, c))
            if day > max_day:
                max_day = day
                
    # Sort days in descending order to find the "last" day
    sorted_days = sorted(day_to_coords.keys(), reverse=True)
    
    # Helper to get 1D index from 2D coordinates
    def get_idx(r: int, c: int) -> int:
        return r * cols + c

    # Process days from latest to earliest
    for day in sorted_days:
        for r, c in day_to_coords[day]:
            curr_idx = get_idx(r, c)
            
            # Connect to virtual top if in row 0
            if r == 0:
                dsu.union(curr_idx, TOP_VIRTUAL)
            # Connect to virtual bottom if in last row
            if r == rows - 1:
                dsu.union(curr_idx, BOTTOM_VIRTUAL)
                
            # Check 4-directional neighbors
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                # If neighbor is within bounds and has already appeared (day <= current day)
                # Note: Since we process days in reverse, "already appeared" means 
                # the neighbor's day is >= current day.
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] >= day:
                    dsu.union(curr_idx, get_idx(nr, nc))
        
        # After adding all ice for this day, check if top and bottom are connected
        # If they are connected, the "last day" we could cross was the day BEFORE 
        # this one (because this day completed the path, meaning we couldn't cross 
        # on the day this path was formed). 
        # Wait, the logic is: if they are connected NOW, it means on 'day', 
        # the path is complete. But we want the last day we COULD cross.
        # Actually, if they are connected on 'day', it means we can cross on 'day'.
        # However, the problem asks for the last day we can cross. 
        # If we process in reverse, the first time they connect, that is the 
        # latest possible day.
        if dsu.find(TOP_VIRTUAL) == dsu.find(BOTTOM_VIRTUAL):
            return day
            
    return -1
