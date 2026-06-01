METADATA = {
    "id": 1303,
    "name": "Find the Team Size",
    "slug": "find_the_team_size",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return the size of each employee's team based on team IDs.",
}


def solve(team: list[int]) -> list[int]:
    """Return the size of each employee's team.

    Args:
        team: A list where team[i] is the team ID of the i‑th employee.

    Returns:
        A list of the same length where each element is the total number of
        employees sharing the same team ID as the corresponding employee.

    Examples:
        >>> solve([1,2,2,3,3,3])
        [1, 2, 2, 3, 3, 3]
        >>> solve([5,5,5,5])
        [4, 4, 4, 4]
    """
    # Count occurrences of each team ID.
    frequency: dict[int, int] = {}
    for team_id in team:
        frequency[team_id] = frequency.get(team_id, 0) + 1

    # Map each employee to the count of their team.
    result: list[int] = []
    for team_id in team:
        result.append(frequency[team_id])

    return result