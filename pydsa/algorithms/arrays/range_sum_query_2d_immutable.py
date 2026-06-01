METADATA = {
    "id": 304,
    "name": "Range Sum Query 2D - Immutable",
    "slug": "range-sum-query-2d-immutable",
    "category": "Prefix Sum",
    "aliases": [],
    "tags": ["prefix_sum", "matrix", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(1) per query, O(m*n) preprocessing",
    "space_complexity": "O(m*n)",
    "description": "Precompute a 2D prefix sum matrix to answer rectangle sum queries in constant time.",
}

class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        """
        Initializes the NumMatrix object with the given 2D matrix.
        
        Args:
            matrix: A 2D list of integers.
        """
        if not matrix or not matrix[0]:
            self.prefix_sums = []
            return

        rows = len(matrix)
        cols = len(matrix[0])
        
        # Create a prefix sum matrix with an extra row and column of zeros
        # to handle boundary conditions (i-1, j-1) without extra if-statements.
        self.prefix_sums = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                # The sum at (r+1, c+1) is the current value + top + left - diagonal_top_left
                # This avoids double counting the overlapping area.
                self.prefix_sums[r + 1][c + 1] = (
                    matrix[r][c] 
                    + self.prefix_sums[r][c + 1] 
                    + self.prefix_sums[r + 1][c] 
                    - self.prefix_sums[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Returns the sum of the elements of the matrix inside the rectangle 
        defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

        Args:
            row1: Top row index.
            col1: Left column index.
            row2: Bottom row index.
            col2: Right column index.

        Returns:
            The sum of the elements in the specified rectangle.

        Examples:
            >>> nm = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,6,7],[4,1,5,0,3]])
            >>> nm.sumRegion(2, 1, 3, 3)
            8
        """
        if not self.prefix_sums:
            return 0

        # Using the inclusion-exclusion principle:
        # Total area (0,0 to row2,col2) 
        # minus top part (0,0 to row1-1,col2)
        # minus left part (0,0 to row2,col1-1)
        # plus the double-subtracted corner (0,0 to row1-1,col1-1)
        # Note: We use +1 offset because prefix_sums is 1-indexed relative to matrix.
        return (
            self.prefix_sums[row2 + 1][col2 + 1]
            - self.prefix_sums[row1][col2 + 1]
            - self.prefix_sums[row2 + 1][col1]
            + self.prefix_sums[row1][col1]
        )

def solve():
    """
    Entry point for testing the implementation.
    """
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 6, 7], [4, 1, 5, 0, 3]]
    nm = NumMatrix(matrix)
    
    # Test case 1
    assert nm.sumRegion(2, 1, 3, 3) == 8
    # Test case 2
    assert nm.sumRegion(1, 1, 2, 2) == 11
    # Test case 3
    assert nm.sumRegion(0, 0, 1, 1) == 14
    
    print("All test cases passed!")
