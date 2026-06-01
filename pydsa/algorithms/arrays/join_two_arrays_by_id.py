METADATA = {
    "id": 2722,
    "name": "Join Two Arrays by ID",
    "slug": "join-two-arrays-by-id",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n + m)",
    "description": "Join two arrays of objects by their ID, filling missing values with -1.",
}

def solve(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    """
    Joins two arrays of integer pairs by their ID.

    If an ID exists in both arrays, the values are merged. If an ID exists in 
    only one array, the missing value is filled with -1. The result is 
    sorted by ID in ascending order.

    Args:
        nums1: A list of lists where each sub-list is [id, val1].
        nums2: A list of lists where each sub-list is [id, val2].

    Returns:
        A list of lists containing the merged [id, val1, val2] sorted by id.

    Examples:
        >>> solve([[1, 2], [2, 3]], [[1, 4], [3, 5]])
        [[1, 2, 4], [2, 3, -1], [3, -1, 5]]
        >>> solve([[1, 2], [2, 3]], [[2, 4], [3, 5]])
        [[1, 2, -1], [2, 3, 4], [3, -1, 5]]
    """
    # Use a dictionary to map ID -> [val1, val2]
    # We initialize val1 and val2 to -1 to handle missing entries easily
    merged_map: dict[int, list[int]] = {}

    # Process the first array: store [val1, -1]
    for id_val, val in nums1:
        merged_map[id_val] = [val, -1]

    # Process the second array: 
    # If ID exists, update val2. If not, create new entry [ -1, val ]
    for id_val, val in nums2:
        if id_val in merged_map:
            merged_map[id_val][1] = val
        else:
            merged_map[id_val] = [-1, val]

    # Extract keys, sort them to ensure ascending order, and build the result
    sorted_ids = sorted(merged_map.keys())
    
    result: list[list[int]] = []
    for id_val in sorted_ids:
        # Construct the final [id, val1, val2] format
        values = merged_map[id_val]
        result.append([id_val, values[0], values[1]])

    return result
