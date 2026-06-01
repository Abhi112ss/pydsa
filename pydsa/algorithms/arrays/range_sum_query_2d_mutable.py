METADATA = {
    "id": 308,
    "name": "Range Sum Query 2D - Mutable",
    "slug": "range-sum-query-2d-mutable",
    "category": "Data Structure",
    "aliases": [],
    "tags": ["segment_tree", "binary_indexed_tree", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(log m * log n)",
    "space_complexity": "O(m * n)",
    "description": "Implement a data structure that supports point updates and range sum queries on a 2D matrix.",
}

class NumMatrix:
    """
    A class to handle 2D matrix updates and range sum queries using a 2D Binary Indexed Tree (Fenwick Tree).
    """

    def __init__(self, matrix: list[list[int]]):
        """
        Initializes the NumMatrix with the given 2D matrix.

        Args:
            matrix: A 2D list of integers.
        """
        if not matrix or not matrix[0]:
            self.rows = 0
            self.cols = 0
            self.bit = []
            self.original_matrix = []
            return

        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.original_matrix = [row[:] for row in matrix]
        
        # BIT is 1-indexed for easier bit manipulation
        self.bit = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]

        # Build the BIT in O(m * n * log m * log n)
        # Note: Can be optimized to O(m * n), but this is standard for BIT construction
        for r in range(self.rows):
            for c in range(self.cols):
                self._update_bit(r + 1, c + 1, self.original_matrix[r][c])

    def _update_bit(self, r: int, c: int, delta: int) -> None:
        """
        Internal helper to update the BIT structure.

        Args:
            r: 1-indexed row index.
            c: 1-indexed column index.
            delta: The value to add to the current cell.
        """
        i = r
        while i <= self.rows:
            j = c
            while j <= self.cols:
                self.bit[i][j] += delta
                j += j & (-j)  # Move to next responsible index in column
            i += i & (-i)      # Move to next responsible index in row

    def update(self, row: int, col: int, val: int) -> None:
        """
        Updates the value of the cell at (row, col) to val.

        Args:
            row: 0-indexed row index.
            col: 0-indexed column index.
            val: The new value to be placed in the cell.
        """
        delta = val - self.original_matrix[row][col]
        self.original_matrix[row][col] = val
        # Update the BIT with the difference (delta)
        self._update_bit(row + 1, col + 1, delta)

    def _query_prefix_sum(self, r: int, c: int) -> int:
        """
        Calculates the prefix sum from (0,0) to (r-1, c-1).

        Args:
            r: 1-indexed row boundary.
            c: 1-indexed column boundary.

        Returns:
            The sum of the rectangle from (0,0) to (r-1, c-1).
        """
        total_sum = 0
        i = r
        while i > 0:
            j = c
            while j > 0:
                total_sum += self.bit[i][j]
                j -= j & (-j)  # Move to parent index in column
            i -= i & (-i)      # Move to parent index in row
        return total_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Calculates the sum of the elements within the rectangle defined by (row1, col1) and (row2, col2).

        Args:
            row1: 0-indexed top row.
            col1: 0-indexed left column.
            row2: 0-indexed bottom row.
            col2: 0-indexed right column.

        Returns:
            The sum of the elements in the specified region.
        """
        # Using the 2D Inclusion-Exclusion Principle:
        # Sum(r1, c1, r2, c2) = PrefixSum(r2, c2) - PrefixSum(r1-1, c2) - PrefixSum(r2, c1-1) + PrefixSum(r1-1, c1-1)
        return (self._query_prefix_sum(row2 + 1, col2 + 1) 
                - self._query_prefix_sum(row1, col2 + 1) 
                - self._query_prefix_sum(row2 + 1, col1) 
                + self._query_prefix_sum(row1, col1))

def solve():
    """
    Example usage of the NumMatrix class.
    """
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    nm = NumMatrix(matrix)
    
    # Test case 1: sumRegion(2, 1, 4, 3)
    # Region: [[2, 0, 1], [1, 0, 1], [0, 3, 0]] -> Sum = 8
    print(f"Sum Region (2,1 to 4,3): {nm.sumRegion(2, 1, 4, 3)}") 
    
    # Test case 2: update(3, 2, 1)
    # Matrix[3][2] becomes 1. Original was 0.
    nm.update(3, 2, 1)
    
    # Test case 3: sumRegion(2, 1, 4, 3) after update
    # Region: [[2, 0, 1], [1, 1, 1], [0, 3, 0]] -> Sum = 9
    print(f"Sum Region (2,1 to 4,3) after update: {nm.sumRegion(2, 1, 4, 3)}")
