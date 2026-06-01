METADATA = {
    "id": 2570,
    "name": "Merge Two 2D Arrays by Summing Values",
    "slug": "merge-two-2d-arrays-by-summing-values",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n + m)",
    "description": "Merge two sorted 2D arrays by summing values of elements with the same ID.",
}

def solve(id1: list[list[int]], id2: list[list[int]]) -> list[list[int]]:
    """
    Merges two 2D arrays where each element is [id, value].
    The arrays are sorted by id. If IDs match, sum their values.

    Args:
        id1: A list of lists where each sub-list is [id, value], sorted by id.
        id2: A list of lists where each sub-list is [id, value], sorted by id.

    Returns:
        A list of lists containing the merged [id, summed_value] pairs, sorted by id.

    Examples:
        >>> solve([[1, 2], [2, 3]], [[1, 4], [4, 5]])
        [[1, 6], [2, 3], [4, 5]]
        >>> solve([[1, 4], [4, 5]], [[1, 2], [2, 3]])
        [[1, 6], [2, 3], [4, 5]]
    """
    merged_result: list[list[int]] = []
    pointer_one = 0
    pointer_two = 0
    
    n = len(id1)
    m = len(id2)

    # Use a two-pointer approach to traverse both arrays simultaneously
    while pointer_one < n and pointer_two < m:
        current_id1 = id1[pointer_one][0]
        current_id2 = id2[pointer_two][0]

        if current_id1 == current_id2:
            # IDs match: sum the values and move both pointers
            summed_value = id1[pointer_one][1] + id2[pointer_two][1]
            merged_result.append([current_id1, summed_value])
            pointer_one += 1
            pointer_two += 1
        elif current_id1 < current_id2:
            # ID in first array is smaller: add it and move first pointer
            merged_result.append(id1[pointer_one])
            pointer_one += 1
        else:
            # ID in second array is smaller: add it and move second pointer
            merged_result.append(id2[pointer_two])
            pointer_two += 1

    # Append any remaining elements from id1
    while pointer_one < n:
        merged_result.append(id1[pointer_one])
        pointer_one += 1

    # Append any remaining elements from id2
    while pointer_two < m:
        merged_result.append(id2[pointer_two])
        pointer_two += 1

    return merged_result
