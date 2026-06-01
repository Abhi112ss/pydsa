METADATA = {
    "id": 1817,
    "name": "Finding the Users Active Minutes",
    "slug": "finding-the-users-active-minutes",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "sets"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the number of active minutes for each user based on their unique active timestamps.",
}

def solve(users: list[list[int]], minutes: int) -> list[int]:
    """
    Calculates the number of users who have a specific number of active minutes.

    Args:
        users: A list of lists where each sublist contains the active minutes of a user.
        minutes: The total number of possible active minutes.

    Returns:
        A list of integers where the index i represents the number of users 
        with (i + 1) active minutes.

    Examples:
        >>> solve([[1, 2], [2], [1, 2, 3]], 3)
        [0, 1, 2]
        >>> solve([[1, 2], [2], [1, 2, 3]], 4)
        [0, 1, 2]
    """
    # Map to store the count of unique active minutes per user
    # Key: user_id (implied by index), Value: set of unique minutes
    user_active_minutes_map: dict[int, set[int]] = {}

    for user_minutes in users:
        # We use a set to automatically handle duplicate minutes for the same user
        unique_minutes = set(user_minutes)
        # Since the problem treats each sublist as a unique user, 
        # we can just track the size of the set.
        # We use a dummy key or just process them directly.
        # To follow the logic of "per user", we track the count of unique minutes.
        user_active_minutes_map[len(user_active_minutes_map)] = len(unique_minutes)

    # result[i] stores how many users have (i + 1) active minutes
    result = [0] * minutes

    # Iterate through the counts of unique minutes calculated for each user
    for count in user_active_minutes_map.values():
        # If a user has 'count' unique minutes, increment the index (count - 1)
        if count <= minutes:
            result[count - 1] += 1

    return result
