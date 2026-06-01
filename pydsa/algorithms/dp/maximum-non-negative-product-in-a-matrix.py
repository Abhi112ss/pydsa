METADATA = {
    "id": 1594,
    "name": "Maximum Non-Negative Product in a Matrix",
    "slug": "maximum-non-negative-product-in-a-matrix",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the maximum non-negative product of a contiguous sub-rectangle in a matrix.",
}

def solve(matrix: list[list[int]]) -> int:
    """
    Finds the maximum non-negative product of a contiguous sub-rectangle in a matrix.

    Args:
        matrix: A 2D list of integers.

    Returns:
        The maximum non-negative product found in any sub-rectangle. 
        Returns 0 if no positive product is possible and 0 is in the matrix.

    Examples:
        >>> solve([[1, -2, -3], [4, 5, 6]])
        120
        >>> solve([[-1, -2], [-3, -4]])
        12
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    max_product = 0
    has_zero = False

    # We iterate through all possible pairs of row boundaries (top, bottom)
    # This reduces the 2D problem into a 1D problem similar to Maximum Product Subarray
    for top_row in range(rows):
        # column_products stores the product of elements from top_row to bottom_row for each column
        # We use a list to keep track of the product of elements in the current vertical strip
        column_products = [1] * cols
        
        for bottom_row in range(top_row, rows):
            for col in range(cols):
                column_products[col] *= matrix[bottom_row][col]
                if matrix[bottom_row][col] == 0:
                    has_zero = True

            # Now solve the 1D "Maximum Product Subarray" problem on column_products
            # We need to track both max and min because a negative * negative = positive
            current_max = 1
            current_min = 1
            
            # To handle zeros in the 1D array, we treat them as boundaries
            # or reset the running products.
            for val in column_products:
                if val == 0:
                    current_max = 1
                    current_min = 1
                    continue
                
                # If val is negative, swapping max and min handles the sign flip
                if val < 0:
                    current_max, current_min = current_min, current_max
                
                # Standard Kadane-like logic for product
                current_max = max(val, current_max * val)
                current_min = min(val, current_min * val)
                
                # Update global maximum if the current product is non-negative
                if current_max > max_product:
                    max_product = current_max

    # If no positive product was found but a zero exists, the answer is 0
    if max_product == 0 and has_zero:
        return 0
        
    return max_product
