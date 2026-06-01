METADATA = {
    "id": 1253,
    "name": "Reconstruct a 2-Row Binary Matrix",
    "slug": "reconstruct-a-2-row-binary-matrix",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "matrix", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Reconstruct a 2-row binary matrix given the sums of its rows and the sums of its columns.",
}

def solve(row_sums: list[int], col_sums: list[int]) -> list[list[int]]:
    """
    Reconstructs a 2-row binary matrix based on row and column sums using a greedy approach.

    Args:
        row_sums: A list of two integers representing the sum of each row.
        col_sums: A list of integers representing the sum of each column.

    Returns:
        A 2xN binary matrix if reconstruction is possible, otherwise an empty list.

    Examples:
        >>> solve([2, 2], [1, 1, 1, 1])
        [[1, 1, 0, 0], [0, 0, 1, 1]] (or any valid permutation)
        >>> solve([1, 1], [1, 1])
        [[1, 0], [0, 1]]
        >>> solve([1, 1], [2, 0])
        []
    """
    num_rows = len(row_sums)
    num_cols = len(col_sums)

    # Basic validation: total sum of rows must equal total sum of columns
    if sum(row_sums) != sum(col_sums):
        return []

    # Initialize the result matrix with zeros
    matrix = [[0] * num_cols for _ in range(num_rows)]

    # Track remaining capacity for each row
    remaining_row_sums = list(row_sums)

    for col_idx in range(num_cols):
        current_col_sum = col_sums[col_idx]

        # Case 1: Column sum is 2. Both rows must have a 1 in this column.
        if current_col_sum == 2:
            for row_idx in range(num_rows):
                if remaining_row_sums[row_idx] > 0:
                    matrix[row_idx][col_idx] = 1
                    remaining_row_sums[row_idx] -= 1
                else:
                    # If a row cannot accept a 1, reconstruction is impossible
                    return []

        # Case 2: Column sum is 1. One row must have a 1, the other a 0.
        elif current_col_sum == 1:
            # Greedily assign the 1 to the row that currently has more remaining sum needed
            # This ensures we don't run out of capacity for rows that need more 1s later.
            assigned = False
            # Sort rows by remaining capacity descending to pick the best candidate
            # However, since it's only 2 rows, we can just check which one is larger.
            if remaining_row_sums[0] >= remaining_row_sums[1]:
                target_row = 0
            else:
                target_row = 1
            
            if remaining_row_sums[target_row] > 0:
                matrix[target_row][col_idx] = 1
                remaining_row_sums[target_row] -= 1
                assigned = True
            
            if not assigned:
                return []

        # Case 3: Column sum is 0. No action needed (already 0).
        elif current_col_sum == 0:
            pass

        # Case 4: Invalid column sum for a 2-row matrix
        else:
            return []

    # Final check: Ensure all row requirements were exactly met
    if any(val != 0 for val in remaining_row_sums):
        return []

    return matrix
