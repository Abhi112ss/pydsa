METADATA = {
    "id": 1914,
    "name": "Cyclically Rotating a Grid",
    "slug": "cyclically_rotating_a_grid",
    "category": "Simulation",
    "aliases": [],
    "tags": ["simulation", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Rotate a grid cyclically by a given number of steps, where elements move along the perimeter of each concentric ring.",
}

def solve(grid: list[list[int]], k: int) -> list[list[int]]:
    """
    Rotates the grid cyclically by k steps.

    Each concentric ring of the grid is rotated independently. The rotation
    is performed by flattening each ring into a 1D list, shifting the elements,
    and then mapping them back to their original positions in the ring.

    Args:
        grid: A 2D list of integers representing the grid.
        k: The number of cyclic shifts to perform.

    Returns:
        A 2D list of integers representing the rotated grid.

    Examples:
        >>> grid = [[1, 2], [3, 4]]
        >>> k = 1
        >>> solve(grid, k)
        [[3, 1], [4, 2]]
    """
    rows = len(grid)
    cols = len(grid[0])
    # Create a deep copy to avoid mutating the input grid
    result = [[0] * cols for _ in range(rows)]
    
    # Determine the number of concentric rings
    num_rings = min(rows, cols) // 2
    
    # Track which cells have been processed to handle the center of odd-sized grids
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    for ring_idx in range(num_rings):
        ring_coords = []
        
        # 1. Traverse the ring in a clockwise direction to collect coordinates
        # Top row (left to right)
        for c in range(ring_idx, cols - ring_idx):
            ring_coords.append((ring_idx, c))
        
        # Right column (top to bottom, skipping first element)
        for r in range(ring_idx + 1, rows - ring_idx):
            ring_coords.append((r, cols - 1 - ring_idx))
            
        # Bottom row (right to left, skipping first element)
        for c in range(cols - 2 - ring_idx, ring_idx - 1, -1):
            ring_coords.append((rows - 1 - ring_idx, c))
            
        # Left column (bottom to top, skipping first and last elements)
        for r in range(rows - 2 - ring_idx, ring_idx, -1):
            ring_coords.append((r, ring_idx))

        # Mark these coordinates as visited
        for r, c in ring_coords:
            visited[r][c] = True

        # 2. Perform the cyclic shift
        # The effective shift is k modulo the length of the ring
        ring_len = len(ring_coords)
        shift = k % ring_len
        
        for i in range(ring_len):
            # The element at ring_coords[i] moves to ring_coords[(i + shift) % ring_len]
            old_r, old_c = ring_coords[i]
            new_r, new_c = ring_coords[(i + shift) % ring_len]
            result[new_r][new_c] = grid[old_r][old_c]

    # 3. Handle the center element for grids with odd dimensions
    # If the grid has an odd number of rows or columns, the center element remains unchanged
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                result[r][c] = grid[r][c]

    return result
