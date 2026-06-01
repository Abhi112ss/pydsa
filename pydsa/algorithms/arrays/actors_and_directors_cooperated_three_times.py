METADATA = {
    "id": 1050,
    "name": "Actors and Directors Who Cooperated At Least Three Times",
    "slug": "actors-and-directors-who-cooperated-at-least-three-times",
    "category": "Database",
    "aliases": [],
    "tags": ["hash_map", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the number of pairs of actors and directors who have worked together at least three times.",
}

def solve(actor_id: list[int], director_id: list[int], timestamp: list[int]) -> int:
    """
    Calculates the number of actor-director pairs that have collaborated at least 3 times.

    Args:
        actor_id: A list of actor IDs for each collaboration.
        director_id: A list of director IDs for each collaboration.
        timestamp: A list of timestamps for each collaboration.

    Returns:
        The count of unique (actor, director) pairs with 3 or more collaborations.

    Examples:
        >>> solve([1, 1, 1, 1, 1], [1, 1, 1, 2, 2], [1, 2, 3, 4, 5])
        1
        >>> solve([1, 2, 2, 3, 3, 3], [1, 2, 3, 1, 2, 3], [1, 2, 3, 4, 5, 6])
        0
    """
    # Use a dictionary to store the frequency of each (actor, director) pair
    # The key is a tuple representing the unique pair
    collaboration_counts: dict[tuple[int, int], int] = {}

    # Iterate through all collaborations provided in the input lists
    for i in range(len(actor_id)):
        pair = (actor_id[i], director_id[i])
        
        # Increment the count for the specific actor-director pair
        collaboration_counts[pair] = collaboration_counts.get(pair, 0) + 1

    # Count how many pairs have a frequency of 3 or more
    result_count = 0
    for count in collaboration_counts.values():
        if count >= 3:
            result_count += 1

    return result_count
