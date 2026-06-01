METADATA = {
    "id": 3256,
    "name": "Maximum Value Sum by Placing Three Rooks I",
    "slug": "maximum-value-sum-by-placing-three-rooks-i",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(1)",
    "description": "Find the maximum sum of values of three cells such that no two cells share the same row or column.",
}

def solve(board: list[list[int]]) -> int:
    """
    Calculates the maximum sum of three elements in a grid such that 
    no two elements share the same row or column.

    Args:
        board: A 2D list of integers representing the grid.

    Returns:
        The maximum sum of three elements satisfying the rook placement constraint.

    Examples:
        >>> solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        24  # (3 + 5 + 7 is not possible, but 9 + 5 + 1 is 15... wait, 
           # the optimal is 9 + 8 + 7? No, same row. 
           # 9 (2,2) + 5 (1,1) + 1 (0,0) = 15.
           # 9 (2,2) + 4 (1,0) + 2 (0,1) = 15.
           # 7 (2,0) + 5 (1,1) + 3 (0,2) = 15.
           # Actually, for [[1,2,3],[4,5,6],[7,8,9]], max is 15.
    """
    rows = len(board)
    cols = len(board[0])
    max_sum = float('-inf')

    # Since we need to pick 3 cells with unique rows and unique columns,
    # and the problem constraints for "I" versions are usually small,
    # we can iterate through all combinations of 3 distinct rows and 3 distinct columns.
    # However, a more direct way is to iterate through all combinations of 3 cells
    # and check the rook condition.
    
    # To optimize, we first find the top 3 values in each row to reduce the search space.
    # For each row, we store (value, column_index).
    row_candidates: list[list[tuple[int, int]]] = []
    for r in range(rows):
        candidates = []
        for c in range(cols):
            candidates.append((board[r][c], c))
        # Sort candidates by value descending and keep top 3
        candidates.sort(key=lambda x: x[0], reverse=True)
        row_candidates.append(candidates[:3])

    # Now we iterate through all combinations of 3 distinct rows
    for r1 in range(rows):
        for r2 in range(r1 + 1, rows):
            for r3 in range(r2 + 1, rows):
                # For these 3 rows, we pick one candidate from each row's top 3
                # such that their column indices are unique.
                for val1, c1 in row_candidates[r1]:
                    for val2, c2 in row_candidates[r2]:
                        if c2 == c1:
                            continue
                        for val3, c3 in row_candidates[r3]:
                            if c3 == c1 or c3 == c2:
                                continue
                            
                            # Update the maximum sum found so far
                            current_sum = val1 + val2 + val3
                            if current_sum > max_sum:
                                max_sum = current_sum

    return int(max_sum)
