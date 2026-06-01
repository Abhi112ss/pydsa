METADATA = {
    "id": 1274,
    "name": "Number of Ships in a Rectangle",
    "slug": "number-of-ships-in-a-rectangle",
    "category": "Divide and Conquer",
    "aliases": [],
    "tags": ["divide_and_conquer", "recursion", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(log(max_coord))",
    "space_complexity": "O(log(max_coord))",
    "description": "Count the number of ships in a rectangle using a quadtree-like divide and conquer approach with a provided API.",
}

class Solution:
    def countShips(self, isShipInRange: callable, height: int, width: int) -> int:
        """
        Counts the number of ships in a rectangle using a divide and conquer approach.

        Args:
            isShipInRange: A function that returns True if there is at least one ship 
                           in the specified rectangle [top, left, bottom, right].
            height: The total height of the grid.
            width: The total width of the grid.

        Returns:
            The total number of ships found in the grid.

        Examples:
            >>> # Example usage (mocking the API)
            >>> def mock_api(top, left, bottom, right):
            ...     # Assume a ship exists at (1, 1)
            ...     return not (top > 1 or bottom < 1 or left > 1 or right < 1)
            >>> sol = Solution()
            >>> sol.countShips(mock_api, 3, 3)
            1
        """

        def divide_and_conquer(top: int, left: int, bottom: int, right: int) -> int:
            # Base case: If the current rectangle contains no ships, return 0
            if not isShipInRange(top, left, bottom, right):
                return 0

            # Base case: If the rectangle is a single cell and we know it has a ship
            if top == bottom and left == right:
                return 1

            # Calculate midpoints to split the rectangle into four quadrants
            mid_row = (top + bottom) // 2
            mid_col = (left + right) // 2

            total_ships = 0

            # Quadrant 1: Top-Left
            total_ships += divide_and_conquer(top, left, mid_row, mid_col)

            # Quadrant 2: Top-Right
            # Only proceed if the rectangle has width to split
            if mid_col < right:
                total_ships += divide_and_conquer(top, mid_col + 1, mid_row, right)

            # Quadrant 3: Bottom-Left
            # Only proceed if the rectangle has height to split
            if mid_row < bottom:
                total_ships += divide_and_conquer(mid_row + 1, left, bottom, mid_col)

            # Quadrant 4: Bottom-Right
            if mid_row < bottom and mid_col < right:
                total_ships += divide_and_conquer(mid_row + 1, mid_col + 1, bottom, right)

            return total_ships

        # Start the recursion from the full grid boundaries
        return divide_and_conquer(0, 0, height - 1, width - 1)

def solve():
    """
    Entry point for testing the implementation.
    """
    # Mock API for testing: Ship at (1, 1) in a 3x3 grid
    def mock_api(top: int, left: int, bottom: int, right: int) -> bool:
        # Check if the ship at (1, 1) is within the queried bounds
        ship_row, ship_col = 1, 1
        return not (top > ship_row or bottom < ship_row or left > ship_col or right < ship_col)

    solution = Solution()
    result = solution.countShips(mock_api, 3, 3)
    print(f"Ships found: {result}")
    assert result == 1
