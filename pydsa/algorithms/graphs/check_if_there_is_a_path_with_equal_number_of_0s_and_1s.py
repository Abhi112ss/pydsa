METADATA = {
    "id": 2510,
    "name": "Check if There is a Path With Equal Number of 0's And 1's",
    "slug": "check-if-there-is-a-path-with-equal-number-of-0s-and-1s",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "graphs", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Determine if there exists a path from the top-left to the bottom-right of a binary matrix such that the number of 0s equals the number of 1s.",
}

def solve(grid: list[list[int]]) -> bool:
    """
    Determines if there is a path from (0, 0) to (m-1, n-1) with equal 0s and 1s.

    Args:
        grid: A 2D list of integers representing the binary matrix.

    Returns:
        True if such a path exists, False otherwise.

    Examples:
        >>> solve([[0, 1], [1, 0]])
        True
        >>> solve([[0, 1], [1, 1]])
        False
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # Target: Since we count both 0s and 1s, the total path length is (rows + cols - 1).
    # For 0s to equal 1s, the total length must be even, and we need exactly half 0s and half 1s.
    total_elements_in_path = rows + cols - 1
    if total_elements_in_path % 2 != 0:
        return False
    
    target_count = total_elements_in_path // 2
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(r: int, c: int, count_zeros: int) -> bool:
        """
        Helper function to perform DFS traversal.
        
        Args:
            r: Current row index.
            c: Current column index.
            count_zeros: Number of zeros encountered so far in the path.
            
        Returns:
            True if a valid path is found, False otherwise.
        """
        # Update zero count if current cell is 0
        if grid[r][c] == 0:
            count_zeros += 1
            
        # Pruning: If zeros exceed half the path length, this path is invalid
        if count_zeros > target_count:
            return False
            
        # Base case: Reached the bottom-right corner
        if r == rows - 1 and c == cols - 1:
            return count_zeros == target_count

        visited[r][c] = True
        
        # Explore 4 possible directions: Down, Up, Right, Left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # Check boundaries and if the cell is already visited
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                if dfs(nr, nc, count_zeros):
                    return True
        
        # Backtrack: Unmark visited to allow other paths to use this cell
        visited[r][c] = False
        return False

    return dfs(0, 0, 0)
