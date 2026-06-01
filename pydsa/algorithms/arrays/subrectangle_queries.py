METADATA = {
    "id": 1476,
    "name": "Subrectangle Queries",
    "slug": "subrectangle_queries",
    "category": "Prefix Sum",
    "aliases": [],
    "tags": ["prefix_sum", "2d_array", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n) for initialization, O(1) per query",
    "space_complexity": "O(m * n)",
    "description": "Answer multiple queries for the sum of elements in a subrectangle of a 2D matrix using prefix sums.",
}

class SubrectangleQueries:
    def __init__(self, matrix: list[list[int]]):
        """
        Initializes the SubrectangleQueries object with a 2D prefix sum array.

        Args:
            matrix: A 2D list of integers representing the grid.
        """
        if not matrix or not matrix[0]:
            self.prefix_sum = []
            self.rows = 0
            self.cols = 0
            return

        self.rows = len(matrix)
        self.cols = len(matrix[0])
        
        # Create a prefix sum matrix with an extra row and column of zeros
        # to handle boundary conditions (index - 1) gracefully.
        # prefix_sum[i][j] stores the sum of matrix[0...i-1][0...j-1]
        self.prefix_sum = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]

        for r in range(self.rows):
            for c in range(self.cols):
                # Inclusion-Exclusion Principle for 2D prefix sum:
                # Current sum = current value + top sum + left sum - top-left diagonal sum
                self.prefix_sum[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.prefix_sum[r][c + 1]
                    + self.prefix_sum[r + 1][c]
                    - self.prefix_sum[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Returns the sum of the elements inside the specified subrectangle.

        Args:
            row1: The starting row index.
            col1: The starting column index.
            row2: The ending row index.
            col2: The ending column index.

        Returns:
            The sum of the elements in the subrectangle defined by (row1, col1) and (row2, col2).

        Examples:
            >>> obj = SubrectangleQueries([[1, 2], [3, 4]])
            >>> obj.sumRegion(0, 0, 1, 1)
            10
            >>> obj.sumRegion(0, 1, 1, 1)
            6
        """
        # Using the precomputed prefix sum to calculate the area sum in O(1).
        # The formula uses the 1-based indexing of our prefix_sum table.
        # Sum = Total(r2, c2) - Top(r1-1, c2) - Left(r2, c1-1) + Overlap(r1-1, c1-1)
        return (
            self.prefix_sum[row2 + 1][col2 + 1]
            - self.prefix_sum[row1][col2 + 1]
            - self.prefix_sum[row2 + 1][col1]
            + self.prefix_sum[row1][col1]
        )

def solve():
    """
    Example usage of the SubrectangleQueries class.
    """
    matrix = [[1, 2], [3, 4]]
    obj = SubrectangleQueries(matrix)
    print(obj.sumRegion(0, 0, 1, 1))  # Expected: 10
    print(obj.sumRegion(0, 1, 1, 1))  # Expected: 6
