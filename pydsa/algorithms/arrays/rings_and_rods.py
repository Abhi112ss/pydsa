METADATA = {
    "id": 2103,
    "name": "Rings and Rods",
    "slug": "rings-and-rods",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "array", "stack"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine the order of rings on each rod by processing them from top to bottom.",
}

def solve(rings: list[list[int]], rods: int) -> list[list[int]]:
    """
    Determines the order of rings on each rod.

    The rings are given as [rod_index, ring_size]. To find the order from top to bottom,
    we process the rings in reverse order. The last ring processed for a specific rod
    will be the one at the bottom, and the first ring processed will be at the top.

    Args:
        rings: A list of lists where rings[i] = [rod_index, ring_size].
        rods: The number of rods.

    Returns:
        A list of lists where result[i] contains the ring sizes on rod i from top to bottom.

    Examples:
        >>> solve([[0, 5], [1, 4], [0, 3], [1, 2]], 2)
        [[5, 3], [4, 2]]
        >>> solve([[0, 1], [1, 2], [0, 3], [1, 4], [0, 5], [1, 6]], 2)
        [[1, 3, 5], [2, 4, 6]]
    """
    # Initialize the result list with empty lists for each rod
    result: list[list[int]] = [[] for _ in range(rods)]

    # Process rings in reverse order. 
    # Since the input provides rings in the order they are placed (bottom to top),
    # iterating backwards allows us to treat the first encountered ring for a rod
    # as the "top-most" ring.
    for i in range(len(rings) - 1, -1, -1):
        rod_index, ring_size = rings[i]
        
        # Append the ring size to the corresponding rod.
        # Because we iterate backwards, the ring that was placed last in the input
        # (the top ring) is added to the list first.
        result[rod_index].append(ring_size)

    return result
