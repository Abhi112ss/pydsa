METADATA = {
    "id": 1267,
    "name": "Count Servers that Communicate",
    "slug": "count-servers-that-communicate",
    "category": "Matrix",
    "aliases": [],
    "tags": ["matrix", "counting", "array"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m + n)",
    "description": "Count the number of servers that can communicate with at least one other server in the same row or column.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Counts the number of servers that can communicate with another server.
    
    A server can communicate if there is at least one other server in the 
    same row or the same column.

    Args:
        grid: A 2D list of integers where 1 represents a server and 0 represents an empty space.

    Returns:
        The total count of servers that can communicate.

    Examples:
        >>> solve([[1,1],[0,0]])
        2
        >>> solve([[1,0],[0,1]])
        0
        >>> solve([[1,1,0],[0,0,0],[0,0,1]])
        2
    """
    if not grid or not grid[0]:
        return 0

    rows_count = len(grid)
    cols_count = len(grid[0])

    # Arrays to store the total number of servers in each row and each column
    row_server_counts = [0] * rows_count
    col_server_counts = [0] * cols_count

    # First pass: Populate the row and column counts
    for r in range(rows_count):
        for c in range(cols_count):
            if grid[r][c] == 1:
                row_server_counts[r] += 1
                col_server_counts[c] += 1

    communicating_servers = 0

    # Second pass: A server communicates if its row or column has more than 1 server
    for r in range(rows_count):
        for c in range(cols_count):
            if grid[r][c] == 1:
                # If the current server's row or column contains other servers
                if row_server_counts[r] > 1 or col_server_counts[c] > 1:
                    communicating_servers += 1

    return communicating_servers
