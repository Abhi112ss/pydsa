METADATA = {
    "id": 1198,
    "name": "Find Smallest Common Element in All Rows",
    "slug": "find-smallest-common-element-in-all-rows",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "array", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(R * C)",
    "space_complexity": "O(C)",
    "description": "Find the smallest element that appears in every row of a given 2D array.",
}

def solve(mat: list[list[int]]) -> int:
    """
    Finds the smallest element that is present in every row of the matrix.

    Args:
        mat: A 2D list of integers where each row is sorted in ascending order.

    Returns:
        The smallest common element if it exists, otherwise -1.

    Examples:
        >>> solve([[1, 2, 3], [2, 4], [3, 4, 5]])
        -1
        >>> solve([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
        3
        >>> solve([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
        1
    """
    if not mat or not mat[0]:
        return -1

    num_rows = len(mat)
    num_cols = len(mat[0])
    
    # Since the rows are sorted, the smallest common element must be 
    # one of the elements present in the first row.
    # We use a frequency map to count occurrences across all rows.
    # Because rows are sorted and contain unique elements (implied by problem constraints 
    # for finding the smallest common element efficiently), we can count 
    # how many rows each number appears in.
    
    counts = {}
    
    for row in mat:
        for element in row:
            # Increment the count for each element encountered.
            # Since each row is sorted and we only care about presence in a row,
            # we assume elements within a single row are unique for the purpose 
            # of finding a common element.
            counts[element] = counts.get(element, 0) + 1
            
            # If an element's count reaches the number of rows, it is a candidate.
            # However, to find the *smallest* one, we can't just return immediately 
            # unless we iterate through the first row in order.
    
    # To ensure we find the SMALLEST common element, we iterate through 
    # the first row (which is already sorted) and check the counts.
    for element in mat[0]:
        if counts.get(element) == num_rows:
            return element
            
    return -1
