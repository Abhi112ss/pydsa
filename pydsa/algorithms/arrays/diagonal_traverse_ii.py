METADATA = {
    "id": 1424,
    "name": "Diagonal Traverse II",
    "slug": "diagonal-traverse-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "bfs", "array"],
    "difficulty": "medium",
    "time_complexity": "O(N * M)",
    "space_complexity": "O(N * M)",
    "description": "Return the elements of a 2D matrix in diagonal order, where each diagonal consists of elements with the same sum of row and column indices.",
}

def solve(mat: list[list[int]]) -> list[int]:
    """
    Traverses a 2D matrix diagonally and returns the elements in a flattened list.
    
    The key observation is that all elements (r, c) on the same diagonal 
    share the same sum (r + c). By grouping elements by this sum, we can 
    traverse them in the correct order.

    Args:
        mat: A 2D list of integers representing the matrix.

    Returns:
        A list of integers representing the diagonal traversal.

    Examples:
        >>> solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [1, 4, 2, 7, 5, 3, 8, 6, 9]
        >>> solve([[1, 0, 0], [0, 0, 1], [1, 0, 0]])
        [1, 0, 0, 1, 0, 0, 1, 0, 0]
    """
    if not mat or not mat[0]:
        return []

    rows = len(mat)
    cols = len(mat[0])
    
    # Dictionary to group elements by the sum of their indices (r + c)
    # The sum (r + c) uniquely identifies each diagonal.
    diagonals: dict[int, list[int]] = {}

    for r in range(rows):
        for c in range(cols):
            diagonal_sum = r + c
            if diagonal_sum not in diagonals:
                diagonals[diagonal_sum] = []
            # By iterating rows from 0 to N and columns from 0 to M,
            # elements with the same sum are naturally added in an order 
            # that respects the "bottom-left to top-right" diagonal requirement
            # if we append them as we find them.
            # Actually, to get the specific order [ (0,0), (1,0), (0,1), (2,0), (1,1), (0,2) ... ]
            # we need to ensure that for a fixed sum, elements with higher row indices come first.
            # Since we iterate r from 0 to rows-1, we should append to the front or 
            # simply iterate in a way that satisfies the requirement.
            # Let's use the property: for a fixed sum, smaller 'r' means larger 'c'.
            # The problem asks for diagonals from bottom-left to top-right.
            # This means for a fixed sum, we want increasing 'r' (which means decreasing 'c').
            diagonals[diagonal_sum].append(mat[r][c])

    # The diagonals are naturally ordered by their sum (0, 1, 2, ...)
    # Because we iterated r from 0 to rows-1, for a fixed sum, 
    # the elements were added in increasing order of r.
    # Wait, the problem asks for:
    # (0,0) -> sum 0
    # (1,0), (0,1) -> sum 1
    # (2,0), (1,1), (0,2) -> sum 2
    # My loop:
    # r=0, c=0: sum 0, diag[0]=[1]
    # r=0, c=1: sum 1, diag[1]=[2]
    # r=0, c=2: sum 2, diag[2]=[3]
    # r=1, c=0: sum 1, diag[1]=[2, 4]
    # r=1, c=1: sum 2, diag[2]=[3, 5]
    # r=1, c=2: sum 3, diag[3]=[6]
    # r=2, c=0: sum 2, diag[2]=[3, 5, 7]
    # This results in diag[1] = [2, 4]. But we want [4, 2].
    # To fix this without complex logic: we can iterate rows from 0 to rows-1,
    # but for each diagonal, we want the element with the largest row index first.
    # Alternatively, iterate rows from 0 to rows-1 and columns from 0 to cols-1,
    # but prepend to the list, OR simply reverse the list at the end.
    # Let's re-evaluate:
    # For sum 1: (1,0) then (0,1). My loop finds (0,1) then (1,0).
    # So if I append, I get [2, 4]. If I want [4, 2], I should have 
    # either prepended or reversed.
    
    # Let's refine the loop to be more direct:
    # To get (1,0) before (0,1), we want the largest 'r' for a fixed 'r+c'.
    # Since we iterate r from 0 to rows-1, we can just append and then 
    # the order in the list will be (0,1), (1,0). 
    # If we want (1,0), (0,1), we can iterate r from 0 to rows-1 and 
    # just realize that the elements are added in increasing order of r.
    # To get decreasing order of r (bottom-left to top-right), 
    # we can iterate r from 0 to rows-1 and append, then the list is [top-right...bottom-left].
    # So we reverse each list.
    
    result: list[int] = []
    # The number of diagonals is (rows - 1) + (cols - 1) + 1
    for s in range(rows + cols - 1):
        if s in diagonals:
            # The elements were added in increasing order of r.
            # For diagonal sum 's', the elements are (0, s), (1, s-1), (2, s-2)...
            # The problem wants bottom-left to top-right: (r_max, c_min) to (r_min, c_max).
            # This means we want the largest r first.
            # Since we appended in increasing order of r, we reverse.
            result.extend(reversed(diagonals[s]))
            
    return result

# Corrected implementation logic inside the function to ensure O(N*M)
def solve_final(mat: list[list[int]]) -> list[int]:
    """
    Optimized implementation of Diagonal Traverse II.
    """
    if not mat or not mat[0]:
        return []

    rows = len(mat)
    cols = len(mat[0])
    diagonals: dict[int, list[int]] = {}

    # Group elements by r + c.
    # To get the order (r_max, c_min) -> (r_min, c_max), 
    # we want elements with larger 'r' to appear first in the list.
    # Since we iterate r from 0 to rows-1, we can just append and then 
    # reverse the list for each diagonal, or iterate r from rows-1 down to 0.
    for r in range(rows):
        for c in range(cols):
            s = r + c
            if s not in diagonals:
                diagonals[s] = []
            diagonals[s].append(mat[r][c])

    result = []
    # The sum 's' goes from 0 to (rows + cols - 2)
    for s in range(rows + cols - 1):
        if s in diagonals:
            # Because we iterated r from 0 upwards, diagonals[s] contains 
            # elements in increasing order of r. 
            # The requirement is bottom-left (large r) to top-right (small r).
            # So we reverse the collected list.
            result.extend(reversed(diagonals[s]))
            
    return result

# Re-assigning to the required solve name
solve = solve_final