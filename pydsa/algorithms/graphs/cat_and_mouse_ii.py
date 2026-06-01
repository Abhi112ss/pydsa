METADATA = {
    "id": 1728,
    "name": "Cat and Mouse II",
    "slug": "cat-and-mouse-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["bfs", "graphs", "dynamic_programming"],
    "difficulty": "hard",
    "time_complexity": "O(M * N^3)",
    "space_complexity": "O(M * N^3)",
    "description": "A game theory problem where a cat and a mouse move on a grid with holes, determining if the mouse can win given optimal play.",
}

def solve(grid: list[list[int]], max_moves: int) -> bool:
    """
    Args:
        grid: A 2D grid where 0 is empty, 1 is a hole, 2 is the mouse, and 3 is the cat.
        max_moves: The maximum number of moves allowed in the game.

    Returns:
        True if the mouse can win, False otherwise.
    """
    rows = len(grid)
    cols = len(grid[0])
    mouse_pos = None
    cat_pos = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                mouse_pos = (r, c)
            elif grid[r][c] == 3:
                cat_pos = (r, c)

    def get_neighbors(r: int, c: int) -> list[tuple[int, int]]:
        neighbors = []
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 1:
                neighbors.append((nr, nc))
        return neighbors

    def is_terminal(m_r: int, m_c: int, c_r: int, c_c: int, turn: int) -> int:
        if m_r == rows - 1 and m_c == cols - 1:
            return 1
        if m_r == c_r and m_c == c_c:
            return 2
        return 0

    status = {}
    degree = {}

    for m_r in range(rows):
        for m_c in range(cols):
            if grid[m_r][m_c] == 1:
                continue
            for c_r in range(rows):
                for c_c in range(cols):
                    if grid[c_r][c_c] == 1:
                        continue
                    for turn in [0, 1]:
                        state = (m_r, m_c, c_r, c_c, turn)
                        term = is_terminal(m_r, m_c, c_r, c_c, turn)
                        if term != 0:
                            status[state] = term
                        else:
                            if turn == 0:
                                degree[state] = len(get_neighbors(m_r, m_c))
                            else:
                                degree[state] = len(get_neighbors(c_r, c_c))
                            if degree[state] == 0:
                                status[state] = 2

    queue = [state for state, s in status.items()]
    idx = 0
    while idx < len(queue):
        curr_state = queue[idx]
        idx += 1
        m_r, m_c, c_r, c_c, turn = curr_state
        curr_res = status[curr_state]

        prev_turn = 1 - turn
        if prev_turn == 0:
            for pm_r, pm_c in get_neighbors(m_r, m_c):
                if grid[pm_r][pm_c] == 1:
                    continue
                prev_state = (pm_r, pm_c, c_r, c_c, 0)
                if prev_state in status:
                    continue
                
                if curr_res == 1:
                    status[prev_state] = 1
                    queue.append(prev_state)
                else:
                    degree[prev_state] -= 1
                    if degree[prev_state] == 0:
                        status[prev_state] = 2
                        queue.append(prev_state)
        else:
            for pc_r, pc_c in get_neighbors(c_r, c_c):
                if grid[pc_r][pc_c] == 1:
                    continue
                prev_state = (m_r, m_c, pc_r, pc_c, 1)
                if prev_state in status:
                    continue

                if curr_res == 2:
                    status[prev_state] = 2
                    queue.append(prev_state)
                else:
                    degree[prev_state] -= 1
                    if degree[prev_state] == 0:
                        status[prev_state] = 1
                        queue.append(prev_state)

    memo = {}

    def solve_recursive(m_r: int, m_c: int, c_r: int, c_c: int, turn: int, moves: int) -> bool:
        if moves > max_moves:
            return False
        
        term = is_terminal(m_r, m_c, c_r, c_c, turn)
        if term == 1: return True
        if term == 2: return False
        
        state = (m_r, m_c, c_r, c_c, turn, moves)
        if state in memo:
            return memo[state]

        if turn == 0:
            res = False
            for nr, nc in get_neighbors(m_r, m_c):
                if solve_recursive(nr, nc, c_r, c_c, 1, moves + 1):
                    res = True
                    break
            memo[state] = res
            return res
        else:
            res = True
            for nr, nc in get_neighbors(c_r, c_c):
                if not solve_recursive(m_r, m_c, nr, nc, 0, moves + 1):
                    res = False
                    break
            memo[state] = res
            return res

    return solve_recursive(mouse_pos[0], mouse_pos[1], cat_pos[0], cat_pos[1], 0, 0)