METADATA = {
    "id": 1282,
    "name": "Group the People Given the Group Size They Belong To",
    "slug": "group-the-people-given-the-group-size-they-belong-to",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Group people into sets of a specific size based on the group size requirement provided for each person.",
}

def solve(groupSizes: list[int]) -> list[list[int]]:
    """
    Groups people into lists based on the required group size specified in groupSizes.

    Args:
        groupSizes: A list of integers where groupSizes[i] is the size of the 
            group that person i belongs to.

    Returns:
        A list of lists, where each inner list contains the indices of people 
        forming a complete group.

    Examples:
        >>> solve([3, 3, 3, 3, 3, 1, 1])
        [[0, 1, 2], [3, 4, 5], [6]] (Note: order of groups/elements may vary)
        >>> solve([1, 1, 1, 1])
        [[0], [1], [2], [3]]
    """
    # Map to store current partial groups being formed for each group size
    # Key: group size, Value: list of indices currently in that group
    group_map: dict[int, list[int]] = {}
    result: list[list[int]] = []

    for person_index, size in enumerate(groupSizes):
        # Initialize the list for a new group size if not seen before
        if size not in group_map:
            group_map[size] = []
        
        # Add the current person to their respective group size bucket
        group_map[size].append(person_index)

        # If the current bucket reaches the required size, move it to result
        if len(group_map[size]) == size:
            result.append(group_map[size])
            # Clear the bucket to start forming the next group of the same size
            group_map[size] = []

    return result
