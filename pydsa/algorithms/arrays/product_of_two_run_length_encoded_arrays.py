METADATA = {
    "id": 1868,
    "name": "Product of Two Run-Length Encoded Arrays",
    "slug": "product_of_two_run_length_encoded_arrays",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "arrays", "run-length encoding"],
    "difficulty": "medium",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n + m)",
    "description": "Multiply two run-length encoded arrays and return the result as a new run-length encoded array.",
}

def solve(encodedArray1: list[list[int]], encodedArray2: list[list[int]]) -> list[list[int]]:
    """
    Multiplies two run-length encoded arrays using a two-pointer approach.

    Args:
        encodedArray1: A list of [value, frequency] pairs representing the first array.
        encodedArray2: A list of [value, frequency] pairs representing the second array.

    Returns:
        A list of [value, frequency] pairs representing the product of the two arrays.

    Examples:
        >>> solve([[2, 3], [3, 2]], [[3, 2], [4, 3]])
        [[18, 2], [12, 3]]
        >>> solve([[1, 1], [2, 1]], [[1, 1], [2, 1]])
        [[1, 1], [4, 1], [1, 1]]
    """
    result: list[list[int]] = []
    i, j = 0, 0
    
    # Track remaining counts for the current segment in each array
    rem1 = encodedArray1[0][1] if encodedArray1 else 0
    rem2 = encodedArray2[0][1] if encodedArray2 else 0

    while i < len(encodedArray1) and j < len(encodedArray2):
        val1 = encodedArray1[i][0]
        val2 = encodedArray2[j][0]
        
        # Calculate the overlap length between the current segments
        overlap = min(rem1, rem2)
        product = val1 * val2
        
        # Add to result if product is non-zero and merges with previous segment
        if product != 0:
            if result and result[-1][0] == product:
                result[-1][1] += overlap
            else:
                result.append([product, overlap])
        
        # Update remaining counts and move pointers if a segment is exhausted
        rem1 -= overlap
        rem2 -= overlap
        
        if rem1 == 0:
            i += 1
            if i < len(encodedArray1):
                rem1 = encodedArray1[i][1]
        
        if rem2 == 0:
            j += 1
            if j < len(encodedArray2):
                rem2 = encodedArray2[j][1]

    return result
