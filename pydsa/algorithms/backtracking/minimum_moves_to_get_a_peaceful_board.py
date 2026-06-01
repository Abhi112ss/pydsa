METADATA = {
    "id": 3189,
    "name": "Minimum Moves to Get a Peaceful Board",
    "slug": "minimum-moves-to-get-a-peaceful-board",
    "category": "Breadth-First Search",
    "aliases": [],
    "tags": ["backtracking", "bitmask", "bfs"],
    "difficulty": "hard",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of moves to rearrange queens on a 3x3 board such that no two queens attack each other.",
}

from collections import deque

def solve(board: list[list[str]]) -> int:
    """
    Finds the minimum number of moves to rearrange queens on a 3x3 board 
    to a peaceful state using BFS.

    Args:
        board: A 3x3 grid of characters where 'Q' represents a queen and '.' is empty.

    Returns:
        The minimum number of moves to reach a peaceful state.

    Examples:
        >>> solve([["Q", ".", "."], [".", ".", "."], [".", ".", "."]])
        2
        >>> solve([["Q", "Q", "Q"], ["Q", "Q", "Q"], ["Q", "Q", "Q"]])
        6
    """
    
    def is_peaceful(state: int) -> bool:
        """Checks if a given bitmask state is peaceful."""
        # Convert bitmask to 2D coordinates
        queens = []
        for i in range(9):
            if (state >> i) & 1:
                queens.append((i // 3, i % 3))
        
        # Check every pair of queens for conflicts
        for i in range(len(queens)):
            for j in range(i + 1, len(queens)):
                r1, c1 = queens[i]
                r2, c2 = queens[j]
                # Same row, same column, or same diagonal
                if r1 == r2 or c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
                    return False
        return True

    # Precompute all valid (peaceful) states for a 3x3 board with 3 queens
    # There are only 362,880 total permutations, but only a few are peaceful.
    peaceful_states = set()
    for state in range(1 << 9):
        # A peaceful board must have exactly 3 queens
        if bin(state).count('1') == 3:
            if is_peaceful(state):
                peaceful_states.add(state)

    # Convert input board to bitmask
    start_state = 0
    for r in range(3):
        for c in range(3):
            if board[r][c] == 'Q':
                start_state |= (1 << (r * 3 + c))

    # BFS to find the shortest path to any peaceful state
    queue = deque([(start_state, 0)])
    visited = {start_state}

    while queue:
        current_state, moves = queue.popleft()

        if current_state in peaceful_states:
            return moves

        # Try moving a queen to an empty spot
        # A move is defined as picking one 'Q' and moving it to one '.'
        for i in range(9):
            if (current_state >> i) & 1:  # If there is a queen at position i
                for j in range(9):
                    if not ((current_state >> j) & 1):  # If position j is empty
                        # Swap queen from i to j
                        next_state = current_state ^ (1 << i) ^ (1 << j)
                        if next_state not in visited:
                            visited.add(next_state)
                            queue.append((next_state, moves + 1))

    return -1
