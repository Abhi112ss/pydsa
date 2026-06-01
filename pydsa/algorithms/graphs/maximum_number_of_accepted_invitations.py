METADATA = {
    "id": 1820,
    "name": "Maximum Number of Accepted Invitations",
    "slug": "maximum-number-of-accepted-invitations",
    "category": "Greedy",
    "aliases": [],
    "tags": ["graphs", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of people who can be invited such that each person is invited by exactly one person and invites exactly one person.",
}

def solve(invitations: list[list[int]]) -> int:
    """
    Calculates the maximum number of people who can be part of a valid invitation cycle.

    The problem asks for the maximum number of people such that each person is 
    invited by exactly one person and invites exactly one person. This is 
    equivalent to finding the sum of the lengths of all disjoint cycles in 
    the functional graph formed by the invitations.

    Args:
        invitations: A list of pairs [a, b] where person 'a' invites person 'b'.

    Returns:
        The maximum number of people that can be included in valid cycles.

    Examples:
        >>> solve([[1, 2], [2, 3], [3, 1], [4, 5], [5, 4]])
        6
        >>> solve([[1, 2], [2, 1], [3, 4], [4, 5], [5, 3]])
        5
    """
    # Map each person to the person they invite
    # Since each person invites at most one person, a dictionary is sufficient
    adj: dict[int, int] = {}
    for inviter, invitee in invitations:
        adj[inviter] = invitee

    visited: set[int] = set()
    total_people_in_cycles: int = 0

    # Iterate through all people who are inviters
    for person in list(adj.keys()):
        if person in visited:
            continue

        # Track the path of the current traversal to detect cycles
        path_map: dict[int, int] = {}
        current: int = person
        step: int = 0

        # Traverse the invitation chain
        while current in adj and current not in visited:
            visited.add(current)
            path_map[current] = step
            
            next_person = adj[current]
            
            # If the next person is in our current path, we found a new cycle
            if next_person in path_map:
                cycle_length = step - path_map[next_person] + 1
                total_people_in_cycles += cycle_length
                break
            
            # If the next person was visited in a previous traversal, no new cycle here
            if next_person in visited:
                break
                
            current = next_person
            step += 1

    return total_people_in_cycles
