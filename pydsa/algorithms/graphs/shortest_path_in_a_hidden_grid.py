METADATA = {
    "id": 1778,
    "name": "Shortest Path in a Hidden Grid",
    "slug": "shortest-path-in-a-hidden-grid",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "dfs", "graph"],
    "difficulty": "hard",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V)",
    "description": "Find the shortest path from a starting position to a target position in a grid where cells are discovered via a robot's movement.",
}

from collections import deque

class Solution:
    def findShortestPath(self, grid: 'GridMaster') -> list[list[int]]:
        """
        Finds the shortest path from the starting position to the target position
        using DFS to map the grid and BFS to find the shortest path.

        Args:
            grid: An object representing the hidden grid with methods 
                  move(direction), isTarget(), and canMove(direction).

        Returns:
            A list of [row, col] coordinates representing the shortest path.
            Returns an empty list if the target is unreachable.

        Examples:
            >>> # Example logic:
            >>> # If start is (0,0) and target is (1,1) and path is (0,0)->(0,1)->(1,1)
            >>> # Returns [[0, 0], [0, 1], [1, 1]]
        """
        # Directions mapping: (row_offset, col_offset, move_command, opposite_move_command)
        # Using strings for directions as per typical GridMaster API requirements
        DIRECTIONS = {
            'U': (-1, 0, 'U', 'D'),
            'D': (1, 0, 'D', 'U'),
            'L': (0, -1, 'L', 'R'),
            'R': (0, 1, 'R', 'L')
        }
        
        # grid_map stores the discovered cells: (r, c) -> is_target (bool)
        grid_map = {}
        start_pos = (0, 0)
        target_pos = None

        def dfs(r: int, c: int) -> bool:
            """Explores the grid using DFS to build a local map."""
            nonlocal target_pos
            
            # Mark current cell as visited/reachable
            grid_map[(r, c)] = grid.isTarget()
            if grid_map[(r, c)]:
                target_pos = (r, c)

            for move_dir, (dr, dc, cmd, rev_cmd) in DIRECTIONS.items():
                nr, nc = r + dr, c + dc
                
                # If we haven't visited this cell and the robot can move there
                if (nr, nc) not in grid_map and grid.canMove(cmd):
                    grid.move(cmd)
                    dfs(nr, nc)
                    # Backtrack: move the robot back to the previous cell
                    grid.move(rev_cmd)

        # Step 1: Map the reachable grid using DFS
        dfs(0, 0)

        # If target was never found during DFS, it's unreachable
        if target_pos is None:
            return []

        # Step 2: Find the shortest path using BFS on the discovered grid_map
        # queue stores (current_r, current_c, path_taken)
        queue = deque([(start_pos[0], start_pos[1], [start_pos])])
        visited_bfs = {start_pos}

        while queue:
            curr_r, curr_c, path = queue.popleft()

            if (curr_r, curr_c) == target_pos:
                return path

            for dr, dc, _, _ in DIRECTIONS.values():
                nr, nc = curr_r + dr, curr_c + dc
                
                # Only move to cells that were discovered and are not walls
                if (nr, nc) in grid_map and (nr, nc) not in visited_bfs:
                    visited_bfs.add((nr, nc))
                    queue.append((nr, nc, path + [(nr, nc)]))

        return []

# Note: The GridMaster class is provided by the LeetCode environment.
# This implementation assumes the standard interface for the problem.