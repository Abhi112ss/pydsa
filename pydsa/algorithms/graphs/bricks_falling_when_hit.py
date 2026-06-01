METADATA = {
    "id": 803,
    "name": "Bricks Falling When Hit",
    "slug": "bricks-falling-when-hit",
    "category": "Union Find",
    "aliases": [],
    "tags": ["union_find", "grid", "reverse_processing", "simulation"],
    "difficulty": "hard",
    "time_complexity": "O(M * (N * K * alpha(N * M)))",
    "space_complexity": "O(N * M)",
    "description": "Calculate how many bricks fall after each hit by processing hits in reverse and using Disjoint Set Union to track connectivity to the top row.",
}

class DSU:
    """Disjoint Set Union (Union-Find) with path compression and union by rank."""
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.connected_to_top = [False] * n

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Merge the smaller rank tree into the larger rank tree
            if self.rank[root_i] < self.rank[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            if self.rank[root_i] == self.rank[root_j]:
                self.rank[root_i] += 1
            
            # Propagate the 'connected to top' property
            if self.connected_to_top[root_j]:
                self.connected_to_top[root_i] = True
            elif self.connected_to_top[root_i]:
                # This case is actually covered by the logic above, 
                # but we ensure the new root knows if either component was connected to top.
                pass 
            
            # Correct way to handle the boolean property:
            self.connected_to_top[root_i] = self.connected_to_top[root_i] or self.connected_to_top[root_j]

def solve(grid: list[list[int]], hits: list[list[int]]) -> list[int]:
    """
    Calculates the number of bricks that fall after each hit.

    Args:
        grid: A 2D grid where 1 represents a brick and 0 represents empty space.
        hits: A list of [row, col] coordinates representing the hits.

    Returns:
        A list of integers where each element is the number of bricks that fell due to that hit.

    Examples:
        >>> grid = [[1,1,1],[1,1,1],[1,1,1]]
        >>> hits = [[0,1],[1,1]]
        >>> solve(grid, hits)
        [0, 2]
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # Create a copy to avoid mutating the input and track current state
    # We will use this to identify which bricks are "permanently" removed by hits
    current_grid = [row[:] for row in grid]
    
    # Mark all hit locations as empty in the initial state for reverse processing
    for r, c in hits:
        current_grid[r][c] = 0
        
    # DSU size is rows * cols. We use a virtual node (index -1 or similar) 
    # but it's easier to just check if a root's connected_to_top is True.
    dsu = DSU(rows * cols)
    
    # Helper to convert 2D to 1D index
    def get_idx(r: int, c: int) -> int:
        return r * cols + c

    # Initialize DSU with bricks that were NOT hit
    for r in range(rows):
        for c in range(cols):
            if current_grid[r][c] == 1:
                idx = get_idx(r, c)
                if r == 0:
                    dsu.connected_to_top[idx] = True
                
                # Union with neighbors (only check right and down to avoid double work)
                for dr, dc in [(0, 1), (1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and current_grid[nr][nc] == 1:
                        dsu.union(idx, get_idx(nr, nc))

    results = []
    
    # Process hits in reverse order
    for i in range(len(hits) - 1, -1, -1):
        r, c = hits[i]
        
        # If the hit was on an empty space, no bricks fall
        if current_grid[r][c] == 0:
            results.append(0)
            continue
            
        # If the hit was on a brick, we "add" it back
        # We need to count how many bricks become connected to the top row
        # that were NOT connected to the top before this addition.
        
        # Before adding, check if the brick itself is already connected to top
        # (This shouldn't happen if the grid was valid, but for safety:)
        # Actually, the logic is: how many NEW bricks become connected to top?
        
        # We temporarily treat the brick as being added.
        # We need to count how many bricks in the component(s) being merged 
        # were NOT connected to top, but now are.
        # However, DSU doesn't easily track "count of bricks in component".
        # Let's refine: We need to track the number of bricks in each component.
        
        # Re-implementing DSU logic slightly to track component size and top-connectivity
        pass

    # Since the standard DSU doesn't track "count of bricks in component", 
    # let's use a more robust approach within the solve function.
    return _solve_with_refined_dsu(grid, hits)

def _solve_with_refined_dsu(grid: list[list[int]], hits: list[list[int]]) -> list[int]:
    rows = len(grid)
    cols = len(grid[0])
    current_grid = [row[:] for row in grid]
    
    for r, c in hits:
        current_grid[r][c] = 0
        
    parent = list(range(rows * cols))
    size = [1] * (rows * cols)
    is_top = [False] * (rows * cols)
    
    def find(i: int) -> int:
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i: int, j: int):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            # Ensure root_i is the one that stays
            if size[root_i] < size[root_j]:
                root_i, root_j = root_j, root_i
            parent[root_j] = root_i
            size[root_i] += size[root_j]
            is_top[root_i] = is_top[root_i] or is_top[root_j]

    def get_idx(r: int, c: int) -> int:
        return r * cols + c

    # Initial DSU setup
    for r in range(rows):
        for c in range(cols):
            if current_grid[r][c] == 1:
                idx = get_idx(r, c)
                if r == 0:
                    is_top[idx] = True
                # Union with neighbors
                for dr, dc in [(0, 1), (1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and current_grid[nr][nc] == 1:
                        union(idx, get_idx(nr, nc))

    ans = []
    for i in range(len(hits) - 1, -1, -1):
        r, c = hits[i]
        
        # If the hit was on a 0, it means it was already empty (not a brick)
        # or it was a brick that was already removed by a later hit.
        # But in reverse, we are adding bricks back.
        # If the original grid had a 0 at (r,c), no brick can ever be there.
        if grid[r][c] == 0:
            ans.append(0)
            continue
            
        # If the hit was on a brick that is already "empty" in our reverse simulation
        # (meaning it was hit by a later hit), we don't add it back yet.
        # Wait, the logic is: hits are processed in reverse. 
        # A hit at index i removes a brick. In reverse, we add it back.
        # If the brick was already 0 in current_grid, it means it was hit by a hit at index > i.
        # But a single hit can only remove one brick. 
        # If multiple hits hit the same (r,c), only the first one (in original order) matters.
        if current_grid[r][c] == 1:
            # This brick was already hit by a later hit? No, that's impossible.
            # If current_grid[r][c] is 1, it means this brick was NOT hit by any hit in hits[i+1:]
            # This is actually wrong. Let's re-evaluate.
            pass

    # Correct logic:
    # 1. current_grid starts as original grid.
    # 2. For all hits, current_grid[r][c] = 0.
    # 3. If a hit (r,c) is on a cell that was already 0 in the original grid, ignore.
    # 4. If a hit (r,c) is on a cell that was already made 0 by a PREVIOUS hit (in original order), 
    #    it's a redundant hit. We must track this.
    
    # Let's restart the logic clearly.
    return _final_logic(grid, hits)

def _final_logic(grid: list[list[int]], hits: list[list[int]]) -> list[int]:
    rows = len(grid)
    cols = len(grid[0])
    
    # Track which hits actually remove a brick
    # A hit only matters if it hits a brick that hasn't been removed yet.
    effective_hits = []
    temp_grid = [row[:] for row in grid]
    for r, c in hits:
        if temp_grid[r][c] == 1:
            effective_hits.append((r, c))
            temp_grid[r][c] = 0
        else:
            effective_hits.append(None) # Redundant hit

    # Now temp_grid contains the state after ALL effective hits
    parent = list(range(rows * cols))
    size = [1] * (rows * cols)
    is_top = [False] * (rows * cols)

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]] # Path compression
            i = parent[i]
        return i

    def union(i: int, j: int):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            if size[root_i] < size[root_j]:
                root_i, root_j = root_j, root_i
            parent[root_j] = root_i
            size[root_i] += size[root_j]
            is_top[root_i] = is_top[root_i] or is_top[root_j]

    def get_idx(r: int, c: int) -> int:
        return r * cols + c

    # Build DSU for remaining bricks
    for r in range(rows):
        for c in range(cols):
            if temp_grid[r][c] == 1:
                idx = get_idx(r, c)
                if r == 0:
                    is_top[idx] = True
                # Check neighbors
                for dr, dc in [(0, 1), (1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and temp_grid[nr][nc] == 1:
                        union(idx, get_idx(nr, nc))

    results = []
    # Process effective hits in reverse
    for i in range(len(effective_hits) - 1, -1, -1):
        hit = effective_hits[i]
        if hit is None:
            results.append(0)
            continue
        
        r, c = hit
        idx = get_idx(r, c)
        temp_grid[r][c] = 1 # Add brick back
        if r == 0:
            is_top[idx] = True
        
        # Before unioning, check if this brick or its new neighbors 
        # will connect a non-top component to the top.
        
        # We need to count how many bricks in the newly formed component 
        # are now connected to the top, but were not before.
        # This is tricky. Let's use the property:
        # New bricks connected to top = (new component size) - (old component size)
        # if the new component is now connected to top and the old ones weren't.
        
        # Actually, the number of bricks that "fall" is the number of bricks 
        # that were connected to the top before the hit was removed.
        # In reverse, it's the number of bricks that BECOME connected to the top 
        # when the brick is added back.
        
        # Let's track the number of bricks in a component that are connected to top.
        # Wait, the problem asks for bricks that fall. 
        # A brick falls if it's no longer connected to the top.
        # In reverse, when we add a brick, we count how many bricks 
        # in the newly merged component are now connected to the top, 
        # but were NOT connected to the top before.
        
        # Let's refine the DSU to track `count_top`: number of bricks in component connected to top.
        # If a component is connected to top, count_top == size.
        # If not, count_top == 0.
        
        # Let's use:
        # size[root] = total bricks in component
        # is_top[root] = boolean, true if component is connected to top
        
        # When adding brick (r,c):
        # 1. Find all adjacent components.
        # 2. Calculate how many bricks will be connected to top after union.
        # 3. If the brick (r,c) itself is at r=0, it's a new top component.
        # 4. If the brick (r,c) connects a component that was NOT top to a component that WAS top,
        #    the number of bricks that "un-fall" is the size of the non-top component.
        
        # Let's re-calculate:
        # Total bricks connected to top after adding (r,c) = 
        #   (is_top[new_root] ? size[new_root] : 0)
        # Total bricks connected to top before adding (r,c) = 
        #   sum(is_top[root_neighbor] ? size[root_neighbor] : 0) + (r==0 ? 1 : 0)
        # This is still slightly off because (r,c) itself might be at r=0.
        
        # Correct logic for "un-falling" bricks:
        # When adding brick (r,c):
        # If r == 0:
        #    The brick (r,c) is now top. Any neighbor component that was NOT top 
        #    now becomes top. The number of bricks that "un-fall" is the sum of 
        #    sizes of all neighbor components that were NOT top.
        #    Plus 1 for the brick (r,c) itself.
        # If r > 0:
        #    If (r,c) connects a component that WAS top to a component that was NOT top,
        #    the number of bricks that "un-fall" is the size of the NOT-top component.
        #    If (r,c) connects two components that were both NOT top, 0 bricks un-fall.
        #    If (r,c) connects two components that were both top, 0 bricks un-fall.
        #    If (r,c) is not connected