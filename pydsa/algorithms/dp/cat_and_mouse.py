METADATA = {
    "id": 913,
    "name": "Cat and Mouse",
    "slug": "cat-and-mouse",
    "category": "Graph",
    "aliases": [],
    "tags": ["graph", "game_theory", "dynamic_programming", "breadth_first_search"],
    "difficulty": "hard",
    "time_complexity": "O(N^3)",
    "space_complexity": "O(N^3)",
    "description": "Determine the winner of a game played on a graph between a cat and a mouse.",
}

from collections import deque

def solve(grid: list[list[int]], mouse_start: list[int], cat_start: list[int]) -> int:
    """
    Args:
        grid: A 2D list representing the graph where grid[i][j] is the neighbor of node i.
        mouse_start: The starting node of the mouse.
        cat_start: The starting node of the cat.

    Returns:
        0 if the mouse wins, 1 if the cat wins, and 2 if it is a draw.
    """
    n = len(grid)
    
    def get_state_key(mouse_pos: int, cat_pos: int, turn: int) -> tuple[int, int, int]:
        return (mouse_pos, cat_pos, turn)

    results = {}
    degree = {}

    for m in range(n):
        for c in range(n):
            for turn in range(2):
                degree[(m, c, turn)] = 0
                for neighbor in grid[m if turn == 0 else c]:
                    if turn == 0:
                        degree[(m, c, turn)] += 1
                    else:
                        degree[(m, c, turn)] += 1
                
                # Correct degree calculation: number of possible moves from this state
                # In this game, the player whose turn it is chooses a neighbor.
                # The degree should represent the number of available moves for the current player.
                # However, for topological sort, we need the out-degree of the state to propagate backwards.
                # Actually, we need the in-degree of the state in the reverse graph.
                # Let's redefine: degree[state] = number of moves available from this state.
                # We will use a queue to process states whose outcome is certain.
                
    # Re-calculating degree correctly: degree[m][c][turn] is the number of moves available from that state.
    degree = {}
    for m in range(n):
        for c in range(n):
            for turn in range(2):
                if turn == 0:
                    degree[(m, c, turn)] = len(grid[m])
                else:
                    degree[(m, c, turn)] = len(grid[c])

    queue = deque()
    outcome = {}

    for m in range(n):
        for c in range(n):
            if m == n - 1:
                outcome[(m, c, 0)] = 0
                outcome[(m, c, 1)] = 0
                queue.append((m, c, 0))
                queue.append((m, c, 1))
            elif c == m:
                outcome[(m, c, 0)] = 1
                outcome[(m, c, 1)] = 1
                queue.append((m, c, 0))
                queue.append((m, c, 1))

    while queue:
        m, c, turn = queue.popleft()
        current_outcome = outcome[(m, c, turn)]
        
        prev_turn = 1 - turn
        for prev_node in grid[c if prev_turn == 0 else m]:
            prev_m = prev_node if prev_turn == 0 else m
            prev_c = c if prev_turn == 0 else prev_node
            prev_state = (prev_m, prev_c, prev_turn)
            
            if prev_state in outcome:
                continue
            
            if (prev_turn == 0 and current_outcome == 0) or (prev_turn == 1 and current_outcome == 1):
                outcome[prev_state] = current_outcome
                queue.append(prev_state)
            else:
                degree[prev_state] -= 1
                if degree[prev_state] == 0:
                    outcome[prev_state] = 1 - current_outcome
                    queue.append(prev_state)

    start_state = (mouse_start[0], cat_start[0], 0)
    return outcome.get(start_state, 2)