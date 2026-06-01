METADATA = {
    "id": 849,
    "name": "Maximize Distance to Closest Person",
    "slug": "maximize-distance-to-closest-person",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum distance you can sit from the closest person in a row of seats.",
}

def solve(seats: list[str]) -> int:
    """
    Calculates the maximum distance to the closest person in a row of seats.

    Args:
        seats: A list of strings where '1' represents a person and '0' represents an empty seat.

    Returns:
        The maximum distance to the closest person.

    Examples:
        >>> solve(["1", "0", "0", "0", "1", "0", "0", "1"])
        2
        >>> solve(["1", "0", "0", "0"])
        3
        >>> solve(["0", "0", "0", "1"])
        3
    """
    n = len(seats)
    max_dist = 0
    last_person_idx = -1

    for i in range(n):
        if seats[i] == "1":
            if last_person_idx == -1:
                # Case 1: Leading zeros (distance from the start to the first person)
                max_dist = i
            else:
                # Case 2: Zeros between two people (distance is half the gap)
                # The closest person is at either end, so we take the midpoint
                gap_size = i - last_person_idx
                max_dist = max(max_dist, gap_size // 2)
            
            last_person_idx = i

    # Case 3: Trailing zeros (distance from the last person to the end)
    if last_person_idx != -1:
        max_dist = max(max_dist, (n - 1) - last_person_idx)

    return max_dist
