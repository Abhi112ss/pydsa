METADATA = {
    "id": 835,
    "name": "Maximal Score After Applying Operation",
    "slug": "maximal-score-after-applying-operation",
    "category": "Matrix",
    "aliases": ["Image Overlap"],
    "tags": ["matrix", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(N^4)",
    "space_complexity": "O(N^2)",
    "description": "Find the maximum number of overlapping 1s between two binary matrices by shifting one matrix.",
}

def solve(img1: list[list[int]], img2: list[list[int]]) -> int:
    """
    Calculates the maximum number of overlapping 1s between two binary matrices
    by applying any possible translation (shift) to one of the matrices.

    Args:
        img1: A 2D list of integers representing the first binary matrix.
        img2: A 2D list of integers representing the second binary matrix.

    Returns:
        The maximum number of overlapping 1s possible after shifting.

    Examples:
        >>> solve([[1, 0], [0, 1]], [[0, 1], [1, 0]])
        2
        >>> solve([[0, 1], [1, 0]], [[0, 1], [1, 0]])
        2
    """
    rows = len(img1)
    cols = len(img1[0])

    # Collect coordinates of all 1s in both matrices
    ones_img1 = []
    for r in range(rows):
        for c in range(cols):
            if img1[r][c] == 1:
                ones_img1.append((r, c))

    ones_img2 = []
    for r in range(rows):
        for c in range(cols):
            if img2[r][c] == 1:
                ones_img2.append((r, c))

    # A translation vector (dr, dc) represents the shift needed to align 
    # a cell from img1 with a cell from img2.
    # If img1[r1, c1] == 1 and img2[r2, c2] == 1, they overlap if 
    # the shift is (r2 - r1, c2 - c1).
    shift_counts: dict[tuple[int, int], int] = {}

    for r1, c1 in ones_img1:
        for r2, c2 in ones_img2:
            # Calculate the vector required to move img1[r1, c1] to img2[r2, c2]
            dr = r2 - r1
            dc = c2 - c1
            shift = (dr, dc)
            
            # Increment the frequency of this specific translation vector
            shift_counts[shift] = shift_counts.get(shift, 0) + 1

    # The maximum frequency in the hash map is the maximum overlap possible
    if not shift_counts:
        return 0
        
    return max(shift_counts.values())
