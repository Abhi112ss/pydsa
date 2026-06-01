METADATA = {
    "id": 489,
    "name": "Robot Room Cleaner",
    "slug": "robot-room-cleaner",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["dfs", "backtracking", "graph_traversal"],
    "difficulty": "hard",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Explore a room using a robot API to clean all reachable cells using backtracking.",
}

class RobotRoomCleaner:
    """
    This class is provided by LeetCode. 
    It represents the robot interface.
    """
    def move(self) -> bool:
        """Moves the robot one step in the current direction. Returns True if successful."""
        pass

    def turnLeft(self) -> None:
        """Turns the robot 90 degrees to the left."""
        pass

    def turnRight(self) -> None:
        """Turns the robot 90 degrees to the right."""
        pass

    def clean() -> None:
        """Cleans the current cell."""
        pass


class Solution:
    def cleanRoom(self, robot: RobotRoomCleaner) -> None:
        """
        Explores the entire room and cleans it using Depth First Search (DFS) 
        with backtracking.

        Args:
            robot (RobotRoomCleaner): The robot interface provided by the environment.

        Returns:
            None

        Examples:
            >>> # Assuming a 2x2 room
            >>> solution = Solution()
            >>> solution.cleanRoom(robot)
        """
        # Directions: 0: up, 1: right, 2: down, 3: left
        # We use (row_change, col_change) for each direction
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()

        def backtrack(row: int, col: int, direction_idx: int) -> None:
            """
            Recursive DFS function to explore and clean the room.

            Args:
                row (int): Current row coordinate.
                col (int): Current column coordinate.
                direction_idx (int): Current facing direction index (0-3).
            """
            # Mark current cell as visited and clean it
            visited.add((row, col))
            robot.clean()

            # Try all 4 possible directions starting from the current facing
            for i in range(4):
                # Calculate the actual direction index to rotate to
                # We use (direction_idx + i) % 4 to simulate turning relative to current orientation
                new_dir_idx = (direction_idx + i) % 4
                dr, dc = directions[new_dir_idx]
                next_row, next_col = row + dr, col + dc

                # If the next cell hasn't been visited, attempt to move there
                if (next_row, next_col) not in visited:
                    # 1. Turn the robot to face the target direction
                    # We need to calculate how many turns are needed from current direction_idx
                    # However, it's easier to maintain the robot's physical orientation 
                    # by turning it to the specific direction relative to its current state.
                    
                    # To simplify: we ensure the robot is facing 'new_dir_idx'
                    # But the loop logic below handles the physical turns.
                    
                    # First, we must ensure the robot is physically facing 'new_dir_idx'
                    # We calculate the difference between current direction and target direction
                    # This is handled by the loop structure and the 'turn' calls below.
                    pass

            # Re-implementing the loop logic more cleanly for physical robot control:
            # The loop above was a placeholder for the logic below.
            
        # Let's redefine the inner function to handle physical turns correctly
        def dfs(r: int, c: int, d: int) -> None:
            visited.add((r, c))
            robot.clean()

            # Try all 4 directions: 0: up, 1: right, 2: down, 3: left
            # We iterate through directions in order to maintain a consistent rotation pattern
            for i in range(4):
                # Calculate the direction index to check
                # We rotate the robot relative to its current direction
                # To check all 4 directions, we can turn right 3 times
                
                # 1. Determine the direction to move
                # We use the current direction 'd' and rotate 'i' times
                target_dir = (d + i) % 4
                dr, dc = directions[target_dir]
                nr, nc = r + dr, c + dc

                if (nr, nc) not in visited:
                    # 2. Physically turn the robot to face the target direction
                    # We need to turn the robot from its current orientation 'd' to 'target_dir'
                    # However, the loop is easier if we just turn the robot 90 deg right each time
                    # and check the direction.
                    
                    # Let's adjust the logic: 
                    # We are at (r, c) facing 'd'. 
                    # We want to try moving in 'target_dir'.
                    # To make this work, we must ensure the robot is facing 'target_dir'
                    # before calling robot.move().
                    
                    # But wait, the loop 'for i in range(4)' with 'turnRight' is more robust.
                    pass

        # Corrected DFS implementation
        def solve_dfs(r: int, c: int, current_dir: int) -> None:
            visited.add((r, c))
            robot.clean()

            # We try 4 directions by turning right 4 times
            for _ in range(4):
                # Calculate next cell based on current robot orientation
                dr, dc = directions[current_dir]
                nr, nc = r + dr, c + dc

                if (nr, nc) not in visited:
                    # Move the robot if the cell is new
                    if robot.move():
                        # Recurse into the new cell
                        # Note: robot is now facing the same direction it was when it moved
                        solve_dfs(nr, nc, current_dir)
                        # Backtrack: Move the robot back to the previous cell
                        # To move back, we must turn 180 degrees
                        robot.turnRight()
                        robot.turnRight()
                        robot.move()
                        # Turn back to the original direction to maintain state
                        robot.turnRight()
                        robot.turnRight()
                
                # Turn the robot 90 degrees right to check the next direction
                robot.turnRight()
                current_dir = (current_dir + 1) % 4

        # Start DFS from (0, 0) facing Up (index 0)
        solve_dfs(0, 0, 0)

def solve():
    """Entry point for testing if needed."""
    pass
