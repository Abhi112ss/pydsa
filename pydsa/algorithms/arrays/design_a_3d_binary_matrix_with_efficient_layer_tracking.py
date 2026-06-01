METADATA = {
    "id": 3391,
    "name": "Design a 3D Binary Matrix with Efficient Layer Tracking",
    "slug": "design-a-3d-binary-matrix-with-efficient-layer-tracking",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "arrays", "3d-matrix"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(D*R*C)",
    "description": "Design a data structure to manage a 3D binary matrix with efficient layer-based operations.",
}

class BinaryMatrix3D:
    """
    A data structure representing a 3D binary matrix (D x R x C).
    Supports point updates and layer-based sum queries.
    """

    def __init__(self, depth: int, rows: int, cols: int):
        """
        Initializes the 3D matrix with zeros.

        Args:
            depth (int): Number of layers (D).
            rows (int): Number of rows per layer (R).
            cols (int): Number of columns per layer (C).
        """
        self.depth = depth
        self.rows = rows
        self.cols = cols
        # Initialize the 3D matrix with 0s
        self.matrix = [[[0 for _ in range(cols)] for _ in range(rows)] for _ in range(depth)]
        # Maintain an auxiliary array to store the sum of each layer for O(1) layer sum access
        self.layer_sums = [0] * depth

    def update(self, d: int, r: int, c: int, val: int) -> None:
        """
        Updates the value at position (d, r, c) to val.

        Args:
            d (int): Depth index.
            r (int): Row index.
            c (int): Column index.
            val (int): New value (0 or 1).
        """
        old_val = self.matrix[d][r][c]
        if old_val != val:
            # Update the matrix cell
            self.matrix[d][r][c] = val
            # Update the precomputed layer sum to maintain O(1) layer sum queries
            diff = val - old_val
            self.layer_sums[d] += diff

    def get_value(self, d: int, r: int, c: int) -> int:
        """
        Returns the value at position (d, r, c).

        Args:
            d (int): Depth index.
            r (int): Row index.
            c (int): Column index.

        Returns:
            int: The value at the specified position.
        """
        return self.matrix[d][r][c]

    def get_layer_sum(self, d: int) -> int:
        """
        Returns the sum of all elements in layer d.

        Args:
            d (int): Depth index.

        Returns:
            int: The sum of elements in the specified layer.
        """
        return self.layer_sums[d]

def solve():
    """
    Example usage of the BinaryMatrix3D class.

    Returns:
        None
    """
    # Initialize a 2x3x3 matrix
    matrix_3d = BinaryMatrix3D(2, 3, 3)

    # Update some values
    matrix_3d.update(0, 0, 0, 1)
    matrix_3d.update(0, 1, 1, 1)
    matrix_3d.update(1, 2, 2, 1)

    # Test get_value
    assert matrix_3d.get_value(0, 0, 0) == 1
    assert matrix_3d.get_value(0, 1, 1) == 1
    assert matrix_3d.get_value(1, 2, 2) == 1
    assert matrix_3d.get_value(0, 1, 0) == 0

    # Test get_layer_sum
    # Layer 0 has two 1s: (0,0,0) and (0,1,1)
    assert matrix_3d.get_layer_sum(0) == 2
    # Layer 1 has one 1: (1,2,2)
    assert matrix_3d.get_layer_sum(1) == 1

    # Update value to change layer sum
    matrix_3d.update(0, 0, 0, 0)
    assert matrix_3d.get_layer_sum(0) == 1
