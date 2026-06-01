METADATA = {
    "id": 773,
    "name": "Sliding Puzzle",
    "slug": "sliding-puzzle",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "matrix", "graph"],
    "difficulty": "medium",
    "time_complexity": "O((M*N)!)",
    "space_complexity": "O((M*N)!)",
    "description": "Find the minimum number of moves to reach the target state in a sliding puzzle using Breadth-First Search.",
}

from collections import deque

def solve(board: list[list[int]]) -> int:
    """
    Finds the minimum number of moves to transform the board into the target state.

    Args:
        board: A 2D list representing the current state of the 2x3 puzzle.

    Returns:
        The minimum number of moves to reach the target state [1, 2, 3, 4, 5, 0],
        or -1 if the target state is unreachable.

    Examples:
        >>> solve([[1, 2, 3], [4, 0, 5]])
        1
        >>> solve([[4, 1, 2], [5, 0, 3]])
        5
        >>> solve([[1, 2, 3], [4, 5, 0]])
        0
    """
    rows = len(board)
    cols = len(board[0])
    target = "123450"
    
    # Convert 2D board to a string representation for easy hashing and comparison
    start_state = "".join(str(board[r][c]) for r in range(rows) for c in range(cols))
    
    if start_state == target:
        return 0

    # Precompute adjacency list for a 1D representation of a 2x3 grid
    # Index mapping for a 2x3 grid:
    # 0 1 2
    # 3 4 5
    adj = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4],
        4: [1, 3, 5],
        5: [2, 4]
    }

    # BFS initialization
    queue = deque([(start_state, 0)])  # (current_state_string, moves_count)
    visited = {start_state}

    while queue:
        current_state, moves = queue.popleft()

        # Find the position of the empty tile '0'
        zero_idx = current_state.find('0')

        # Try all possible moves for the empty tile based on precomputed adjacency
        for neighbor in adj[zero_idx]:
            # Swap '0' with its neighbor to create a new state
            state_list = list(current_state)
            state_list[zero_idx], state_list[neighbor] = state_list[neighbor], state_list[zero_idx]
            next_state = "".join(state_list)

            if next_state == target:
                return moves + 1

            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, moves + 1))

    return -1
