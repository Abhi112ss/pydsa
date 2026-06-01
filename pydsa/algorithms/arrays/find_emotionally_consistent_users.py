METADATA = {
    "id": 3808,
    "name": "Find Emotionally Consistent Users",
    "slug": "find_emotionally_consistent_users",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "arrays", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(n * m)",
    "description": "Group users whose emotional expression patterns follow the same relative sequence of changes.",
}

def solve(users: list[list[int]]) -> list[int]:
    """
    Identifies the IDs of users who belong to the largest group of 
    emotionally consistent users based on their expression patterns.

    An emotional pattern is defined by the sequence of relative changes 
    (differences) between consecutive emotional states.

    Args:
        users: A list of lists, where each sub-list contains [user_id, state_1, state_2, ..., state_k].

    Returns:
        A list of user IDs that belong to the largest group of consistent users. 
        If there is a tie, the group with the smallest user ID is returned.

    Examples:
        >>> solve([[1, 1, 2, 1], [2, 5, 6, 5], [3, 1, 1, 1]])
        [1, 2]
        >>> solve([[1, 1, 2, 3], [2, 10, 11, 12], [3, 1, 2, 1]])
        [1, 2]
    """
    # Map to store the pattern (tuple of differences) to a list of user IDs
    pattern_groups: dict[tuple[int, ...], list[int]] = {}

    for user_data in users:
        user_id = user_data[0]
        states = user_data[1:]
        
        # Calculate the sequence of differences between consecutive states
        # This normalizes the pattern (e.g., [1, 2, 1] and [5, 6, 5] both become (1, -1))
        if len(states) <= 1:
            # A single state has an empty difference pattern
            pattern = ()
        else:
            differences = []
            for i in range(len(states) - 1):
                differences.append(states[i + 1] - states[i])
            pattern = tuple(differences)
        
        if pattern not in pattern_groups:
            pattern_groups[pattern] = []
        pattern_groups[pattern].append(user_id)

    # Find the maximum group size
    max_size = 0
    for group in pattern_groups.values():
        if len(group) > max_size:
            max_size = len(group)

    # Collect all groups that have the maximum size
    candidate_groups = []
    for group in pattern_groups.values():
        if len(group) == max_size:
            # Sort IDs within the group to handle tie-breaking logic easily
            candidate_groups.append(sorted(group))

    # Tie-breaking: Return the group whose smallest user ID is the minimum among all largest groups
    # Sort the groups based on their first element (the smallest ID in that group)
    candidate_groups.sort(key=lambda x: x[0])

    return candidate_groups[0]
