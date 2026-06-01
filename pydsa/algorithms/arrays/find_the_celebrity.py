METADATA = {
    "id": 277,
    "name": "Find the Celebrity",
    "slug": "find-the-celebrity",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "two_pointer", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the person in a group who is known by everyone but knows no one.",
}

def solve(n: int, knows: callable) -> int:
    """
    Finds the celebrity in a group of n people using a two-pass approach.
    
    A celebrity is defined as someone who:
    1. Is known by everyone else in the group.
    2. Knows no one else in the group.

    Args:
        n: The number of people in the group.
        knows: A helper function `knows(a, b)` that returns True if a knows b, 
               and False otherwise.

    Returns:
        The index of the celebrity if one exists, otherwise -1.

    Examples:
        >>> def mock_knows(a, b):
        ...     # Person 1 is the celebrity
        ...     matrix = [[0, 1, 0], [0, 0, 0], [0, 1, 0]]
        ...     return matrix[a][b] == 1
        >>> solve(3, mock_knows)
        1
    """
    if n <= 0:
        return -1

    # Step 1: Find a potential candidate using a greedy elimination approach.
    # If A knows B, A cannot be the celebrity.
    # If A does not know B, B cannot be the celebrity.
    candidate = 0
    for person in range(1, n):
        if knows(candidate, person):
            # Current candidate knows someone, so they cannot be the celebrity.
            # The person they know might be the celebrity.
            candidate = person

    # Step 2: Verify the candidate.
    # The elimination process only guarantees that if a celebrity exists, 
    # it must be the 'candidate'. We must check the two celebrity conditions.
    for person in range(n):
        if person == candidate:
            continue
        
        # Condition 1: The celebrity must not know anyone.
        # Condition 2: Everyone else must know the celebrity.
        if knows(candidate, person) or not knows(person, candidate):
            return -1

    return candidate
