METADATA = {
    "id": 1306,
    "name": "Jump Game III",
    "slug": "jump-game-iii",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "dfs", "recursion", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if you can reach any index containing the value 0 starting from a given index by jumping forward or backward by the value at the current index.",
}

def solve(arr: list[int], start_index: int) -> bool:
    """
    Determines if an index with value 0 is reachable from the start_index.

    The problem is modeled as a graph traversal where each index 'i' has 
    edges to 'i + arr[i]' and 'i - arr[i]'.

    Args:
        arr: A list of integers representing the jump distances.
        start_index: The starting position in the array.

    Returns:
        True if an index with value 0 is reachable, False otherwise.

    Examples:
        >>> solve([2, 3, 1, 1, 4], 0)
        True
        >>> solve([1, 2, 3, 4, 5], 0)
        False
    """
    n = len(arr)
    # Use a stack for an iterative Depth First Search (DFS)
    stack: list[int] = [start_index]
    # Keep track of visited indices to prevent infinite loops
    visited: set[int] = {start_index}

    while stack:
        current_index = stack.pop()

        # Check if we have reached the target
        if arr[current_index] == 0:
            return True

        jump_distance = arr[current_index]
        
        # Calculate potential next positions
        next_positions = [current_index + jump_distance, current_index - jump_distance]

        for next_idx in next_positions:
            # Validate bounds and ensure the index hasn't been visited
            if 0 <= next_idx < n and next_idx not in visited:
                visited.add(next_idx)
                stack.append(next_idx)

    return False
