METADATA = {
    "id": 3078,
    "name": "Match Alphanumerical Pattern in Matrix I",
    "slug": "match_alphanumerical_pattern_in_matrix_i",
    "category": "Matrix",
    "aliases": [],
    "tags": ["arrays", "string_matching", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n * k)",
    "space_complexity": "O(1)",
    "description": "Find all starting positions in a matrix where a given pattern can be matched in any of the 8 directions.",
}

def solve(matrix: list[list[str]], pattern: str) -> list[list[int]]:
    """
    Finds all starting coordinates (row, col) in a matrix where the pattern 
    can be matched in any of the 8 cardinal or diagonal directions.

    Args:
        matrix: A 2D list of single-character strings representing the grid.
        pattern: A string representing the sequence to search for.

    Returns:
        A list of [row, col] coordinates where the pattern starts.

    Examples:
        >>> solve([["a", "b"], ["c", "d"]], "ab")
        [[0, 0]]
        >>> solve([["a", "b", "a"], ["b", "a", "b"]], "aba")
        [[0, 0], [0, 2], [1, 1]]
    """
    if not matrix or not matrix[0] or not pattern:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    pattern_len = len(pattern)
    results = []

    # 8 possible directions: N, NE, E, SE, S, SW, W, NW
    directions = [
        (-1, 0), (-1, 1), (0, 1), (1, 1),
        (1, 0), (1, -1), (0, -1), (-1, -1)
    ]

    for r in range(rows):
        for c in range(cols):
            # Optimization: Only start checking if the first character matches
            if matrix[r][c] == pattern[0]:
                # If pattern is length 1, we found a match immediately
                if pattern_len == 1:
                    results.append([r, c])
                    continue

                # Check all 8 directions from the current cell
                match_found = False
                for dr, dc in directions:
                    is_match = True
                    for i in range(1, pattern_len):
                        nr, nc = r + dr * i, c + dc * i
                        
                        # Check boundaries and character equality
                        if not (0 <= nr < rows and 0 <= nc < cols) or matrix[nr][nc] != pattern[i]:
                            is_match = False
                            break
                    
                    if is_match:
                        match_found = True
                        break
                
                if match_found:
                    results.append([r, c])

    return results
