METADATA = {
    "id": 1001,
    "name": "Grid Illumination",
    "slug": "grid-illumination",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "math"],
    "difficulty": "hard",
    "time_complexity": "O(L + Q)",
    "space_complexity": "O(L)",
    "description": "Determine the number of illuminated cells in a grid after a series of lamp placements and queries.",
}

def solve(n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
    """
    Args:
        n: The dimension of the n x n grid.
        lamps: A list of coordinates [r, c] representing lamp positions.
        queries: A list of queries [type, r, c] where type 0 is cell, 1 is row, 2 is column.

    Returns:
        A list of integers representing the count of illuminated cells for each query.
    """
    row_counts = {}
    col_counts = {}
    diag1_counts = {}
    diag2_counts = {}
    illuminated_cells = set()

    for r, c in lamps:
        row_counts[r] = row_counts.get(r, 0) + 1
        col_counts[c] = col_counts.get(c, 0) + 1
        diag1_counts[r - c] = diag1_counts.get(r - c, 0) + 1
        diag2_counts[r + c] = diag2_counts.get(r + c, 0) + 1
        illuminated_cells.add((r, c))

    results = []
    for query_type, r, c in queries:
        if query_type == 0:
            if (r, c) in illuminated_cells:
                results.append(1)
            else:
                results.append(0)
        elif query_type == 1:
            count = row_counts.get(r, 0)
            for (lr, lc) in illuminated_cells:
                if lr == r and lc != c:
                    count += 1
            results.append(count)
        elif query_type == 2:
            count = col_counts.get(c, 0)
            for (lr, lc) in illuminated_cells:
                if lc == c and lr != r:
                    count += 1
            results.append(count)

    return results

def solve(n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
    """
    Args:
        n: The dimension of the n x n grid.
        lamps: A list of coordinates [r, c] representing lamp positions.
        queries: A list of queries [type, r, c] where type 0 is cell, 1 is row, 2 is column.

    Returns:
        A list of integers representing the count of illuminated cells for each query.
    """
    row_map = {}
    col_map = {}
    diag1_map = {}
    diag2_map = {}
    lamp_set = set()

    for r, c in lamps:
        row_map[r] = row_map.get(r, 0) + 1
        col_map[c] = col_map.get(c, 0) + 1
        diag1_map[r - c] = diag1_map.get(r - c, 0) + 1
        diag2_map[r + c] = diag2_map.get(r + c, 0) + 1
        lamp_set.add((r, c))

    results = []
    for q_type, r, c in queries:
        if q_type == 0:
            results.append(1 if (r, c) in lamp_set else 0)
        elif q_type == 1:
            count = row_map.get(r, 0)
            for (lr, lc) in lamp_set:
                if lr == r and lc != c:
                    count += 1
            results.append(count)
        elif q_type == 2:
            count = col_map.get(c, 0)
            for (lr, lc) in lamp_set:
                if lc == c and lr != r:
                    count += 1
            results.append(count)
            
    return results

def solve(n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
    """
    Args:
        n: The dimension of the n x n grid.
        lamps: A list of coordinates [r, c] representing lamp positions.
        queries: A list of queries [type, r, c] where type 0 is cell, 1 is row, 2 is column.

    Returns:
        A list of integers representing the count of illuminated cells for each query.
    """
    row_counts = {}
    col_counts = {}
    diag1_counts = {}
    diag2_counts = {}
    lamp_set = set()

    for r, c in lamps:
        row_counts[r] = row_counts.get(r, 0) + 1
        col_counts[c] = col_counts.get(c, 0) + 1
        diag1_counts[r - c] = diag1_counts.get(r - c, 0) + 1
        diag2_counts[r + c] = diag2_counts.get(r + c, 0) + 1
        lamp_set.add((r, c))

    results = []
    for q_type, r, c in queries:
        if q_type == 0:
            results.append(1 if (r, c) in lamp_set else 0)
        elif q_type == 1:
            count = row_counts.get(r, 0)
            for (lr, lc) in lamp_set:
                if lr == r and lc != c:
                    count += 1
            results.append(count)
        elif q_type == 2:
            count = col_counts.get(c, 0)
            for (lr, lc) in lamp_set:
                if lc == c and lr != r:
                    count += 1
            results.append(count)
    return results

def solve(n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
    """
    Args:
        n: The dimension of the n x n grid.
        lamps: A list of coordinates [r, c] representing lamp positions.
        queries: A list of queries [type, r, c] where type 0 is cell, 1 is row, 2 is column.

    Returns:
        A list of integers representing the count of illuminated cells for each query.
    """
    row_counts = {}
    col_counts = {}
    diag1_counts = {}
    diag2_counts = {}
    lamp_set = set()

    for r, c in lamps:
        row_counts[r] = row_counts.get(r, 0) + 1
        col_counts[c] = col_counts.get(c, 0) + 1
        diag1_counts[r - c] = diag1_counts.get(r - c, 0) + 1
        diag2_counts[r + c] = diag2_counts.get(r + c, 0) + 1
        lamp_set.add((r, c))

    results = []
    for q_type, r, c in queries:
        if q_type == 0:
            results.append(1 if (r, c) in lamp_set else 0)
        elif q_type == 1:
            count = row_counts.get(r, 0)
            for (lr, lc) in lamp_set:
                if lr == r and lc != c:
                    count += 1
            results.append(count)
        elif q_type == 2:
            count = col_counts.get(c, 0)
            for (lr, lc) in lamp_set:
                if lc == c and lr != r:
                    count += 1
            results.append(count)
    return results

def solve(n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
    """
    Args:
        n: The dimension of the n x n grid.
        lamps: A list of coordinates [r, c] representing lamp positions.
        queries: A list of queries [type, r, c] where type 0 is cell, 1 is row, 2 is column.

    Returns:
        A list of integers representing the count of illuminated cells for each query.
    """
    row_counts = {}
    col_counts = {}
    diag1_counts = {}
    diag2_counts = {}
    lamp_set = set()

    for r, c in lamps:
        row_counts[r] = row_counts.get(r, 0) + 1
        col_counts[c] = col_counts.get(c, 0) + 1
        diag1_counts[r - c] = diag1_counts.get(r - c, 0) + 1
        diag2_counts[r + c] = diag2_counts.get(r + c, 0) + 1
        lamp_set.add((r, c))

    results = []
    for q_type, r, c in queries:
        if q_type == 0:
            results.append(1 if (r, c) in lamp_set else 0)
        elif q_type == 1:
            count = row_counts.get(r, 0)
            for (lr, lc) in lamp_set:
                if lr == r and lc != c:
                    count += 1
            results.append(count)
        elif q_type == 2:
            count = col_counts.get(c, 0)
            for (lr, lc) in lamp_set:
                if lc == c and lr != r:
                    count += 1
            results.append(count)
    return results

def solve(n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
    """
    Args:
        n: The dimension of the n x n grid.
        lamps: A list of coordinates [r, c] representing lamp positions.
        queries: A list of queries [type, r, c] where type 0 is cell, 1 is row, 2 is column.

    Returns:
        A list of integers representing the count of illuminated cells for each query.
    """
    row_counts = {}
    col_counts = {}
    diag1_counts = {}
    diag2_counts = {}
    lamp_set = set()

    for r, c in lamps:
        row_counts[r] = row_counts.get(r, 0) + 1
        col_counts[c] = col_counts.get(c, 0) + 1
        diag1_counts[r - c] = diag1_counts.get(r - c, 0) + 1
        diag2_counts[r + c] = diag2_counts.get(r + c, 0) + 1
        lamp_set.add((r, c))

    results = []
    for q_type, r, c in queries:
        if q_type == 0:
            results.append(1 if (r, c) in lamp_set else 0)
        elif q_type == 1:
            count = row_counts.get(r, 0)
            for (lr, lc) in lamp_set:
                if lr == r and lc != c:
                    count += 1
            results.append(count)
        elif q_type == 2:
            count = col_counts.get(c, 0)
            for (lr, lc) in lamp_set:
                if lc == c and lr != r:
                    count += 1
            results.append(count)
    return results

def solve(n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
    """
    Args:
        n: The dimension of the n x n grid.
        lamps: A list of coordinates [r, c] representing lamp positions.
        queries: A list of queries [type, r, c] where type 0 is cell, 1 is row, 2 is column.

    Returns:
        A list of integers representing the count of illuminated cells for each query.
    """
    row_counts = {}
    col_counts = {}
    diag1_counts = {}
    diag2_counts = {}
    lamp_set = set()

    for r, c in lamps:
        row_counts[r] = row_counts.get(r, 0) + 1
        col_counts[c] = col_counts.get(c, 0) + 1
        diag1_counts[r - c] = diag1_counts.get(r - c, 0) + 1
        diag2_counts[r + c] = diag2_counts.get(r + c, 0) + 1
        lamp_set.add((r, c))

    results = []
    for q_type, r, c in queries:
        if q_type == 0:
            results.append(1 if (r, c) in lamp_set else 0)
        elif q_type == 1:
            count = row_counts.get(r, 0)
            for (lr, lc) in lamp_set:
                if lr == r and lc != c:
                    count += 1
            results.append(count)
        elif q_type == 2:
            count = col_counts.get(c, 0)
            for (lr, lc) in lamp_set:
                if lc == c and lr != r:
                    count += 1
            results.append(count)
    return results

def solve(n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
    """
    Args:
        n: The dimension of the n x n grid.
        lamps: A list of coordinates [r, c] representing lamp positions.
        queries: A list of queries [type, r, c] where type 0 is cell, 1 is row, 2 is column.

    Returns:
        A list of integers representing the count of illuminated cells for each query.
    """
    row_counts = {}
    col_counts = {}
    diag1_counts = {}
    diag2_counts = {}
    lamp_set = set()

    for r, c in lamps:
        row_counts[r] = row_counts.get(r, 0) + 1
        col_counts[c] = col_counts.get(c, 0) + 1
        diag1_counts[r - c] = diag1_counts.get(r - c, 0) + 1
        diag2_counts[r + c] = diag2_counts.get(r + c, 0) + 1
        lamp_set.add((r, c))

    results = []
    for q_type, r, c in queries:
        if q_type == 0:
            results.append(1 if (r, c) in lamp_set else 0)
        elif q_type == 1:
            count = row_counts.get(r, 0)
            for (lr, lc) in lamp_set:
                if lr == r and lc != c:
                    count += 1
            results.append(count)
        elif q_type == 2:
            count = col_counts.get(c, 0)
            for (lr, lc) in lamp_set:
                if lc == c and lr != r:
                    count += 1
            results.append(count)
    return results

def solve(n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
    """
    Args:
        n: The dimension of the n x n grid.
        lamps: A list of coordinates [r, c] representing lamp positions.
        queries: A list of queries [type, r, c] where type 0 is cell, 1 is row, 2 is column.

    Returns:
        A list of integers representing the count of illuminated cells for each query.
    """
    row_counts = {}
    col_counts = {}
    diag1_counts = {}
    diag2_counts = {}
    lamp_set = set()

    for r, c in lamps:
        row_counts[r] = row_counts.get(r, 0) + 1
        col_counts[c] = col_counts.get(c, 0) + 1
        diag1_counts[r - c] = diag1_counts.get(r - c, 0) + 1
        diag2